// make clean; make gstatus

#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <map>
#include <iterator>
#include <vector>
#include <sstream>
#include <numeric>
#include <utility>
#include <math.h>

int main()
{
    std::string line;
    while (!std::getline(std::cin, line).eof())
    {
        if (line[0] == '*')
        {
            std::cout << line.substr(2) << std::endl;
            break;
        }
    }
}
