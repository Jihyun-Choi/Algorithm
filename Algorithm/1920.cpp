#include <iostream>
#include <string>
using namespace std;

int arr[100000] = { 0 };
int main() {
	int num, x;

	cin >> num;
	for (int i = 0; i < num; i++) {
		cin >> x;
		arr[x] = 1;
	}

	cin >> num;
	for (int i = 0; i < num; i++) {
		cin >> x;
		if (arr[x]) cout << "1" << endl;
		else cout << "0" << endl;
	}
}