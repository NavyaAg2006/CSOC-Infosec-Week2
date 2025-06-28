# Extended GCD
The extended Euclidean algorithm updates the results of gcd(a, b) using the results calculated by the recursive call gcd(b%a, a).
```python
a = int(input())
b = int(input())

if b<a:
    r1,r2 = a,b
else:
    r1,r2 = b,a
s1,s2 = 1,0
t1,t2 = 0,1

while r2>0:
    q,r = divmod (r1, r2)
    r1, r2 = r2, r

    s1,s2 = s2,s1 - q * s2
    t1, t2 = t2,t1 - q * t2

print(s1)
```
We have to have the smaller one among the intgers we get for 26513 and 32321.
## Flag
**-8404**
