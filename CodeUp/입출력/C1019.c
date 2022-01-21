#include <stdio.h>

int main(){
	int y, m, d;
	
	scanf("%d.%d.%d", &y, &m, &d);
	printf("%04d.%02d.%02d", y, m, d); // 2칸을 사용해 출력하는데, 한 자리 수인 경우 앞에 0을 붙여 출력
	
	return 0;
}
