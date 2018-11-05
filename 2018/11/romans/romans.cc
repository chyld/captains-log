// make clean; make romans; cat samples/t0.in | ./romans

#include <iostream>
#include <math.h>

int main()
{
    float X;
    std::cin >> X;
    const float ratio_mile_paces = 1e3 * (5280 / 4854.0);
    const int result = roundf(X * ratio_mile_paces);
    std::cout << result << std::endl;
}
