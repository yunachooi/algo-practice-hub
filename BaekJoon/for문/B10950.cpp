#include <stdio.h>

main(){
	int t, a, b;
	
	scanf("%d", &t); //°³¼ö 
	
	for (int i = 0; i < t; i++){
		scanf("%d %d",&a, &b);
		printf("%d\n",a+b);
	}
		
	return 0;
}
