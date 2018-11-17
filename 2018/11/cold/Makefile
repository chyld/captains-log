PROG=pokerhand
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g -O0
LDFLAGS=-g -O0
OBJS=pokerhand.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

pokerhand.o:
	$(CC) $(CPPFLAGS) -c pokerhand.cc

clean:
	rm -f $(PROG) $(OBJS)
