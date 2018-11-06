// make clean; make zamka; cat samples/zamka.1.in | ./zamka

#include <iostream>
#include <string>
#include <math.h>

int getValue(int, int, int, int);

int main()
{
    int L, D, X;
    std::cin >> L >> D >> X;

    const int N = getValue(L, D + 1, +1, X);
    const int M = getValue(D, L - 1, -1, X);

    std::cout << N << std::endl
              << M << std::endl;
}

int getValue(int start, int stop, int step, int value)
{
    for (int i = start; i != stop; i += step)
    {
        auto s = std::to_string(i);
        int sum = 0;
        for (auto c : s)
        {
            sum += (c - 48);
        }
        if (sum == value)
        {
            return i;
        }
    }

    return 0;
}
