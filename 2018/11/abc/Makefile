PROG=abc
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g -O0
LDFLAGS=-g -O0
OBJS=abc.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

abc.o:
	$(CC) $(CPPFLAGS) -c abc.cc

clean:
	rm -f $(PROG) $(OBJS)
