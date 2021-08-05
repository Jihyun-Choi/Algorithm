#include <iostream>
#include <math.h>
#define endl '\n'
using namespace std;

int main() {
	char arr[100];
	int num, sum = 0;

	cin >> num;
	for (int i = 0; i < num; i++) {
		cin >> arr[i];
		sum += arr[i] - 48;
	}
	cout << sum;

	return 0;
}