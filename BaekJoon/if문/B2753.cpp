#include <stdio.h>

main(){
	int year; //³âµµ 
	
	scanf("%d",&year);
	
	if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
		printf("1"); //À±³â
	else printf("0");
	
	return 0;
}
