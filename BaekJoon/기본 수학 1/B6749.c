#include <stdio.h>

int main(){
    int y, m; // youngest, middle child
    scanf("%d %d", &y, &m);

    printf("%d", m + (m - y));

    return 0;
}