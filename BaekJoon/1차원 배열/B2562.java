import java.util.Scanner;

public class B2562 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int arr[] = new int[9];
		int max = 0, max_index = 0;
		
		for (int i = 0; i < arr.length; i++)
			arr[i]=sc.nextInt();
		sc.close();
		
		for (int i = 0; i < arr.length; i++) {
			if(arr[i] > max) {
				max = arr[i];
				max_index = i;
			}
		}
		
		System.out.println(max);
		System.out.println(max_index+1);
	}

}
