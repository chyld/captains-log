PROG=carrots
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g -O0
LDFLAGS=-g -O0
OBJS=carrots.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

carrots.o:
	$(CC) $(CPPFLAGS) -c carrots.cc

clean:
	rm -f $(PROG) $(OBJS)
