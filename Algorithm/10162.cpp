#include <iostream>
#include <string>
using namespace std;

int main() {
	int a = 0, b = 0, c = 0, n;

	cin >> n;

	while (n >= 300) {//= 안붙여서 틀렸음,,,
		n -= 300;
		a++;
	}
	while (n >= 60) {
		n -= 60;
		b++;
	}
	while (n >= 10) {
		n -= 10;
		c++;
	}
	if (n) {
		cout << "-1";
		return 0;
	}
	cout << a << " " << b << " " << c << endl;


}