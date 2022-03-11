#include <stdio.h>

int main(){
    int a, b, c;
    int mul, num;
    int arr[100]={};
    scanf("%d\n%d\n%d", &a, &b, &c);

    mul  = a * b * c;

    // 방법 1
    /* for(int i = 0; mul > 0; i++){
            num = mul % 10;
            mul /= 10;
            arr[num] ++;
        } */

    // 방법 2
    while (mul > 0) {
        num = mul % 10;
        mul /= 10;
        arr[num] ++;
    }

    for (int i = 0; i < 10; i++)
        printf("%d\n", arr[i]);

    return 0;
}