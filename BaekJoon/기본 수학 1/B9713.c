#include <stdio.h>

int main(){
    int t, n;
    scanf("%d", &t);

    for(int i = 0; i < t; i++){
        int sum = 0;
        scanf("%d", &n);

        if(n % 2 == 1){
            for(int j = 1; j <= n; j += 2)
                sum += j;
            printf("%d\n", sum);
        }
    }

    return 0;
}