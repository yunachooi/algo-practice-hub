#include <stdio.h>

int main(){
	int a, b;
	double div;
	
	scanf("%d %d",&a, &b);
	
	div = (double)a / b; //정수를 실수로 변환
	printf("%.9f",div);
	
	return 0;
}
