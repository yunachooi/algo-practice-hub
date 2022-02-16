#include <stdio.h>

int main(){
    int n, i;
    int sum = 0;
    scanf("%d", &n);

    for(i = 0; n > sum; i++)
        sum += i;
    printf("%d", i-1);

    return 0;
}