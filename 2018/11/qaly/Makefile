PROG=yoda
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g -O0
LDFLAGS=-g -O0
OBJS=yoda.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

yoda.o:
	$(CC) $(CPPFLAGS) -c yoda.cc

clean:
	rm -f $(PROG) $(OBJS)
