LIB_NAME = libgini.so
C_SRC = process_gini.c
ASM_SRC = process_gini_asm32.s
OBJ = process_gini.o process_gini_asm.o

# Flags 
CFLAGS = -m32 -fPIC -Wall
LDFLAGS = -shared
NASMFLAGS = -f elf32

# Compilador
CC = gcc
ASM = nasm

all: $(LIB_NAME)

$(LIB_NAME): $(OBJ)
	$(CC) -m32 $(LDFLAGS) -o $@ $^

# Compilar archivo C
process_gini.o: $(C_SRC) process_gini.h
	$(CC) $(CFLAGS) -c $< -o $@

# Compilar archivo ASM
process_gini_asm.o: $(ASM_SRC)
	$(ASM) $(NASMFLAGS) $< -o $@

clean:
	rm -f *.o $(LIB_NAME)




# LIB_NAME = libgini.so
# C_SRC = process_gini.c
# ASM_SRC = process_gini_asm64.s
# OBJ = process_gini.o process_gini_asm.o

# # Flags 
# CFLAGS = -m64 -fPIC -Wall
# LDFLAGS = -shared
# NASMFLAGS = -f elf64

# # Compilador
# CC = gcc
# ASM = nasm

# all: $(LIB_NAME)

# $(LIB_NAME): $(OBJ)
# 	$(CC) -m64 $(LDFLAGS) -o $@ $^

# # Compilar archivo C
# process_gini.o: $(C_SRC) process_gini.h
# 	$(CC) $(CFLAGS) -c $< -o $@

# # Compilar archivo ASM
# process_gini_asm.o: $(ASM_SRC)
# 	$(ASM) $(NASMFLAGS) $< -o $@

# clean:
# 	rm -f *.o $(LIB_NAME)


# CC=gcc
# ASM=nasm
# CFLAGS=-Wall -m32 -g
# ASFLAGS=-f elf32
# LDFLAGS=-m32
# OBJ=test.o process_gini_asm32.o
# EXEC=test

# all: $(EXEC)

# $(EXEC): $(OBJ)
# 	$(CC) $(LDFLAGS) -o $@ $^

# test.o: test.c
# 	$(CC) $(CFLAGS) -c $< -o $@

# process_gini_asm32.o: process_gini_asm32.s
# 	$(ASM) $(ASFLAGS) $< -o $@

# clean:
# 	rm -f *.o $(EXEC)