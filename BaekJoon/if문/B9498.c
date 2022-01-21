#include<stdio.h>

int main(void) {
	int score; //점수
	
	scanf("%d", &score);
	
	if (score >= 90 && score <= 100)
		printf("A");
	else if (score < 90 && score >= 80)
		printf("B");
	else if (score < 80 && score >= 70)
		printf("C");
	else if (score < 70 && score >= 60)
		printf("D");
	else
		printf("F");
	
	return 0;
}

