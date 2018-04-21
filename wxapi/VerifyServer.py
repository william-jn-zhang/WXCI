import hashlib
from config.cfg import VERIFY_TOKEN

def verifyServer(signature, timestamp, nonce):
    token = VERIFY_TOKEN
    list = [token, timestamp, nonce]
    list = sorted(list)
    str = "".join(list)
    digest = hashlib.sha1(str).hexdigest()
    if signature == digest:
        return True
    else:
        return False

