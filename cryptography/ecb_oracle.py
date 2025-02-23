#!/usr/bin/env python3
import requests
import json
import time
import string
from os import system


def extract_text(text):
    text = json.loads(text)
    text = text["ciphertext"]
    return text

def get_text(text):
    text = requests.get(f"http://aes.cryptohack.org/ecb_oracle/encrypt/{text.encode("utf-8").hex()}/").text
    text = extract_text(text)
    return text

def generate_plaintext(characters_quantity, letter):
    return letter * characters_quantity
 
def bruteforce(plaintext, wordlist, flag):
    ciphertext = get_text(plaintext)
    flag_block = ciphertext[:64]

    for word in wordlist:
        payload = plaintext + flag + word
        ciphered_payload = get_text(payload)
        ciphered_payload_block = ciphered_payload[:64]

        if flag_block == ciphered_payload_block:
            return word


flag = "crypto{"
wordlist = string.printable

while True:
    plaintext = generate_plaintext(31 - len(flag), 'a')
    flag += bruteforce(plaintext, wordlist, flag)
    system("clear")
    print(flag)
    
    if '}' in flag: break 

print("[!] DONE")