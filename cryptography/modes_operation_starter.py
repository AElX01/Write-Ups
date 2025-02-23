#!/usr/bin/env python3
import requests
import json


def extract_text(text, type):
    text = json.loads(text)
    text = text[f"{type}"]
    return text

def get_text(text, action):
    text = requests.get(f"http://aes.cryptohack.org/block_cipher_starter/{action}/{text if action == "decrypt" else ""}").text
    text = extract_text(text, "ciphertext" if action == "encrypt_flag" else "plaintext")
    return text


ciphertext = get_text(None, "encrypt_flag")
print(bytearray.fromhex(get_text(ciphertext, "decrypt")).decode())