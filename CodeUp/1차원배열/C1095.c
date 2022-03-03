#include <stdio.h>

int main(){
    int n, fast;
    int arr[10000] = {};
    scanf("%d", &n);

    for(int k = 1; k <= n; k++)
        scanf("%d", &arr[k]);

    for(int k = n; k >= 1; k--)
        if(arr[k] < fast)
            fast = arr[k];
    printf("%d", fast);

    return 0;
}