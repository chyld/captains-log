PROG=cold
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g -O0
LDFLAGS=-g -O0
OBJS=cold.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

cold.o:
	$(CC) $(CPPFLAGS) -c cold.cc

clean:
	rm -f $(PROG) $(OBJS)
