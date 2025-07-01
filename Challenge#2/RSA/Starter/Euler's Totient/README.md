# Euler's Totient
**Euler’s totient function**, also called **Euler’s phi function**, denoted as `φ(n)` is the number of integers in the range for which the greatest common divisor, `gcd(n,k)` is equal to `1`.  
Also, if two numbers m and n are relatively prime, then,  `φ(m,n) = φ(m).φ(n)`  
When n is prime number, `φ(n)=n-1`.  
  
So in our case  
`φ(N) = φ(p.q) = φ(p).φ(q) = (p-1).(q-1)`
```python
>>> p = 857504083339712752489993810777
>>> q = 1029224947942998075080348647219
>>> (p-1)*(q-1)
```
## Flag
**882564595536224140639625987657529300394956519977044270821168**
