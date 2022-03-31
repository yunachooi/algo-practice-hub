#include <stdio.h>

int main(){
    int n;

    for(int i = 1; i >= 0; i++){
        scanf("%d", &n);
        if(n == 0)
            return 0;

        printf("%d. ", i);

        if(n % 2 == 0) { // 짝수
            n = 3 * n / 2 * 3 / 9;
            printf("even %d", n);
        }
        else{ // 홀수
            n = (3 * n + 1) / 2 * 3 / 9;
            printf("odd %d", n);
        }
        printf("\n");
    }
}