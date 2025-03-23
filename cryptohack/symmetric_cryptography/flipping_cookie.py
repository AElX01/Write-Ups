import json
from requests import get


def get_text(type, url):
    text = json.loads(get(url).text)
    text = text[type]
    
    return text


def get_flag(ciphertext):
    iv = ciphertext[:32]
    cookie = ciphertext[32:]

    print(iv, cookie)

get_flag(get_text("cookie", "https://aes.cryptohack.org/flipping_cookie/get_cookie"))