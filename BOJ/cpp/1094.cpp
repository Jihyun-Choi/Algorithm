#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
int main()
{
	int len = 64, x, num = 1;

	scanf(" %d", &x);

	for (int i = 0; i <= 6; i++) {
		if (x == pow(2, i)) {
			printf("%d", num);
			return 0;
		}
	}

	for (int j = 5; j > 0; j--) {
		if (x > pow(2, j)) {
			x -= pow(2, j);
			num++;
		}
		if (x == pow(2, j))
			break;
	}
	printf("%d", num);

}