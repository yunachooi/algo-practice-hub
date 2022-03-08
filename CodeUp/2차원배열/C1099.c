#include <stdio.h>

int main(){
    int x, y;
    int arr[10][10] = {};

    for(x = 0; x < 10; x++)
        for (y = 0; y < 10; y++)
            scanf("%d", &arr[x][y]);

    x = 1;
    y = 1;

    while(x != 10 && y != 10){
        if (arr[x][y] == 0){
            arr[x][y] = 9;
            y++;
        } //if
        else if (arr[x][y] == 1){
            y--;
            x++;
        } // else if
        else if (arr[x][y] == 2){
            arr[x][y] = 9;
            break;
        } // else if
    } // while

    for(x = 0; x < 10; x++){
        for(y = 0; y < 10; y++)
            printf("%d ", arr[x][y]);
        printf("\n");
    } // for

    return 0;
}