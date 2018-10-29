#include <iostream>
using namespace std;

int main()
{
    long N;
    cin >> N;
    string names[2] = {"Bob", "Alice"};
    string result = names[N % 2];
    cout << result << endl;
}
