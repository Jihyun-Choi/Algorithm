#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int arr[10000] = { 0, };
	int a, b;

	cin >> a >> b;
	for (int i = 0; i < a; i++) {
		cin >> arr[i];
	}
	for (int i = 0; i < a; i++) {
		if (arr[i] < b) {
			cout << arr[i] << " ";
		}
	}

}
