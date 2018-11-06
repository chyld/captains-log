// make clean; make fizzbuzz; cat samples/fizzbuzz-01.in | ./fizzbuzz

#include <iostream>
#include <string>
#include <math.h>

int main()
{
    int X, Y, N;
    std::cin >> X >> Y >> N;

    for (int i = 1; i <= N; i++)
    {
        if ((i % X) + (i % Y) == 0)
            std::cout << "FizzBuzz" << std::endl;
        else if (i % X == 0)
            std::cout << "Fizz" << std::endl;
        else if (i % Y == 0)
            std::cout << "Buzz" << std::endl;
        else
            std::cout << i << std::endl;
    }
}
