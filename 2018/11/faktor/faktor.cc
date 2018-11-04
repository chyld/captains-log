// clear; make clean; make faktor; cat samples/faktor.dummy.1.in | ./faktor

#include <iostream>
#include <math.h>

int main()
{
    int A, I;
    float discount = 0.99;
    std::cin >> A >> I;
    int result = ceil(A * (I - discount));
    std::cout << result << std::endl;
}
