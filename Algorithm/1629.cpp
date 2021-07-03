#include <iostream>
#include <string>
using namespace std;

int main() {
    int a, b, arr[3], x, y, r, l, c = 100;

    cin >> a;
    cin >> b;

    for (int i = 0; i < 3; i++) {
        arr[i] = b / c;
        b -= (arr[i] * c);
        c /= 10;//3,8,5
    }
    x = a * arr[2];
    y = a * arr[1];
    r = a * arr[0];
    l = x + (y * 10) + (r * 100);

    cout << x << endl << y << endl << r << endl << l << endl;
}