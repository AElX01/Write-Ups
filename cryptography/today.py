import math

base = 106
prime = 24691
alice_key = 12375

for i in range(2, prime - 2):
    if alice_key == (106 ** i) % prime:
        print(i)