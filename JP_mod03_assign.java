
//////////
//
// Rasmussen College, Java Programming,
// Module 03 Assignment - Largest and Smallest Value
//
// (Create a program using an array that finds the largest and smallest value
// of an array.)
// 
// by David Lang on 19-01-15
//
//////////

import java.util.Scanner;

class assign {
	
    public static void main(String[] args) {
		
		// Initiate array 'numbers' and designate array's size.
		int[] numbers = new int[5];
		// Initiate variables.
		int max;
		int min;
		
		Scanner input = new Scanner(System.in);
		
		// Program introduction.
		System.out.print("\nHello!!!\n\nPlease key in 5 numbers...\n\n");
		
		// Initiate 'for loop' as user input to designate numbers from array
		// 'numbers'.
		for (int each = 0; each < numbers.length; each++) {
			System.out.print("Number " + (each + 1) + " = ");
			numbers[each] = input.nextInt();
		}
		
		// To initiate sort of 'numbers' array to find max and min, first
		// designate max and min as first index from 'numbers' array.
		max = numbers[0];
		min = numbers[0];
		
		// Initiate 'for loop' to sort array 'numbers' to find max and min.
		for (int each = 1; each < numbers.length; each++) {
			if (max < numbers[each]) {
				max = numbers[each];
			}
			if (min > numbers[each]) {
				min = numbers[each];
			}
		}
		// Final output of max and min numbers from user input.
		System.out.println("\nThe largest number from your entries is " + 
		max + ".");
		System.out.println("The smallest number from your entries is " +
		min + ".");
	}
}
