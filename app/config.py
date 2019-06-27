from synapsepy import Client

# please change client_id, client_secret,fingerprint, or ip_address if needed.
client_id = 'client_id_270ltbWxdXaGJT5sFEePNUR4n0gz9CoYZiQkSuML'
client_secret = 'client_secret_gWL1sPb3zn5Y4kydBHwu9F8Ta62NtE0lRqi7MQKS'
fingerprint = 'ee422391e52e3b8a81d44fd0a508a84f'
ip_address = '1.2.3.132'
usr_id = '5d0be3f12beda64993244caf'

client = Client(
    client_id=client_id,
    client_secret=client_secret,
    fingerprint=fingerprint,
    ip_address=ip_address,
    devmode=True
)
