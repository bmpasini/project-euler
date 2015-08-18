package solutions;

import java.util.List;
import java.util.ArrayList;

// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
// Find the sum of all the multiples of 3 or 5 below 1000.

public class prob1 {

	public static void main(String[] args) {
		displaySumOfMultiples(1000);
	}

	public static void displaySumOfMultiples(int iter) {
		int sum = findSumOfMultiples(iter);
		System.out.println(sum);
	}

	public static int findSumOfMultiples(int iter) {

		List<Integer> multiples = new ArrayList<>();

		for (int i = 1; i < iter; i++) {
			if (isMultipleOfx(i, 3) || isMultipleOfx(i, 5)) {
				multiples.add(i);
			}
		}

		return sumIntList(multiples);
	}

	public static boolean isMultipleOfx(int n, int x) {
		if (n % x == 0) {
			return true;
		} else {
			return false;
		}
	}

	public static int sumIntList(List<Integer> arr) {
		int sum = 0;
		for (int x : arr) {
			sum += x;
		}
		return sum;
	}

}
