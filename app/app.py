from flask import request, Response
from flask import Flask
from synapsepy import Client
import json

app = Flask(__name__)

client = Client(
    client_id='client_id_270ltbWxdXaGJT5sFEePNUR4n0gz9CoYZiQkSuML',
    client_secret='client_secret_gWL1sPb3zn5Y4kydBHwu9F8Ta62NtE0lRqi7MQKS',
    fingerprint='ee422391e52e3b8a81d44fd0a508a84f',
    ip_address='1.2.3.132',
    devmode=True
)

usr_id = '5d0be3f12beda64993244caf'
usr = client.get_user(usr_id, full_dehydrate=True)

# ---------------------
name = 'Tim'
email = 'louie121201huang@gmail.com'
# ----------------------


@app.route('/getData', methods=["GET"])
def getDatea():
    obj = usr.body
    p = json.dumps(obj, sort_keys=False, indent=1)
    res = Response(p, mimetype='application/json')
    return res


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
