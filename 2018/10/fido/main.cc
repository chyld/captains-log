#include <iostream>
#include <vector>
#include <string>
#include "dog.h"

int main()
{
    std::string names[] = {"alpha", "beta", "gamma"};
    std::vector<fido::Dog> dogs;

    for (long unsigned int i = 0; i < std::size(names); i++)
    {
        dogs.push_back(fido::Dog(names[i]));
    }

    for (auto d : dogs)
    {
        std::cout << "dog: " << d.getName() << std::endl;
    }
}
