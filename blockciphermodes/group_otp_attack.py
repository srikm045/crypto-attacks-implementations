import hashlib

def group_sub(m1: bytes, m2: bytes) -> bytes:
    assert len(m1) == len(m2)
    res = b""
    for i in range(len(m1)):
        res += chr((m1[i]-m2[i])%128).encode()
    return res

def generate_key(k1_byte, length):
    key = bytes([k1_byte])
    for x in range(1, length):
        next_byte = hashlib.sha256(key).digest()[0] % 128
        key += bytes([next_byte])
    return key

file_path = r"C:\Users\srika\Downloads\ciphertext.enc"
with open(file_path, 'rb') as f:
   c1= f.read()

length = len(c1)

for k1 in range(1,128):
    key = generate_key(k1, length)
    plaintext = group_sub(c1, key)
    try:
        plaintext_str = plaintext.decode('ascii')
        if all(32 <= c <= 126 for c in plaintext):
            print(f"{plaintext_str}")
    except:
        continue