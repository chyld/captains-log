PROG=fizzbuzz
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g -O0
LDFLAGS=-g -O0
OBJS=fizzbuzz.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

fizzbuzz.o:
	$(CC) $(CPPFLAGS) -c fizzbuzz.cc

clean:
	rm -f $(PROG) $(OBJS)
