#include <stdio.h>

int main(){
    char str[1000001];
    int arr[26] = {};
    int max = 0, cheak = 0; // cheak = 많이 사용된 알파벳이 여러개 존재하는 경우
    scanf("%s", &str);

    for(int i = 0; str[i] != '\0'; i++){
        if (str[i] >= 'a' && str[i] <= 'z')
            str[i] -= 'a' - 'A';
        arr[str[i] - 'A']++;
    }

    for(int i = 1; i < 26; i++){
        if (arr[max] < arr[i])
            max = i;
    }

    for(int i = max + 1; i < 26; i++){
        if (arr[max] == arr[i]){
            cheak = 1;
            break;
        }
    }

    if (cheak) printf("?");
    else printf("%c", 'A' + max);

    return 0;
}