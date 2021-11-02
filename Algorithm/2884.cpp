#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
    int hour, min;

    scanf(" %d %d", &hour, &min);

    if (min >= 45)
        printf("%d %d", hour, min - 45);
    else if (hour == 0)
        printf("%d %d", 24 - 1, 60 + (min - 45));
    else
        printf("%d %d", hour - 1, 60 + (min - 45));
}