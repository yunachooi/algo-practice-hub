#include <stdio.h>

int main(){
    int n;

    scanf("%d", &n);

    while(n != 0) {
        printf("%d\n", n);
        n = n - 1; // n--;, n -= 1; 과 같다.
    }

    return 0;
}