#include <iostream>
#include <string>
using namespace std;

int main() {
    int a, b, c, val;

    cin >> a >> b >> c;

    if (a >= b) {
        val = (b >= c) ? b : (a >= c) ? c : a;
    }
    else val = (a >= c) ? a : (b >= c) ? c : b;

    cout << val;


}