#include <stdio.h>

int main(){
    int n;

    scanf("%d", &n);

    while(n != 0) {
        n -= 1; // n--;, n = n - 1; 와 같다.
        printf("%d\n", n);
    }

    return 0;
}