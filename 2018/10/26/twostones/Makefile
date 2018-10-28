PROG=twostones
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g
LDFLAGS=
OBJS=twostones.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

twostones.o:
	$(CC) $(CPPFLAGS) -c twostones.cpp

clean:
	rm -f $(PROG) $(OBJS)
