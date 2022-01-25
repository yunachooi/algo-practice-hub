#include <stdio.h>

int main()
{
    long long int a, b; // 정수의 범위 -1073741824 ~ 1073741824

    scanf("%lld %lld", &a, &b);

    printf("%lld", a+b);

    return 0;
}
