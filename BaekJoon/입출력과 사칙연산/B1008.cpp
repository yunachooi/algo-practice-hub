#include <stdio.h>

main(){
	int a, b;
	double div;
	
	scanf("%d %d",&a, &b);
	
	div=(double)a/b; //정수 실수 변환 
	printf("%.9f",div);
	
	return 0;
}
