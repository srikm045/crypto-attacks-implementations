from pwn import *

HOST = "0.cloud.chals.io"
PORT = 10779

# Uncomment the 'process' line below when you want to test locally, uncomment the 'remote' line below when you want to execute your exploit on the server
# target = process(["python", "./server.py"])
target = remote(HOST, PORT)

def recvuntil(msg):
    resp = target.recvuntil(msg.encode()).decode()
    print(resp)
    return resp

def sendline(msg):
    print(msg)
    target.sendline(msg.encode())

def recvline():
    resp = target.recvline().decode()
    print(resp)
    return resp

def recvall():
    resp = target.recvall().decode()
    print(resp)
    return resp


# ===== YOUR CODE BELOW =====


payload = "00" * 2048  # Sending 2048 null bytes in hex format

# ===== YOUR CODE ABOVE =====


recvuntil("string: ")
sendline(payload)

for level in range(100):
    recvuntil("c1: ")
    c1_hex = recvline().strip()

    recvuntil("c2: ")
    c2_hex = recvline().strip()
    
    recvuntil("c1 or c2: ")

    # ===== YOUR CODE BELOW =====
    c1_bytes = bytes.fromhex(c1_hex)
    c2_bytes = bytes.fromhex(c2_hex)
    
    if b'\x00' in c1_bytes:
        guess = 2 
    else:
        guess = 1 
    # ===== YOUR CODE ABOVE =====

    sendline(f"c{guess}")

recvall()
target.close()