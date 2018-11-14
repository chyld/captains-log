// make clean; make yoda; cat samples/yoda.1.in | ./yoda

#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <iterator>
#include <vector>
#include <sstream>
#include <math.h>

int main()
{
    int i1, i2;
    std::cin >> i1 >> i2;

    auto s1 = std::to_string(i1);
    auto s2 = std::to_string(i2);

    std::reverse(s1.begin(), s1.end());
    std::reverse(s2.begin(), s2.end());

    int len = std::max(s1.length(), s2.length());
    std::stringstream ss1, ss2;

    for (int i = 0; i < len; i++)
    {
        int a = i < (int)s1.length() ? (int)s1[i] - 48 : 0;
        int b = i < (int)s2.length() ? (int)s2[i] - 48 : 0;

        if (a > b)
            ss1 << a;
        else if (b > a)
            ss2 << b;
        else
        {
            ss1 << a;
            ss2 << b;
        }
    }

    s1 = ss1.str();
    s2 = ss2.str();

    std::reverse(s1.begin(), s1.end());
    std::reverse(s2.begin(), s2.end());

    s1 = s1.length() > 0 ? std::to_string(std::stoi(s1)) : "YODA";
    s2 = s2.length() > 0 ? std::to_string(std::stoi(s2)) : "YODA";

    std::cout << s1 << std::endl
              << s2 << std::endl;
}
