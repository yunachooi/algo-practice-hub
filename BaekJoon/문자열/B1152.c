#include <stdio.h>

int main(){
    int count = 0;
    char arr[1000001] = {};
    gets(arr); // 띄어쓰기 가능

    if(arr[0] == ' ') count -= 1; // 첫문자 공백

    for(int i = 0; i < 1000000; i++){
        if(arr[i] == '\0') break; // 문자열 종료
        if(arr[i + 1] == '\0')
            if(arr[i] == ' ') continue;
        if(arr[i] == ' ') count++;
    }
    printf("%d", count + 1);

    return 0;
}