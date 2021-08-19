#include <iostream>
using namespace std;

int main() {
	int a, num = 0;
	int arr[5] = {};

	cin >> a;
	for (int i = 0; i < 5; i++) {
		cin >> arr[i];
		if (arr[i] == a) num++;
	}

	cout << num;
}