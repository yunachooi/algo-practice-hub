#include <stdio.h>

int main(){
    int c, n;
    scanf("%d", &c);

    for(int i = 0; i < c; i++){
        scanf("%d", &n);
        int sum = 0;
        int arr[1001] = {};
        double avg = .0;
        int count = 0; // 초기화

        for(int j = 0; j < n; j++){
            scanf("%d", &arr[j]);
            sum += arr[j];
        } // for2

        avg = (double)sum / n;

        for(int k = 0; k < n; k++)
            if(avg < arr[k])
                count ++;
        printf("%.3lf%%\n", (double)count * 100 / n);
    } // for1

    return 0;
}