#include <iostream>
using namespace std;

int main()
{
    int x, y;
    int d2[2][2] = {{1, 3}, {4, 2}};
    cin >> x >> y;
    cout << d2[x * y < 0][x < 0] << endl;
}
