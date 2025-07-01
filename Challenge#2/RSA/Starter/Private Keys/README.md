# Private Keys
Private key is the multiplicative inverse  
`d = e^(−1) modϕ(n)`  
To do this we use the function
```python
def extended_gcd(a, b):
    if b == 0:
        return (1, 0)
    x1, y1 = extended_gcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return (x, y)

def mod_inverse(e, phi):
    x, y = extended_gcd(e, phi)
    return x % phi
```
The modular inverse is our private key.
## Flag
**121832886702415731577073962957377780195510499965398469843281**
