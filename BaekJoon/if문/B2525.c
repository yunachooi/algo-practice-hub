#include <stdio.h>

int main(){
    int h, m, n;
    int total;
    scanf ("%d %d %d", &h, &m, &n);

    total = m + n;
    m = total % 60;
    h += total / 60;

    if(h > 24)
        h -= 24;
    if(h == 24)
        h = 0;

    printf("%d %d", h, m);

    return 0;
}