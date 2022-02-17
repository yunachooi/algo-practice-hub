#include <stdio.h>

int main(){
    int n, m;
    scanf("%d %d", &n, &m);

    for(int i=1; i<=n; i++) { // 중첩의 원리
        for (int j = 1; j <= m; j++)
            printf("%d %d\n", i, j);
    }
}