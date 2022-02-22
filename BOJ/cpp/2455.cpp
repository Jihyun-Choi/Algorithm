#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int p1, p2, p3, p4;
	int s1, s2, s3, s4, max = 0, sum = 0;

	scanf(" %d %d", &p1, &s1);
	scanf(" %d %d", &p2, &s2);
	scanf(" %d %d", &p3, &s3);
	scanf(" %d %d", &p4, &s4);

	sum += s1;
	max = max > sum ? max : sum;
	sum = sum - p2 + s2;
	max = max > sum ? max : sum;
	sum = sum - p3 + s3;
	max = max > sum ? max : sum;
	sum = sum - p4 + s4;
	max = max > sum ? max : sum;

	printf("%d", max);
}