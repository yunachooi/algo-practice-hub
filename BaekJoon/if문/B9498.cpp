#include<stdio.h>

main(void) {
	int score; //Á¡¼ö 
	
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

