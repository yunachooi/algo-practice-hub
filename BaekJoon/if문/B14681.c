#include <stdio.h>

int main(){
	int x, y;
	
	scanf("%d %d",&x, &y);
	
	if(x > 0 && y > 0)
		printf("1"); // 1사분면
	else if(x < 0 && y > 0)
		printf("2"); // 2사분면
	else if(x < 0 && y < 0)
		printf("3"); // 3사분면
	else if(x > 0 && y < 0)
		printf("4"); // 4사분면
		
	return 0;
}
