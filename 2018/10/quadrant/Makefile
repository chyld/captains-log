PROG=quadrant
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g
LDFLAGS=
OBJS=quadrant.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

quadrant.o:
	$(CC) $(CPPFLAGS) -c quadrant.cc

clean:
	rm -f $(PROG) $(OBJS)
