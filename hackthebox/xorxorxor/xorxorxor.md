# BabyEncryption

|platform|challenge type|difficulty
|-|-|-
|HackTheBox|Crypto|Easy

## DESCRIPTION

**Who needs AES when you have XOR?**

## SOLUTION

We are given the files *challenge.py* and *output.txt*. The *challenge.py* file contains the following code:

```python
#!/usr/bin/python3
import os
flag = open('flag.txt', 'r').read().strip().encode()

class XOR:
    def __init__(self):
        self.key = os.urandom(4)
    def encrypt(self, data: bytes) -> bytes:
        xored = b''
        for i in range(len(data)):
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
        return xored
    def decrypt(self, data: bytes) -> bytes:
        return self.encrypt(data)

def main():
    global flag
    crypto = XOR()
    print ('Flag:', crypto.encrypt(flag).hex())

if __name__ == '__main__':
    main()
```

This piece of software is a **file encryption** program that implements the **XOR** cipher to encrypt what's inside the file. The encryption process of **XOR** is as follows:

Given a byte *x* from the plaintext *X* and a byte *k* from the key *K*, the **XOR** ciphers will generate an encrypted byte *y* from the ciphertext *Y* as follows:

*Y = xi ^ ki = yi*

Where *i* is the number of bytes.

```python

```