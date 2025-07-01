# Structure of AES
We have a function that Converts a 16-byte array into a 4x4 matrix.
```python
def bytes2matrix(text):
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]
```
To reverse this we simply need to flatten the 4x4 matrix into a single list and then convert the flattened list of integers into a bytes object.
```python
def matrix2bytes(matrix):
    return bytes(sum(matrix, []))
```
## Flag
**crypto{inmatrix}**
