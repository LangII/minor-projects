
import java.util.Scanner;

class JP_mod01_assign {
    public static void main(String[] args) {
    	
		// Create object 'input' of 'Scanner' class.
    	Scanner input = new Scanner(System.in);
		
		// From user input, assign value to created variable 'number' and
		// create object 'reverse'.
    	System.out.print("Input your number and press enter:  ");
    	int number = input.nextInt(), reverse = 0;
		
		// Initiate while loop, terminate loop when variable 'number' is equal
		// to 0.
		while(number != 0) {
			
			// Create variable 'digit' and assign it value of first digit of
			// variable 'number'.
            int digit = number % 10;
			
			// Move all digits within variable 'reverse' to left by 1, then
			// assign first digit of 'reverse' the value of variable 'digit'.
            reverse = reverse * 10 + digit;
			
			// Remove first digit from within variable 'number'.
            number /= 10;
        }
		
		// Initiate final output.
    	System.out.println("Reverse of input number is:  " + reverse);
    }
}
