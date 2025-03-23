# BabyEncryption

|platform|challenge type|difficulty
|-|-|-
|HackTheBox|Crypto|Very Easy

### DESCRIPTION

**You are after an organised crime group which is responsible for the illegal weapon market in your country. As a secret agent, you have infiltrated the group enough to be included in meetings with clients. During the last negotiation, you found one of the confidential messages for the customer. It contains crucial information about the delivery. Do you think you can decrypt it?**

### SOLUTION

The challenge is not as fancy as is sounds in the description, as it only requires some modular arithmetic knowledge.  
Once files have been downloaded, we get the secret message **msg.enc** and the software that has been used to generate it:

```python
import string
from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

ct = encryption(MSG)
f = open('./msg.enc','w')
f.write(ct.hex())
f.close()
```

By analizing the code we can infer this is **not** a cryptosystem given the lack of encryption and decryption keys, but rather an **encoding** algorithm producing an output that is easily reversible. The secret message is generated with the following equation *y = (123 x char + 18) mod 256*, we can easily solve the equation for *char* to get the secret message:

*y = (123 x char + 18) mod 256*

*y - 18 = 123 x char mod 256*

*123 x char = (y - 18) mod 256*

Take into account division is not directly applicable in modular arithmetic, the we can take *123* out of *char* is by finding the inverse modulo of *123*, similar to what is done in **RSA** to find the private exponent:

*123 x i = 1 mod 256*

*i = 123^-1 mod 256*

Therefore, instead of passing *123* at the other side, we pass its inverse modulo successfully solving the equation:

*char = (y - 18) x i mod 256*

The following python script can be used to solve the challenge:

```python
from sympy import mod_inverse

def decryption(msg):
    msg = bytes.fromhex(msg)
    x = []
    i = pow(123, -1, 256)

    for y in msg:
        x.append(chr((y - 18) * i % 256))
    
    return ''.join(x)

x = decryption("6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921")
f = open('./msg.enc','w')
f.write(x)
f.close()
```

It transforms the encoded message to bytes, then finds the modular inverse of *123* and applies the equation we did above to get each character from the message:

```bash
Th3 nucl34r w1ll 4rr1v3 0n fr1d4y.
HTB{...}
```

