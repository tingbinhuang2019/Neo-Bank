from flask import request, Response
from flask import Flask
from synapsepy import Client
import json
from pymongo import MongoClient
from datetime import datetime
import time
import pprint
from cleanData import create_user, clean_user_data, remove_user_data
from createTrans import create_user_trans
from config import client, fingerprint, ip_address, usr_id

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.check
col = db.uuu

# method to check if database has user name


def hasUser(name):
    return (col.find_one({"name": name})) != None

# get and post method
@app.route('/getData', methods=["GET", "POST"])
def getData():
    name = request.args.get("new_user")
    if not hasUser(name):
        body = create_user(name, fingerprint)
        col.insert_one(body)
    obj = col.find_one({"name": name})
    user_data = clean_user_data(obj)
    p = json.dumps(user_data, sort_keys=False, indent=1)
    res = Response(p, mimetype='application/json')
    return res

# patch method
@app.route('/createTransaction', methods=["GET", "PATCH"])
def updateData():
    fromWho = request.args.get("sender")
    toWho = request.args.get("receiver")
    amount = request.args.get('amount')

    if not hasUser(fromWho) or not hasUser(toWho):
        return Response("no such user, please re-enter user name.", mimetype='application/json')
    d = create_user_trans(col, amount, fromWho, toWho)

    d = {"sender": fromWho,
         "receiver": toWho,
         "amount": amount}
    p = json.dumps(d, sort_keys=False, indent=1)
    res = Response(p, mimetype='application/json')
    return res

# delete method
@app.route('/delete', methods=["GET", "POST", "DELETE"])
def removeUser():
    remove_user = request.args.get("remove_user")

    if not hasUser(remove_user):
        return Response("No such user in database.", mimetype='application/json')
    remove_user_data(remove_user, col)
    message = "User " + remove_user + " has been removed."
    return Response(message, mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)
