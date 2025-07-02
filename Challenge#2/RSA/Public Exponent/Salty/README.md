# Salty
We have been given the code used to encrypt and the values of `n`, `e` and `ct`.  
Since `e = 1`, `ct = pt % n`, and `pt < n`, so `pt = ct`.  
Thus all we need to do is
```python
pt = ct
flag = long_to_bytes(pt)
```
## Flag
**crypto{saltstack_fell_for_this!}**
