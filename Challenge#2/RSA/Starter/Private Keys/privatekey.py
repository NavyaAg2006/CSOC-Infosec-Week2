def extended_gcd(a, b):
    if b == 0:
        return (1, 0)
    x1, y1 = extended_gcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return (x, y)

def mod_inverse(e, phi):
    x, y = extended_gcd(e, phi)
    return x % phi

e = 65537
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
phi = (p-1)*(q-1)

print(mod_inverse(e, phi))