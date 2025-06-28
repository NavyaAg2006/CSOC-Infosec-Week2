# XOR Starter
run the script to get the new string-
```python
string = "label"

flag = ""

for i in string:
    xor = ord(i)^13
    flag += chr(xor)

print(flag)
```
enclose the string `crypto{}`
## Flag
**crypto{aloha}**
# XOR Properties
Since, we know that-  
`if A^B=C`  
`=> A=B^C`
```python
KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY23 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
output = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

print(xor(output,xor(KEY1,KEY23)).decode())
```
## Flag
**crypto{x0r_i5_ass0c1at1v3}**
# Favourite byte
We xor the given message until we get a result that's formatted like the flag, i.e. starts with `crypto{`
```python
from pwn import xor
from itertools import count

cipher = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in count():
	tmp = xor(cipher,i).decode()
	if ("crypto" in tmp):
		print(tmp)
		break
```
## Flag
**crypto{0x10_15_my_f4v0ur173_by7e}**
# You either know, XOR you don't
We know that our cipher when XORed with the unknown key would give then first 7 characters as `crypto{` so we XOR the first 7 characters of the cipher with `crypto{` to get the first 7 characters of the key.
```python
from pwn import xor

cipher = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print(xor(cipher[:7], "crypto{").decode())
```
The following script outputs `myXORke`, so the 8th character is obviously 'y'. We add it and our first guess would be to repeat the phrase until the key is as long as the cipher.
```python
from pwn import xor

cipher = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
partialkey = xor(cipher[:7], "crypto{").decode()
partialkey += "y"
completekey = (partialkey * (len(cipher)//len(partialkey)+1))[:len(cipher)]
print(xor(cipher, completekey))
```
## Flag
**crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}**
