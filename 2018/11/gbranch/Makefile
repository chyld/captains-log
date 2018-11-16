PROG=gbranch
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g -O0
LDFLAGS=-g -O0
OBJS=gbranch.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

gbranch.o:
	$(CC) $(CPPFLAGS) -c gbranch.cc

clean:
	rm -f $(PROG) $(OBJS)
