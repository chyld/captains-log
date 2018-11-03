PROG=timeloop
CC=g++-8
CPPFLAGS=-std=c++17 -Wall -pedantic -g -O0
LDFLAGS=-g -O0
OBJS=timeloop.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

timeloop.o:
	$(CC) $(CPPFLAGS) -c timeloop.cc

clean:
	rm -f $(PROG) $(OBJS)
