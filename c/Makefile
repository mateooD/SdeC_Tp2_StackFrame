LIB_NAME = libgini.so
SRC = process_gini.c

# Flags de compilación
CFLAGS = -fPIC -Wall
LDFLAGS = -shared

# Objetos generados
OBJ = $(SRC:.c=.o)

all: $(LIB_NAME)

$(LIB_NAME): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f *.o $(LIB_NAME)