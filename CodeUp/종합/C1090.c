#include <stdio.h>

int main(){
    long long int a, r, n;
    long long int i = 1, k;
    scanf("%lld %lld %lld", &a, &r, &n);

    for(k = a; ; i++, k *= r)
        if(i == n)
            break;
    printf("%lld", k);

    return 0;
}