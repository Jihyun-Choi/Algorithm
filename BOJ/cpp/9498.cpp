#include <iostream>
#include <string>
using namespace std;

int main() {
	int num, g;

	cin >> g;
	num = g / 10;

	switch (num) {
	case 10:
	case 9:
		cout << "A";
		break;
	case 8:
		cout << "B";
		break;
	case 7:
		cout << "C";
		break;
	case 6:
		cout << "D";
		break;
	default:
		cout << "F";
	}
}
