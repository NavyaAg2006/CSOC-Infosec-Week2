ascii_codes = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

result = ""

for i in ascii_codes:
    character = chr(i)
    result += character

print(result)