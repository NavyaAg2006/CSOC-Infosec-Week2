# Challenge_2
## Walkthrough
The contents of file `source.enc` are `base64` encoded. We download the file and use command
```bash
cat source.enc | base64 -d
```
We the the script for how our flag was encoded
```python
with open('flag.txt', 'r') as f :
    flag = f.read()

s = ''.join(format(ord(i), '02x') for i in flag)
e = ""

for i in range(0,len(s),4) :
    e += format(int(s[i:i+2],16), '02x')+format(int(s[i:i+2],16)^int(s[i+2:i+4],16), '02x')

with open('output.txt', 'w') as f :
    f.write(e)
```
In order to decode the flag from the output given to us we write the reverse script.
```python
#decoder
with open('output.txt', 'r') as f:
    e = f.read()

decoded = ""

for i in range(0, len(e), 4):
    a = int(e[i:i+2], 16)
    b = int(e[i+2:i+4], 16) ^ a
    decoded += chr(a) + chr(b)

with open('recovered_flag.txt', 'w') as f:
    f.write(decoded)
```
Using this we obtain our flag.
## Flag
**CSOC25{y0u_kn0w_X0r_4nd_b45364}**
