#include <stdio.h>

int main(){
    int w, h, b; // w * h = 해상도
    float sc; // storage capacity
    scanf("%d %d %d", &w, &h, &b);

    sc = w * h * b;
    sc /= (8 * 1024 * 1024);

    printf("%.2f MB", sc);

    return 0;
}