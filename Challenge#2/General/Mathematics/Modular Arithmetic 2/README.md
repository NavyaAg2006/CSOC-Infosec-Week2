# Modular Arithmetic 2
This problem right here deals with **Fermat’s Little Theorem**
### a^(p-1) ≡ 1 (mod p)
> [!NOTE]
>  a raise to p-1 modulo p is equal to 1, on the condition that p is prime and a is any integer not divisible by p.

In this challenge, `65536` is `65537 - 1` which `65537` is a prime. So you can check if `273246787654` and `65536` is coprime or not. If it is, print `1`.
```python
import math
a = 273246787654
p = 65537

if(math.gcd(a, p) == 1):
    print(1)
```
## Flag
**1**
