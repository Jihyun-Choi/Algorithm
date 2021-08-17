#include <iostream>
using namespace std;

int main() {
    int a, b, c, d, x, y, min;

    cin >> a >> b;
    cin >> c >> d;

    x = a + d;
    y = b + c;
    min = x < y ? x : y;
    cout << min;

}
