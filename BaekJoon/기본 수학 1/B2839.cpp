#include <stdio.h>

main()
{
    int n, a;

    scanf("%d",&n);

    a = n % 5;

    if (n == 4 || n == 7)
        printf("-1");
    else{
        if (a == 0)
            printf("%d",n / 5);
        else if (a==1 || a==3)
            printf("%d",(n / 5) + 1);
        else
            printf("%d",(n / 5) + 2);
    }

    return 0;
} 

