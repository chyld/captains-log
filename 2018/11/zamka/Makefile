PROG=romans
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g -O0
LDFLAGS=-g -O0
OBJS=romans.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

romans.o:
	$(CC) $(CPPFLAGS) -c romans.cc

clean:
	rm -f $(PROG) $(OBJS)
