import hashlib
from Crypto.Util.number import bytes_to_long

with open("private.key", "r") as f:
    content = f.read()

lines = content.strip().split('\n')
N = int(lines[0].split('=')[1])
d = int(lines[1].split('=')[1])

m = "crypto{Immut4ble_m3ssag1ng}"
H = bytes_to_long(hashlib.sha256(m.encode()).digest())

print(pow(H,d,N))
