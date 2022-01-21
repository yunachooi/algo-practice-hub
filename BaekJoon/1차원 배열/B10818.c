#include <stdio.h>

main(){
    int n, min, max;
	scanf("%d", &n);
	
    int arr[n];
    for(int i = 0 ; i < n ; i++)
        scanf("%d", &arr[i]);
    
    min = max = arr[0]; // min, max 초기값 설정
 
    for(int i = 1 ; i < n ; i++){
        if(max < arr[i])
            max = arr[i];
			
		if(min > arr[i])
            min = arr[i];  
    }
    
    printf("%d %d", min, max);
    
    return 0;
}
