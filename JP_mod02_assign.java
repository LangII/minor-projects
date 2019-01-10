
//////////
//
// Rasmussen College, Java Programming,
// Module 02 Assignment - Calculate the Area
//
// (Create an application to calculate the area of a square, rectangle, 
// triangle, or the circumference of a circle through a menu system.)
// 
// by David Lang on 19-01-09
//
//////////

import java.util.Scanner;
import java.text.DecimalFormat;

class JP_mod02_assign {
	
	// Method to determine user's desired program options. 
	public static void main_menu() {
		
    	Scanner menu_input = new Scanner(System.in);
		
		// Display of user main menu with variable 'menu_num' used for
		// user input.
    	System.out.print("\nWhat would you like to do?" + "\n" +
			"\n1)  Calculate the area of a square." +
			"\n2)  Calculate the area of a rectangle." +
			"\n3)  Calculate the area of a triangle." +
			"\n4)  Calculate the circumference of a circle." +
			"\n5)  Calculate the length of the border of a rectangle." +
			"\n" + "\nYour entry:  ");
    	int menu_num = menu_input.nextInt();
		
		// Series of 'if statements' to determine next menu output.
		if (menu_num == 1) {
			areaSquare();
		} else if (menu_num == 2) {
			areaRectangle();
		} else if (menu_num == 3) {
			areaTriangle();
		} else if (menu_num == 4) {
			circumCircle();
		} else if (menu_num == 5) {
			borderRect();
		} else if (menu_num == 0) {
			main_menu();
		} else {
			System.out.println("\nPlease try again.");
			main_menu();
		}
	}

	// Method used to take user input of square side and output square area.
	public static void areaSquare() {
		
		Scanner areaSquare_input = new Scanner(System.in);
		
		// Display prompt to take user input of side length of square.
		System.out.print("\nYou chose calculate the area of a square." +
			"\nPlease key in the length of the sides of the square." +
			"\n\nYour entry:  ");
		double square_side = areaSquare_input.nextDouble();
		// 'if statement' to allow user option to return to main menu.
		if (square_side == 0) {
			main_menu();
		}
		
		// Operation to calculate area of square.
		double area_sq = Math.pow(square_side, 2);
		// Use class 'DecimalFormat' to reduce output of area to 2 decimals.
		DecimalFormat dub_form = new DecimalFormat("0.00");
		
		// Output of area of square from user input.
		System.out.print("\nThe area of a square with side length of "
			+ square_side + " is " + dub_form.format(area_sq) + "." + "\n");
		
		main_menu();
	}
	
	// Method used to take user input of sides of rectangle to calculate area
	// of rectangle as output.
	public static void areaRectangle() {
		
		Scanner areaRectangle_input = new Scanner(System.in);
		
		// Display prompts to take user input of sides of rectangle.
		System.out.print("\nYou chose calculate the area of a rectangle." +
			"\nPlease key in the width of the rectangle.\n\nYour entry:  ");
		double width = areaRectangle_input.nextDouble();
		// 'if statement' to allow user option to return to main menu.
		if (width == 0) {
			main_menu();
		}
		System.out.print("\nPlease key in the length of the rectangle." +
		"\n\nYour entry:  ");
		double length = areaRectangle_input.nextDouble();
		// 'if statement' to allow user option to return to main menu.
		if (length == 0) {
			main_menu();
		}
		
		// Operation to calculate area of rectangle.
		double area_rect = width * length;
		// Use class 'DecimalFormat' to reduce output of area to 2 decimals.
		DecimalFormat dub_form = new DecimalFormat("0.00");
		
		// Output of area of rectangle from user input.
		System.out.print("\nThe area of a rectangle with width of " + width + 
			" and length of " + length + " is " + dub_form.format(area_rect) +
			".\n");
		
		main_menu();
	}

	public static void areaTriangle() {
		
		Scanner areaTriangle_input = new Scanner(System.in);
		
		// Display prompts to take user input of sides of triangle.
		System.out.print("\nYou chose calculate the area of a triangle." +
			"\nPlease key in the width of the triangle.\n\nYour entry:  ");
		double width = areaTriangle_input.nextDouble();
		// 'if statement' to allow user option to return to main menu.
		if (width == 0) {
			main_menu();
		}
		System.out.print("\nPlease key in the length of the triangle." +
		"\n\nYour entry:  ");
		double length = areaTriangle_input.nextDouble();
		// 'if statement' to allow user option to return to main menu.
		if (length == 0) {
			main_menu();
		}
		
		// Operation to calculate area of triangle.
		double area_tri = (width * length) / 2;
		// Use class 'DecimalFormat' to reduce output of area to 2 decimals.
		DecimalFormat dub_form = new DecimalFormat("0.00");
		
		// Output of area of triangle from user input.
		System.out.print("\nThe area of a triangle with width of " + width + 
			" and length of " + length + " is " + dub_form.format(area_tri) +
			".\n");
		
		main_menu();
	}
	
	public static void circumCircle() {
		
		Scanner circumCircle_input = new Scanner(System.in);
		
		// Display prompt to take user input of radius of circle.
		System.out.print("\nYou chose calculate the circumference of a circle."
			+ "\nPlease key in the radius of the circle." +
			"\n\nYour entry:  ");
		double circle_rad = circumCircle_input.nextDouble();
		// 'if statement' to allow user option to return to main menu.
		if (circle_rad == 0) {
			main_menu();
		}
		
		// Operation to calculate circumference of circle.
		double circle_circum = 2 * Math.PI * circle_rad;
		// Use class 'DecimalFormat' to reduce output of circumference
		// to 2 decimals.
		DecimalFormat dub_form = new DecimalFormat("0.00");
		
		// Output of circumference of circle from user input.
		System.out.print("\nThe circumference of a circle with radius of "
			+ circle_rad + " is " + dub_form.format(circle_circum) + ".\n");
		
		main_menu();
	}
	
	public static void borderRect() {
		
		Scanner borderRect_input = new Scanner(System.in);
		
		System.out.print("\nYou chose calculate the border of a rectangle." +
			"\nPlease key in the width of the rectangle.\n\nYour entry:  ");
		double width = borderRect_input.nextDouble();
		// 'if statement' to allow user option to return to main menu.
		if (width == 0) {
			main_menu();
		}
		
		System.out.print("\nPlease key in the length of the rectangle." +
		"\n\nYour entry:  ");
		double length = borderRect_input.nextDouble();
		// 'if statement' to allow user option to return to main menu.
		if (length == 0) {
			main_menu();
		}
		
		// Operation to calculate border of rectangle.
		double border_rect = (width + length) * 2;
		// Use class 'DecimalFormat' to reduce output of border to 2 decimals.
		DecimalFormat dub_form = new DecimalFormat("0.00");
		
		// Output of border of rectangle from user input.
		System.out.print("\nThe border of a rectangle with width of " + width + 
			" and length of " + length + " is " + dub_form.format(border_rect) +
			".\n");
		
		main_menu();
	}
	
    public static void main(String[] args) {
		// Program introduction.
		System.out.println("\nHello!" + "\n\n" + "(If at any time you " +
		"would like to return to the main menu, key in 0 into any entry.)");
    	main_menu();
	}
}

