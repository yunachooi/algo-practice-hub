#include <stdio.h>

int main() {
    char a[4];
    char anum[4];
    char b[4];
    char bnum[4];
    scanf("%s", a);
    scanf("%s", b);

    for (int i = 0; i < 3; i++)
        anum[2 - i] = a[i];
    for (int i = 0; i < 3; i++)
        bnum[2 - i] = b[i];

    if ((int)anum[0]*100 + (int)anum[1]*10 + (int)anum[2] > ((int)bnum[0]*100 + (int)bnum[1]*10 + (int)bnum[0]))
        for (int i = 0; i <3; i++)
            printf("%c", anum[i]);
    else
        for (int i = 0; i < 3; i++)
            printf("%c", bnum[i]);

    return 0;
}