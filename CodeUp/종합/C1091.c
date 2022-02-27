#include <Stdio.h>

int main(){
    long long int a, m, d, n; // 시작 값, 곱할 값, 더할 값, N번째
    long long int i = 1, k;
    scanf("%lld %lld %lld %lld", &a, &m, &d, &n);

    for(int i = 1; i == n; i++)
        k = a * m + d;
    for(k = a; ; i++, k = (k * m) + d)
        if(i == n)
            break;
    printf("%lld", k);

    return 0;
}