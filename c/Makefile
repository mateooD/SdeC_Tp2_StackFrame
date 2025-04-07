CC=gcc
ASM=nasm
CFLAGS=-Wall -m32 -g
ASFLAGS=-f elf32
LDFLAGS=-m32
OBJ=test_gini.o process_gini_asm.o
EXEC=test_gini

all: $(EXEC)

$(EXEC): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $^

test_gini.o: test_gini.c
	$(CC) $(CFLAGS) -c $< -o $@

process_gini_asm.o: process_gini_asm.s
	$(ASM) $(ASFLAGS) $< -o $@

clean:
	rm -f *.o $(EXEC)
