#include <iostream>

int main()
{
    long counter = 0, X = 0, N = 0, sum = 0;
    for (std::string line; std::getline(std::cin, line); counter++)
    {
        if (counter == 0)
        {
            X = std::stol(line);
        }
        else if (counter == 1)
        {
            N = std::stol(line);
        }
        else
        {
            sum += std::stol(line);
        }
    }

    long result = X + ((X * N) - sum);
    std::cout << result << std::endl;
    return 0;
}
