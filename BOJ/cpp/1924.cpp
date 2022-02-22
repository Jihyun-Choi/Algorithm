#include <iostream>
#define endl '\n'
using namespace std;

int main() {
	int x, y;
	int month[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	string day[7] = { "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT" };

	cin >> x >> y;

	for (int i = 0; i < x - 1; i++) {
		y += month[i];
	}
	cout << day[y % 7];

	return 0;
}