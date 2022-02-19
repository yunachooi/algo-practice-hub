#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 1; i <= n; i++){
        if (i % 3 == 0 || i % 6 == 0 || i % 9 == 0) {
            if(i >= 33)
                printf("XX "); // 33이상일 경우 박수 두 번
            else
                printf("X ");
        }
        else
            printf("%d ", i);
    }

    return 0;
}