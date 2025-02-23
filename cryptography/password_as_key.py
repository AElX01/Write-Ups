#!/usr/bin/env python3

from Crypto.Cipher import AES
import requests
import hashlib
import json


def get_flag():
    encrypted_flag = requests.get("http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/")
    encrypted_flag = json.loads(encrypted_flag.text)
    encrypted_flag = encrypted_flag["ciphertext"]
    return encrypted_flag

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    try:
        return {"plaintext": bytearray.fromhex(decrypted.hex()).decode()}
    except Exception as e:
        return "NONE"

def bruteforce_hash(encrypted_flag):
    with open('/opt/wordlists/words') as f:
        words = [w.strip() for w in f.readlines()]
    print(f"bruteforcing...")

    for word in words:
        key = hashlib.md5(word.encode()).hexdigest()
        flag = decrypt(encrypted_flag, key)
        
        if flag != "NONE": break

    return flag


encrypted_flag = get_flag()
flag = bruteforce_hash(encrypted_flag)

print(flag)