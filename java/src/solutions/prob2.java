package solutions;

// Each new term in the Fibonacci sequence is generated by adding the previous two terms.
// By starting with 1 and 2, the first 10 terms will be:
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
// By considering the terms in the Fibonacci sequence whose values do not exceed four million,
// find the sum of the even-valued terms.

public class prob2 {

	public static void main(String[] args) {
		int limit = 4 * 1000 * 1000;
		printFibonacciEvenNumbersBelowX(limit);
		System.exit(1);
	}

	public static void printFibonacciEvenNumbersBelowX(int x) {
		System.out.println(sumFibonacciEvenNumbersBelowX(x));
	}

	public static int sumFibonacciEvenNumbersBelowX(int x) {

		int fib = 0, i = 1, sum = 0;

		while (fib < x) {
			fib = fibonacci(i++);
			if (fib % 2 == 0) {
				sum += fib;
			}
		}

		return sum;
	}

	public static int fibonacci(int n) {
		if (n == 0 || n == 1) {
			return n;
		} else {

			int last = 0, beforeLast = 1, sum = 1;

			for (int i = 2; i < n; i++) {
				sum = last + beforeLast;
				beforeLast = last;
				last = sum;
			}

			return sum;
		}

	}

}
