package solutions;

// It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
// Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
// Which starting number, under one million, produces the longest chain?

public class prob14 {
	public static void main(String[] args) {
		System.out.println(longestChain(1000000L));
	}
	
	public static long longestChain(long n) {
		long cnt = 0;
		long largestCnt = 0;
		long longestChainNumber = 0;
		for (int i = 1; i < n; i++) {
			cnt = collatzIterations(i);
			if (cnt > largestCnt) {
				largestCnt = cnt;
				longestChainNumber = i;
			}
		}
		return longestChainNumber;
	}
	
	public static long collatzIterations(long n) {
		long cnt = 0;
		while (n != 1) {
			if (n % 2 == 0) n = n / 2;
			else n = 3 * n + 1;
			cnt++;
		}
		return cnt;
	}
}
