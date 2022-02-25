#include <stdio.h>

int main(){
    int a, d, n;
    int i = 1, sum;
    scanf("%d %d %d", &a, &d, &n);

    for(sum = a; ; i++, sum += d)
        if(i == n)
            break;
    printf("%d", sum);

    return 0;
}