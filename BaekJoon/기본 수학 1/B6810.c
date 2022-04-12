#include <stdio.h>

int main(){
    int a, b, c;
    int sum = 91; // first ten digits will always be 9780921418
                // sum = 9 + 7 ∗ 3 + 8 + 0 ∗ 3 + 9 + 2 ∗ 3 + 1 + 4 ∗ 3 + 1 + 8 ∗ 3
    scanf("%d %d %d", &a, &b, &c);

    sum += a + b * 3 + c;
    printf("The 1-3-sum is %d", sum);

    return 0;
}