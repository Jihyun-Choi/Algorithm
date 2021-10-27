#include <iostream>
using namespace std;

int main() {
	int num, n, sum = 0, re = 0;

	cin >> num;

	for (int i = 0; i < num; i++) {
		cin >> n;

		if (n) {
			re++;
			sum += re;
		}
		else re = 0;
	}

	cout << sum;
}