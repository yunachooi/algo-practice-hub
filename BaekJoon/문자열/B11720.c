#include <stdio.h>

int main(){
	int n, sum = 0;
	char arr[101];
	scanf("%d", &n);
	scanf("%s", &arr);
	
	for(int i = 0; i < n; i++)
		sum += arr[i] - 48; // 48 = '0'
	printf("%d", sum);
	
	return 0;
}
