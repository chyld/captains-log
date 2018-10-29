PROG=fido
CC=g++
CPPFLAGS=-std=c++17 -Wall -pedantic -g
LDFLAGS=
OBJS=main.o dog.o

$(PROG) : $(OBJS)
	$(CC) $(LDFLAGS) -o $(PROG) $(OBJS)

main.o:
	$(CC) $(CPPFLAGS) -c main.cc

dog.o:
	$(CC) $(CPPFLAGS) -c dog.cc

clean:
	rm -f $(PROG) $(OBJS)
