import os
import pickle
import hashlib
import hmac
import secrets

key = "My SeCret KeY"


def reverse_fun():
    with open("users.json", "rb") as f:
        data = f.read()

    try:
        digest, pickle_data = data.split(b'\x23\x20\x23')
        expected_digest = str.encode(hmac.new(bytes(key, 'latin-1'), pickle_data, digestmod=hashlib.sha512).hexdigest())

        if not secrets.compare_digest(digest, expected_digest):
            print('Invalid Signature')
            exit(1)

        d = pickle.loads(pickle_data)
        return d

    except ValueError:
        print('\nInvalid Value or Data tampered')
        exit(1)


if __name__ == '__main__':
    print(reverse_fun())
