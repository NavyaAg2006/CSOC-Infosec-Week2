with open('output.txt', 'r') as f:
    e = f.read()

decoded = ""

for i in range(0, len(e), 4):
    a = int(e[i:i+2], 16)
    b = int(e[i+2:i+4], 16) ^ a
    decoded += chr(a) + chr(b)

with open('recovered_flag.txt', 'w') as f:
    f.write(decoded)
