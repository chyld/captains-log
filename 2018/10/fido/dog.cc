#include <string>
#include "dog.h"

fido::Dog::Dog(std::string name)
{
    this->name = name;
}

std::string fido::Dog::getName() const
{
    return this->name;
}
