#include <iostream> 
using namespace std;

int main(void) { 
	int n;
	long long sum= 1, a;
	int arr[10] = {0, };
	
	for (int i = 0; i < 3; i++) {
		cin >> a;
		sum *= a;
	}
	
	for (int i = 0; sum > 0; i++) {
		n = sum % 10;
		arr[n] = arr[n] + 1;
		sum /= 10;
	}

	for (int i = 0; i < 10; i++) {
		cout << arr[i] << endl;
	}
}
 