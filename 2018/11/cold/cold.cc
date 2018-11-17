// make clean; make cold; cat samples/cold-001.in | ./cold

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
    int n;
    std::cin >> n;
    std::vector<int> nums;
    for (int i = 0; i < n; i++)
    {
        int num;
        std::cin >> num;
        nums.push_back(num);
    }

    auto lambda = [&](int total, int x) { return total + (int)(x < 0); };
    int count = std::accumulate(nums.begin(), nums.end(), 0, lambda);
    std::cout << count << std::endl;
}
