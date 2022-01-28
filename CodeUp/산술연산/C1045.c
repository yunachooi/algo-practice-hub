#include <stdio.h>

int main(){
    int a, b;

    scanf("%d %d", &a, &b);

    printf("%d\n", a + b);
    printf("%d\n", a - b);
    printf("%d\n", a * b);
    printf("%d\n", a / b);
    printf("%d\n", a % b);
    printf("%.2lf", (double)a / b); // 소수점 이하 셋째 자리에서 반올림해 둘째 자리까지 출력

    return 0;
}