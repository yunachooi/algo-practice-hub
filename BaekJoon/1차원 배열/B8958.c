#include <stdio.h>
#include <string.h> // strlen()

int main(){
    int n, combo, score;
    char ox[100];
    scanf("%d", &n);

    for(int i = 0; i < n; i++){
        score = combo = 0;
        scanf("%s", &ox);

        for(int j = 0; j < strlen(ox); j++){
            if(ox[j] == 'O'){
                score += 1 + combo;
                combo++;
            }
            else // 'X'
                combo = 0; // score는 유지.
        }

        printf("%d\n", score);
    }

    return 0;
}