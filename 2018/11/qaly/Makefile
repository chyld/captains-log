PROG=qaly
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g -O0
LDFLAGS=-g -O0
OBJS=qaly.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

qaly.o:
	$(CC) $(CPPFLAGS) -c qaly.cc

clean:
	rm -f $(PROG) $(OBJS)
