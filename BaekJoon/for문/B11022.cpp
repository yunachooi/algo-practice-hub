#include <stdio.h>

main(){
    int t, a, b, c; // t : °³¼ö 
    
    scanf("%d",&t);
    
    for(int i = 1; i <= t; i++){
        scanf("%d %d",&a, &b);
        c = a + b;
        printf("Case #%d: %d + %d = %d\n", i, a, b, c);
    }
    
    return 0;
}
