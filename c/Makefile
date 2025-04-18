LIB_NAME = libgini.so
C_SRC = process_gini.c
ASM_SRC = process_gini_asm.s
OBJ = process_gini.o process_gini_asm.o

# Flags 
CFLAGS = -m32 -g -fPIC -Wall
LDFLAGS = -shared
NASMFLAGS = -f elf32

# Compilador
CC = gcc
ASM = nasm

all: $(LIB_NAME)

$(LIB_NAME): $(OBJ)
	$(CC) -m32 -g $(LDFLAGS) -o $@ $^

# Compilar archivo C
process_gini.o: $(C_SRC) process_gini.h
	$(CC) $(CFLAGS) -c $< -o $@

# Compilar archivo ASM
process_gini_asm.o: $(ASM_SRC)
	$(ASM) $(NASMFLAGS) $< -o $@

clean:
	rm -f *.o $(LIB_NAME)