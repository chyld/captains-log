// make clean; make pokerhand; cat samples/1.in | ./pokerhand

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

bool compare(const std::pair<int, int> &a, const std::pair<int, int> &b)
{
    return a.second < b.second;
}

int main()
{
    std::map<char, int> counter;
    std::string card;
    while (std::cin >> card)
    {
        char rank = card[0];
        int count = counter.count(rank) ? counter[rank] + 1 : 1;
        counter[rank] = count;
    }

    auto max_pair = std::max_element(counter.begin(), counter.end(), compare);
    int largest = max_pair->second;
    std::cout << largest << std::endl;
}
