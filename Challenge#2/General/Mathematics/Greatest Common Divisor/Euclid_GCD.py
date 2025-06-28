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