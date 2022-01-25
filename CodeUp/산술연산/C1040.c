#include <stdio.h>

int main()
{
    long long int a; // 정수의 범위 -2147483647 ~ +2147483647

    scanf("%lld %lld", &a);

    printf("%lld", -a);

    return 0;
}
