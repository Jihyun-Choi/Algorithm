#include <iostream>
#define endl '\n'
using namespace std;

int main() {
	int num, a, b;
	char c;

	cin >> num;
	for (int i = 0; i < num; i++) {
		cin >> a >> c >> b;//왜 이따구로 입력해도 알아서 잘들어가는거지?
		cout << a + b << endl;
	}

	return 0;
}