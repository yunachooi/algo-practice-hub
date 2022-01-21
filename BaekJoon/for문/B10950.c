#include <stdio.h>

int main(){
	int t, a, b;
	
	scanf("%d", &t); // 테스트 케이스 개수
	
	for (int i = 0; i < t; i++){
		scanf("%d %d",&a, &b);

		printf("%d\n",a+b);
	}
		
	return 0;
}
