// make clean; make abc; cat samples/1.in | ./abc

#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <iterator>
#include <math.h>

int main()
{
    int x, y, z;
    std::string s;
    std::cin >> x >> y >> z >> s;
    int size = 3;
    int nums[] = {x, y, z};

    std::sort(nums, nums + size);
    std::map<char, int> lookup;

    for (int i = 0; i < size; i++)
    {
        auto n = nums[i];
        auto c = char(65 + i);
        lookup.insert(std::pair<char, int>(c, n));
    }

    for (char c : s)
    {
        std::cout << lookup[c] << " ";
    }

    std::cout << std::endl;
}
