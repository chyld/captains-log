PROG=faktor
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g -O0
LDFLAGS=-g -O0
OBJS=faktor.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

faktor.o:
	$(CC) $(CPPFLAGS) -c faktor.cc

clean:
	rm -f $(PROG) $(OBJS)
