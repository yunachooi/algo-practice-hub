#include <stdio.h>

int main() {
    int a;

    scanf("%d", &a);

    if(a < 0){
        printf("%s\n", "minus"); // 음
        if(a % 2 == 0)
            printf("%s\n", "even"); // 짝
        else printf("%s\n", "odd"); // 홀
    }
    else{
        printf("%s\n", "plus"); // 양
        if(a % 2 == 0)
            printf("%s\n", "even"); // 짝
        else printf("%s\n", "odd"); // 홀
    }

    return 0;
}