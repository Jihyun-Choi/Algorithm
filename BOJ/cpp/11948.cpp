#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int arr[6] = { 0, };
	int num = 0;

	for (int i = 0; i < 6; i++) {
		cin >> arr[i];
	}

	num += (arr[4] > arr[5] ? arr[4] : arr[5]);
	sort(arr, arr + 4);

	num += (arr[3] + arr[1] + arr[2]);

	cout << num;
}