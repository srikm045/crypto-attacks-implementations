from Crypto.Util.strxor import strxor

file_path2 = r"C:\Users\srika\Downloads\ciphertext2.enc"
file_path1 = r"C:\Users\srika\Downloads\ciphertext1.enc"
with open(file_path1, 'rb') as f:
   c1= f.read()

with open(file_path2, 'rb') as f:
    c2= f.read()

mini_len = min(len(c1),len(c2))
c1=c1[:mini_len]
c2=c2[:mini_len]

x = strxor(c1,c2)
t = (x.hex())

xor_keymsg = "20014d404d0c150e021c2c1d1a4d032d1510113a05111526520c1b050a33150a1e50011b0c1d1a16073610040f55131d0018424a0e"
msg = b"cs409m{one_time_pad_key_reuse_compromises_security}"
fake = b"Cryptanalysis frequently involves statistical attacks" 
xor_bytes = bytes.fromhex(t)
x= strxor(xor_bytes[:len(fake)], fake)
print(x)