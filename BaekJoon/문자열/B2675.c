#include <stdio.h>
#include <string.h>

int main(){
    int t, r, len; // 테스트 개수, 반복
    char s[21];
    scanf("%d", &t);

    for(int i = 0; i < t; i++){
        scanf("%d", &r);
        scanf("%s", &s);

        len = strlen(s);

        for(int j = 0; j < len; j++)
            for(int k = 0; k < r; k++)
                printf("%c", s[j]);
        printf("\n");
    }

    return 0;
}