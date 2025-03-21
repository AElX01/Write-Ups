PUBLIC_KEY = [65537, 17 * 23]

def cipher(x):
    return pow(x, PUBLIC_KEY[0], PUBLIC_KEY[1])

x = int(input("plaintext: "))
print(cipher(x))