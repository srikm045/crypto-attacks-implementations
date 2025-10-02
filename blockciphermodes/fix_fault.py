def decrypt_ciphertext(ciphertext, keystream):
    c_num = int.from_bytes(ciphertext, 'big')
    c_digits = []
    while c_num > 0:
        c_num, rem = divmod(c_num, 255)
        c_digits.append(rem)
    c_digits = c_digits[::-1] or [0]
    
    p_digits = []
    for ci, ki in zip(c_digits, keystream):
        pi = (ci - ki + 1) % 255
        p_digits.append(pi)
    
    plain_num = 0
    for d in p_digits:
        plain_num = plain_num * 255 + d
    
    return plain_num.to_bytes((plain_num.bit_length() + 7) // 8, 'big')

text_path = r"C:\Users\srika\Downloads\ciphertexts.enc"
keyfile_path = r"C:\Users\srika\Downloads\keyfile"

with open(text_path, 'rb') as f:
    ciphertext = f.read()

with open(keyfile_path, 'rb') as f:
    keystream = f.read()

plaintext = decrypt_ciphertext(ciphertext, keystream)
print(plaintext)