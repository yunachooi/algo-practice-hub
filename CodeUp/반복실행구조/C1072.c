#include <stdio.h>

int main(){
    int n, m;

    scanf("%d", &n);

    reget: //레이블은 콜론( : ) 으로 끝난다.
    scanf("%d", &m);
    printf("%d\n", m);
    n -= 1;
    if(n != 0) goto reget; //reget:으로 이동

    return 0;
}