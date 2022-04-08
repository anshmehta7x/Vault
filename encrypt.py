import math
import random
from cryptography.fernet import Fernet


def encrypt(pword):
    k = Fernet.generate_key()
    fern = Fernet(k)
    encrypted = fern.encrypt(pword.encode())
    return [encrypted,k]


def decrypt(crypt, key):
    f = Fernet(key)
    decrypted = f.decrypt(crypt).decode()
    return decrypted
    