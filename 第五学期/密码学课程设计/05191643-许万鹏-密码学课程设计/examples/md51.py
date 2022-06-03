from main import *
import hashlib
import string

chars = string.digits + string.ascii_uppercase
plaintext = "TASC?O3RJMV?WDJKX?ZM"
ciphertext = "e9032???da???08????911513?0???a2"

machine = MD5()
for i in chars:
    for j in chars:
        for k in chars:
            temp_plaintext = f'TASC{i}O3RJMV{j}WDJKX{k}ZM'
            m = hashlib.md5()
            m.update(temp_plaintext.encode())
            temp_ciphertext = m.hexdigest()
            # temp_ciphertext = machine.hash(temp_plaintext)
            if temp_ciphertext.startswith('e9032') and temp_ciphertext.endswith('a2'):
                print(f'plaintext = {temp_plaintext}')
                print(f'ciphertext = {temp_ciphertext}')
                break
