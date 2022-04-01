#include <stdio.h>

int main(){
    int t, n;
    scanf("%d", &t);

    for(int i = 0; i < t; i++){
        scanf("%d", &n);
        printf("Pairs for %d: ", n);

        for(int j = 1; j <= (n / 2); j++){
            if(j != n - j){
                if(j == 1) printf("%d %d", j, n - j);
                else printf(", %d %d", j, n - j);
            }
        }
        printf("\n");
    }

    return 0;
}