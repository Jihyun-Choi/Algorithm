#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int a, b, c, d, e, ave;
	scanf(" %d", &a);
	scanf(" %d", &b);
	scanf(" %d", &c);
	scanf(" %d", &d);
	scanf(" %d", &e);

	if (a < 40)
		a = 40;
	if (b < 40)
		b = 40;
	if (c < 40)
		c = 40;
	if (d < 40)
		d = 40;
	if (e < 40)
		e = 40;
	ave = (a + b + c + d + e) / 5;
	printf("%d", ave);

}