#include <stdio.h>

int main(){
    int n, sum = 0;
    scanf("%d", &n);

    for(int i = 1; ; i++){ // for 반목문에서 가운데의 조건이 빠진 경우 무한 반복된다.
        sum += i;
        if(sum >= n)
            break; // 참이면, 가장 가까운 반복 코드블록의 밖으로 빠져나간다.
    } //break; 가 실행되면 반복을 중단하고 여기로 빠져 나온다.
    printf("%d", sum);

    return 0;
}