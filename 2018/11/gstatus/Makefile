PROG=gstatus
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g -O0
LDFLAGS=-g -O0
OBJS=gstatus.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

gstatus.o:
	$(CC) $(CPPFLAGS) -c gstatus.cc

clean:
	rm -f $(PROG) $(OBJS)
