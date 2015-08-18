package solutions;

// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

public class prob5 {
	public static void main(String[] args) {
		System.out.println(smallestProduct(20));
	}
	
	public static int smallestProduct(int n) {
		boolean foundIt = false;
		int smallestProduct = 0;
		
		while(!foundIt) {
			smallestProduct++;
			foundIt = true;
			for(int i = 1; i < n && foundIt; i++) {
				foundIt = false;
				if(smallestProduct % i == 0) {
					foundIt = true;
				}
			}
		}
		return smallestProduct;
	}
}
