#include <iostream>
#define endl '\n'
using namespace std;

int main() {
	int num, a, b;

	cin >> num;
	for (int i = 0; i < num; i++) {
		cin >> a >> b;
		printf("Case #%d: %d + %d = %d\n", i + 1, a, b, a + b);
	}

	return 0;
}