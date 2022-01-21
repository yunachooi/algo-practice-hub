#include <stdio.h>

int main(){
    int t, a, b, c;
    
    scanf("%d",&t); // 테스트 케이스 개수
    
    for(int i = 1; i <= t; i++){
        scanf("%d %d",&a, &b);

        c = a + b;

        printf("Case #%d: %d + %d = %d\n", i, a, b, c);
    }
    
    return 0;
}
