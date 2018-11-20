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
    std::string data;
    std::cin >> data;
    std::string output = data.empty() ? "" : " *";
    std::cout << output << std::endl;
}
