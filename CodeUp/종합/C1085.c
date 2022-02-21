#include <stdio.h>

int main(){
    long long int h, b, c, s;
    double sc; // storage capacity
    scanf("%lld %lld %lld %lld", &h, &b, &c, &s);

    sc = h * b * c * s;
    sc /= (8 * 1024 * 1024); // bit > byte > kbyte > mbyte

    printf("%.1f MB", sc);

    return 0;
}