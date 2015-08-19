package solutions;

// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
// Find the sum of all the primes below two million.

public class prob10 {
	
	public static void main(String[] args) {
		System.out.println(findSum(2000000));
	}
	
	public static long findSum(int n) {
		long sum = 0;
		for(long i = 2; i < n; i++) {
			if(isPrime(i))
				sum += i;
		}
		return sum;
	}
	
	public static boolean isPrime(long n) {
		if(n == 2L) return true;
		for(long i = 2L; i <= (long) Math.floor(Math.sqrt(n)); i++) {
			if(n % i == 0L) return false;
		}
		return true;
	}
}
