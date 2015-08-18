package solutions;

import java.util.ArrayList;
import java.util.List;

// A palindromic number reads the same both ways.
// The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
// Find the largest palindrome made from the product of two 3-digit numbers.

public class prob4 {
	public static void main(String[] args) {
		System.out.println(findLargestPalindrome(900,999,900,999));
	}
	
	public static int findLargestPalindrome(int min_i, int max_i, int min_j, int max_j) {
		int largestPalindrome = 1;
		for (int i = min_i; i <= max_i; i++) {
			for (int j = min_j; j <= max_j; j++) {
				if (isNumPalindrome(i*j)) {
					if(i*j > largestPalindrome) {
						largestPalindrome = i*j;
					}
				}
			}
		}
		return largestPalindrome;
	}
	
	public static boolean isNumPalindrome(int n) {
		List<Integer> decomposedReverseNumber = decomposeNumIntoReverseList(n);
		return decomposedReverseNumber.equals(reverseList(decomposedReverseNumber));
	}
	
	public static List<Integer> decomposeNumIntoReverseList(int n) {
		List<Integer> numList = new ArrayList<>();
		int N = n;
		while (N > 1) {
			numList.add(N % 10);
			N = N / 10;
		}
		return numList;
	}
	
	public static List<Integer> reverseList(List<Integer> reverseList) {
		List<Integer> list = new ArrayList<Integer>(reverseList);
		for(int i = 0; i < list.size() / 2; i++) {
		    int temp = list.get(i);
		    list.set(i, list.get(list.size() - i - 1));
		    list.set(list.size() - i - 1, temp);
		}
		return list;
	}

}
