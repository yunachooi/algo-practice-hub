#include <stdio.h>

int main()
{
    long long int a, b; // 정수의 범위 -2147483648 ~ +2147483648

    scanf("%lld %lld", &a, &b);

    printf("%lld", a+b);

    return 0;
}

