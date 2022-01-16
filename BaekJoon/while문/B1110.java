import java.util.Scanner;

public class B1110 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		sc.close();
		
		int cnt = 0; //cycle
		int newn = n; 
        
		while (true) {
			n = ((n % 10) * 10) + (((n / 10) + (n % 10)) % 10);
			cnt ++;
 
			if (newn == n)
				break;
		}
		
		System.out.println(cnt);
	}

}
