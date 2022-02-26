#include <stdio.h>

int main(){
    int a, d, n;
    int i = 1, k;
    scanf("%d %d %d", &a, &d, &n);

    for(k = a; ; i++, k += d)
        if(i == n)
            break;
    printf("%d", k);

    return 0;
}