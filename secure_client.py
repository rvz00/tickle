import os
import pickle
import hmac
import hashlib

key = 'My SeCret KeY'

def fun(name,password):
    s = {"username":name,"password":password}
    safecode = pickle.dumps(s)
    digest = str.encode(hmac.new(bytes(key, 'latin-1'), safecode, hashlib.sha512).hexdigest())

    with open("users.json","wb") as f:
        f.write(digest + b'\x23\x20\x23' + safecode)
    return digest

if __name__ == '__main__':
    u = input("Username : ")
    p = input("Password : ")
    yo_fun = fun(u,p)
