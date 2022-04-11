#include <stdio.h>

int main(){
    int a, e; // antenna, eyes
    scanf("%d %d", &a, &e);

    if(a >= 3)
        if(e <= 4) printf("TroyMartian\n");
    if(a <= 6)
        if (e >= 2) printf("VladSaturnian\n");
    if(a <= 2)
        if(e <= 3) printf("GraemeMercurian\n");

    return 0;
}
