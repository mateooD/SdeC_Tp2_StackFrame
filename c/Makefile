CC = gcc
CFLAGS = -Wall -fPIC -O2
LDFLAGS = -shared

all: libgini.so

libgini.so: process_gini.o
	$(CC) $(LDFLAGS) -o $@ $^

process_gini.o: process_gini.c process_gini.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f *.o *.so
