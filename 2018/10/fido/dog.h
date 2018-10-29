#ifndef FIDO_DOG_H
#define FIDO_DOG_H

#include <string>

namespace fido
{
class Dog
{
  private:
    std::string name;

  public:
    Dog(std::string name);
    std::string getName() const;
};
} // namespace fido

#endif
