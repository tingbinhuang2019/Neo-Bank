from synapsepy import Client
from datetime import datetime
import time
from config import client, fingerprint, ip_address


def update_user_balance(db, today, user):
    today = str(datetime.date(datetime.today()))
    new_balance = "balance." + today

    if user["last_tran_date"] != today:
        date = user["last_tran_date"]
        pre_balance = user["balance"][date]
        db.update({"name": user["name"]}, {
            "$set": {new_balance: pre_balance}})
        db.update({"name": user["name"]}, {
                  "$set": {"last_tran_date": today}})


def create_user_trans(db, amount, fromWho, toWho):

    sender = db.find_one({"name": fromWho})
    receiver = db.find_one({"name": toWho})

    body = {
        "to": {
            "type": "ACH-US",
            "id": receiver["node_id"]
        },
        "amount": {
            "amount": amount,
            "currency": "USD"
        },
        "extra": {
            "ip": "192.168.0.1"
        }
    }
    id = str(sender["user_id"])

    sender_node = client.get_user(
        id, ip=ip_address, fingerprint=fingerprint, full_dehydrate=True)
    sender_node.create_trans(sender["node_id"], body)

    # update user balance in database as transaction is being created
    update_user_balance(db, str(datetime.date(datetime.today())), sender)
    update_user_balance(db, str(datetime.date(datetime.today())), receiver)

    # update user transaction info in database
    record_trans(sender, receiver, db, amount)


def record_trans(sender, receiver, db, amount):
    today = str(datetime.date(datetime.today()))
    new_balance = "balance." + today
    tran = "transaction." + today
    current_balance = "balance." + today

    # update sender information
    date1 = sender["last_tran_date"]
    sender_balance = str(

        float(sender["balance"][date1]) - float(amount))

    sender_outgoing_data = {"in": "False",
                            "node_id": str(receiver["node_id"]), "name": receiver["name"], "amount": amount}
    db.update_one({"name": sender["name"]}, {
                  "$push": {tran: sender_outgoing_data}})
    db.update_one({"name": sender["name"]}, {
                  "$set": {current_balance: sender_balance}})

    # update receiver information
    date2 = receiver["last_tran_date"]
    receiver_balance = str(
        float(receiver["balance"][date2]) + float(amount))
    receiver_incoming_data = {"in": "True",
                              "node_id": str(sender["node_id"]), "name": sender["name"], "amount": amount}
    db.update_one({"name": receiver["name"]}, {
                  "$push": {tran: receiver_incoming_data}})
    db.update_one({"name": receiver["name"]}, {
                  "$set": {current_balance: receiver_balance}})
