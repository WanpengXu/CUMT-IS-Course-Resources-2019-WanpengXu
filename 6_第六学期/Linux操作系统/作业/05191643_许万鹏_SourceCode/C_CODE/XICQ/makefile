all:client server

client:client.o
	gcc client.o -o client.elf -lpthread
server:server.o
	gcc server.o -o server.elf -lpthread
clean:
	rm -f client.elf server.elf *.o