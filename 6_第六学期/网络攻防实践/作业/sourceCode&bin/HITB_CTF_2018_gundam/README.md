### HITB-XCTF -PWN pt.487

## Review
* I alway prefer ubuntu 16.04 version when i solve the ctf.
* I could not find the vulnerability in this binary.
* Finally, I found that the version of libc is 2.26.(CMD => `strings libc.so.6 | grep "libc-"`)
* In server, this binary is running on ubuntu 17.10.
* Then, I count`t execute this binary with server libc.
* ubuntu 17.04 => libc-2.25, ubuntu 17.10 => libc-2.26
* Because, I was install ubuntu 17.10....

## Vulnerability
* libc-2.26 is a way to info leak, and the structure of the heap is very different.

* The biggest feature of libc-2.26 is that it is double-free regardless of its size, Because we initially use a heap space called tcache, not an unsorted bin, fastbin, and so on.

## Info Leak

* The heap leak and libc leak methods are different from previous versions of libc.
* libc-2.26 use tcache. tcache is used like fastbin. Therefore Heap leak is easy..but libc leak is difficult

## Libc Leak

* tcache can have a maximun of 7 chunks. Therefore by freeing more than 7 chunks, the remaining chunks will be treated as usual.
* If chunk of 0x100 size is freed after 7-tcache(all) has been freed, then the freed chunk goes into unsorted bin.
* Therefore, We can libc leak.

## Exploit 

* libc-2.26 version can be double-free regardless of size.
* So you can do exploit using **__free_hook()** address , **system()** address 
* It is recommended that you are debugging yourself for details.
