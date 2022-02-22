#include <iostream> 
#include <algorithm>
using namespace std;

int main() {
	int n, m[10];


	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> m[i];
	}

	for (int i = 0; i < n; i++) {
		int r = 0;
		while (m[i] > 0) {

			if (m[i] % 2) {
				cout << r << " ";
			}
			m[i] /= 2;
			r++;
		}
	}

}