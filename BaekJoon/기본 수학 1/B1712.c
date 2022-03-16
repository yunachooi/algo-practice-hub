#include <stdio.h>

int main(){
    int a, b, c; // 고정비용, 가변비용, 판매비용
    scanf("%d %d %d", &a, &b, &c);

    if(b >= c) printf("%d", -1);
    else printf("%d", a / (c - b) + 1);

    return 0;
}