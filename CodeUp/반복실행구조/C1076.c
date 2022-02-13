#include <stdio.h>

int main(){
    char x, t = 'a';

    scanf("%c", &x);

    do {
        printf("%c ", t);
        t += 1; // t = t + 1 과 같은 의미이다.
    } while(t < x + 1); // 의미 : t의 값이 'z'보다 작은 동안 반복된다.

    return 0;
}