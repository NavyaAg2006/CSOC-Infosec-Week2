# Base64
## Challenge Description
Take the below hex string, decode it into bytes and then encode it into Base64.  
`72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf`
> [!TIP]
> In Python, after importing the base64 module with import base64, you can use the base64.b64encode() function. Remember to decode the hex first as the challenge description states.
## Walkthrough
We use the following python script to decrypt
```python
from base64 import b64encode
a = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytes = bytes.fromhex(a)
b64 = b64encode(bytes)
print(b64code)
```
## Flag
**crypto/Base+64+Encoding+is+Web+Safe/**
