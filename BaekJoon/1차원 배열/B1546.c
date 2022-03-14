#include <stdio.h>

int main(){
    double arr[1000] = {};
    double n, max = 0, sum = 0;
    scanf("%lf", &n);

    for(int i = 0; i < n; i++){
        scanf("%lf", &arr[i]);

        if(arr[i] > max)
            max = arr[i];
    }
    for(int i = 0; i < n; i++)
        arr[i] = (arr[i] / max) * 100;
    for(int i = 0; i < n; i++)
        sum += arr[i];
    printf("%lf", sum / n);

    return 0;
}