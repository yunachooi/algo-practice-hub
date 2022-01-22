#include <stdio.h>

int main(){
    char arr[30];

    scanf("%s", arr);

    for(int i = 0; arr[i] != '\0'; i++) // 널문자가 나올 때까지 출력
        printf("\'%c\'\n", arr[i]);

    return 0;
}