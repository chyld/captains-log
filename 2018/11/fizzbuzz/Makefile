PROG=zamka
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g -O0
LDFLAGS=-g -O0
OBJS=zamka.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

zamka.o:
	$(CC) $(CPPFLAGS) -c zamka.cc

clean:
	rm -f $(PROG) $(OBJS)
