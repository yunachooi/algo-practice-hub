#include <stdio.h>

int main(){
    int h, w, n;
    int l, d, x, y;
    int i, j;
    int arr[1000][1000];

    scanf("%d %d %d", &h, &w, &n);
    for(i = 0; i < n; i++)
    {
        scanf("%d %d %d %d", &l, &d, &x, &y);

        if(d == 0)
            for(j = y; j < y + l; j++)
                arr[x][j] = 1;
        else
            for(j = x; j < x + l; j++)
                arr[j][y] = 1;
    } // for

    for(i = 1; i <= h; i++, puts(""))
        for(j = 1; j <= w; j++)
            printf("%d ", arr[i][j]);

    return 0;
}