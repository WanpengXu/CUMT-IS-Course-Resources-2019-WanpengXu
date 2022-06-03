# Configurations
PROJECT	=	run
CC	=	g++
FLAGS	=	-g
WFLAGS	=	-Wall -Wextra
OPTIMIZATION =	-O2
OBJ	=	RC6.o
HEADER	=	RC6.hpp
SRC	=	RC6.cpp
DRIVER	=	RC6_main.cpp

# Build
all:		$(PROJECT)

$(PROJECT):	$(OBJ) $(DRIVER)
		$(CC) $(FLAGS) $^ -o $@

warning-enbl:	$(OBJ) $(DRIVER)
		$(CC) $(FLAGS) $(WFLAGS) $^ -o $@

optimizations:	$(OBJ) $(DRIVER)
		$(CC) $(FLAGS) $(OPTIMIZATION) $^ -o $@

# Build object files
%.o:		%.c
		$(CC) $(FLAGS) -c $^

# Clean up
clean:
		rm -f *.o *~ *.a $(PROJECT) warning-enbl optimizations

# tar relevent files
tar:		clean
		cd ..; \
		tar -cvf RC6_enc.tar RC6

rm_tar:
		cd ..; \
		rm RC6_enc.tar