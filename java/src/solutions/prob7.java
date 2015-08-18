package solutions;

// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
// What is the 10001st prime number?

public class prob7 {
	public static void main(String[] args) {
		System.out.println(findPrime(10001L));
	}
	
	public static long findPrime(long n) {
		long primeCnt = 0L;
		long i = 1L;
		while(primeCnt < n) {
			i++;
			if(isPrime(i)) {
				primeCnt++;
			}
		}
		return i;
	}
	
	public static boolean isPrime(long n) {
		if(n == 2L) return true;
		for(long i = 2L; i <= (long) Math.floor(Math.sqrt(n)); i++) {
			if(n % i == 0L) return false;
		}
		return true;
	}
}
