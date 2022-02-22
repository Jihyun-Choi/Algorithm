#include <iostream>
using namespace std;
//int num[1000000] = {0};

//int minf(int a, int b) { return a < b ? a : b; }
//int maxf(int a, int b) { return a > b ? a : b; }

int main() {
	int n, max = -1000001, min = 1000001, num;

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> num;
		max = max > num ? max : num;
		min = min < num ? min : num;
	}

	cout << min << " " << max;

	return 0;
}