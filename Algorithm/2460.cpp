#include <iostream>
using namespace std;

int main() {
	int sum = 0, max = 0, a, b;

	for (int i = 0; i < 10; i++) {
		cin >> a >> b;
		sum -= a;
		max = max > sum ? max : sum;
		sum += b;
		max = max > sum ? max : sum;
	}
	cout << max;
}