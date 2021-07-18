#include <iostream> 
using namespace std;

int main(void) {
	int s1[4], s2[4], num1 = 0, num2 = 0;

	for (int i = 0; i < 4; i++) {
		cin >> s1[i];
		num1 += s1[i];
	}
	for (int i = 0; i < 4; i++) {
		cin >> s2[i];
		num2 += s2[i];
	}
	cout << (num1 >= num2 ? num1 : num2) << endl;
}