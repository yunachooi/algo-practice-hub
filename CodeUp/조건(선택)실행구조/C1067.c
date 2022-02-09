#include <stdio.h>

int main() {
    int a;

    scanf("%d", &a);

    if(a < 0){
        printf("minus\n"); // 음
        if(a % 2 == 0)
            printf("even\n"); // 짝
        else printf("odd\n"); // 홀
    }
    else{
        printf("plus\n"); // 양
        if(a % 2 == 0)
            printf("even\n"); // 짝
        else printf("odd\n"); // 홀
    }

    return 0;
}