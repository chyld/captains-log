// make clean; make qaly; cat samples/1.in | ./qaly

#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <map>
#include <iterator>
#include <vector>
#include <sstream>
#include <numeric>
#include <math.h>

int main()
{
    int N;
    std::cin >> N;
    std::vector<float> products;

    for (int i = 0; i < N; i++)
    {
        float q, y, product;
        std::cin >> q >> y;
        product = q * y;
        products.push_back(product);
    }

    auto lambda = [&](float a, float b) { return a + b; };
    auto qaly = std::accumulate(products.begin(), products.end(), 0.0, lambda);
    std::cout << std::setprecision(3) << std::fixed;
    std::cout << qaly << std::endl;
}
