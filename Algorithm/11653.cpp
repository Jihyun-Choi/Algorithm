#include <iostream>
using namespace std;

int main() {
	int num;

	cin >> num;
	for (int i = 2; i <= num;) {
		if (!(num % i)) {
			cout << i << endl;
			num /= i;
		}
		if (num % i) i++;
	}
}