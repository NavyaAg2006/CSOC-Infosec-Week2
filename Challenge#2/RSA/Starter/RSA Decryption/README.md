# RSA Decryption
We already calculated the `private key`, `d` in the previous challenge so all we need to do calculate  
`c^d modN`  
and that will be our plaintext.

Add the following lines in the code used for the previous challenge
```python
d = mod_inverse(e, phi)
c = 77578995801157823671636298847186723593814843845525223303932
print(pow(c, d, p*q))
```
The complete code is attached.
## Flag
**13371337**
