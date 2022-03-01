#include <stdio.h>

int main(){
    int n, t;
    int a[24] = {}; // 초기화
    scanf("%d", &n);

    for(int i = 1; i <= n; i++){
        scanf("%d", &t);
        a[t] += 1; // 들어있던 값에 1만큼 더해 다시 저장
    }
    for(int j = 1; j <= 23; j++)
        printf("%d ", a[j]); // 1 ~ 23번 배열에 저장되어있는 값 출력하기

    return 0;
}