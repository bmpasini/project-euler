package solutions;

// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
// a2 + b2 = c2
// For example, 32 + 42 = 9 + 16 = 25 = 52.
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

public class prob9 {
	
	public static void main(String[] args) {
		System.out.println(findProductabc());
	}
	
	public static int findProductabc() {
		int a = 1;
		int b = 1;
		double c = 1;
		
		while(true) {
			for (a = 1; a < 1000; a++) {
				c = findc(a,b);
				if(!iscInt(c))
					continue;
				if(a + b + (int)c == 1000)
					return a*b*(int)c;
			}
			b++;
		}
	}
	
	public static boolean iscInt(double c) {
		return (Math.floor(c) == c);
	}
	
	public static double findc(int a, int b) {
		return Math.sqrt(a*a + b*b);
	}

}
