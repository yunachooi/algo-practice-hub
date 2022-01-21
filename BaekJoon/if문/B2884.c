#include <stdio.h>

int main(){
	int h,m; // h시 m분
	
	scanf("%d %d", &h, &m);
	
	if (m < 45) { // 45분 전에 알람
		h -= 1;
		m = (m + 60) - 45;
	}
	else m -= 45;
	
	if (h < 0) h += 24;
	printf("%d %d", h, m);
	
	return 0;
}
