from base64 import urlsafe_b64encode
from os import urandom
from cryptography.fernet import Fernet


def generate_key(power=16) -> str:
    decoded_key = ''
    for _ in range(power):
        _key = urlsafe_b64encode(urandom(32)).decode()
        decoded_key += _key

    return decoded_key


def encryept(key_string: str, data: str) -> str:
    obj = Fernet(key_string.encode())
    encryepted_bytes = obj.encrypt(data.encode())
    return encryepted_bytes.decode()


def decryept(key_string: str, data: str) -> str:
    obj = Fernet(key_string.encode())
    decryepted_bytes = obj.decrypt(data.encode())
    return decryepted_bytes.decode()
