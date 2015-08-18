package solutions;
// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?

public class prob3 {
	public static void main(String[] args) {
		long n = 600851475143L;
		printLargestPrimeFactor(n);
	}
	
	public static void printLargestPrimeFactor(long n) {
		System.out.println(largestPrimeFactor(n));
	}
	
	public static long largestPrimeFactor(long n) {
		long largestPrimeFactor = 1;
		for(long i = 2; i <= n; i++) {
			if(n % i == 0) {
				n = n / i;
				largestPrimeFactor = i;
				System.out.print("i: " + i + ", ");
				System.out.println("n: " + n);
			}
		}
		return largestPrimeFactor;
	}
}
