# Greatest Common Divisor
According to `Euclid's Algorithm` the GCD remains the same when we subtract the smaller no. from the the greater. So on repeatedly subtracting once the numbers become same we get the GCD.
```python
def euclid(a,b):
    if (a==b):
        return a
    else:
        if (b>a):
            return euclid(b-a,a)
        else:
            return euclid(a-b,b)

x = int(input("Enter first no.: "))
y = int(input("Enter second no.: "))
print(euclid(x,y))
```
We have to find the GCD of 66528 and 52920.
## Flag
**1512**
