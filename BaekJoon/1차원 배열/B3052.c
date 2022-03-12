#include <stdio.h>

int main(){
    int arr[42] = {};
    int count = 0, num;

    for(int i = 0; i < 10; i++){
        scanf("%d", &num);
        arr[num % 42]++; // 42로 나눈 나머지 값을 카운트
    }
    for(int i = 0; i < 42; i++)
        if(arr[i] != 0) count++;
    printf("%d", count);

    return 0;
}