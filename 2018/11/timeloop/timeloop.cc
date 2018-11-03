// make clean; make timeloop; cat samples/a.in | ./timeloop

#include <iostream>

int main()
{
    int N;
    std::cin >> N;
    for (int i = 1; i <= N; i++)
    {
        std::cout << i << " Abracadabra" << std::endl;
    }
}
