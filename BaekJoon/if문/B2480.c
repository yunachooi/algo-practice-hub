#include <stdio.h>

int main(){
    int x, y, z;
    scanf("%d %d %d", &x, &y, &z);

    if(x == y && y == z)
        printf("%d", 10000 + x * 1000); // 같은 눈 x, y, z
    else if(x == y)
        printf("%d", 1000 + x * 100); // 같은 눈 x, y
    else if(x == z)
        printf("%d", 1000 + x * 100); // 같은 눈 x, z
    else if(y == z)
        printf("%d", 1000 + y * 100); // 같은 눈 y, z
    else{
        if(x > y){
            if(x > z) printf("%d", x * 100); // 가장 큰 눈 x
            else printf("%d", z * 100); // 가장 큰 눈 z
        }
        else{
            if(y > z) printf("%d", y * 100); // 가장 큰 눈 y
            else printf("%d", z * 100); // 가장 큰 눈 z
        }
    }

    return 0;
}