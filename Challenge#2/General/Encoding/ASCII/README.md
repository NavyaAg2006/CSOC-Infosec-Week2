# ASCII
## Challenge Description
ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.  
Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.
## Walkthrough
We use the attached python script to convert the given integers to `ASCII characters` using the `chr()` function.
```python
ascii_codes = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

result = ""

for i in ascii_codes:
    character = chr(i)
    result += character

print(result)
```
## Flag
**crypto{ASCII_pr1nt4bl3}**
