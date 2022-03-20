#include <stdio.h>
#include <string.h> // strlen()

int main(){
    int len, temp;
    int arr[26] = {};
    char word[101];
    scanf("%s", &word);

    len = strlen(word);

    for(int i = 0; i < 26; i++)
        arr[i] = -1; // -1로 초기화

    for(int i = 0; i < len; i++){
        temp = word[i] - 97; // 아스키코드
        if (arr[temp] != -1) continue;
        else arr[temp] = i;
    }

    for (int i = 0; i < 26; i++)
        printf("%d ", arr[i]);

    return 0;
}