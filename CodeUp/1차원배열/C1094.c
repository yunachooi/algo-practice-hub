#include <stdio.h>

int main(){
    int n;
    int arr[10000] = {};
    scanf("%d", &n);

    for(int k = 1; k <= n; k++)
        scanf("%d", &arr[k]);

    for(int k = n; k >= 1; k--)
        printf("%d ", arr[k]);

    return 0;
}