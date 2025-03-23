#!/usr/bin/env python3
import requests
import json


def extract_text(text, type):
    text = json.loads(text)
    text = text[f"{type}"]
    return text

def get_text(text, action):
    text = requests.get(f"http://aes.cryptohack.org/ecbcbcwtf/{action}/{text if action == "decrypt" else ""}").text
    text = extract_text(text, "ciphertext" if action == "encrypt_flag" else "plaintext")
    return text

def cbc_decryption(ciphertext):
    flag = ''

    for i in range(32, 96, 32):
        plaintext = get_text(ciphertext[i:i + 32], "decrypt")
        initial_xor = int(plaintext, 16) ^ int(ciphertext[i - 32:i], 16)
        flag += hex(initial_xor)[2:]

    flag = bytearray.fromhex(flag[:32]).decode() + bytearray.fromhex(flag[32:64]).decode()
    return flag
    

ciphertext = get_text(None, "encrypt_flag")
print(cbc_decryption(ciphertext))