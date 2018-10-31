#include <iostream>

int main()
{
    for (int i = 0; i < 100; i++)
    {
        if (i % 15 == 0)
        {
            std::cout << "fizz: " << i << std::endl;
        }
        else if (i % 5 == 0 || i % 3 == 0)
        {
            std::cout << "buzz: " << i << std::endl;
        }
        else
        {
            std::cout << "fizzbuzz: " << i << std::endl;
        }
    }
}
