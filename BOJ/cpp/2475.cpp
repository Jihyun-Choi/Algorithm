#include <iostream>
using namespace std;

int main() {
    int a, b, c, d, e, sum = 0;
    cin >> a >> b >> c >> d >> e;
    sum += a * a;
    sum += b * b;
    sum += c * c;
    sum += d * d;
    sum += e * e;

    cout << sum % 10;
}
