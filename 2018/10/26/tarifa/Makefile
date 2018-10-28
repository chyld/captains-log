PROG=tarifa
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g
LDFLAGS=
OBJS=tarifa.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

tarifa.o:
	$(CC) $(CPPFLAGS) -c tarifa.cpp

clean:
	rm -f $(PROG) $(OBJS)
