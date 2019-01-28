
//////////
//
// Rasmussen College, Java Programming,
// Module 04 Assignment - Sequential File Output
//
// (( Write a program that a user inputs clients with id #, first name,
// last name, and account balance and outputs to a sequential file. Then read
// the data from that output file and print the data. ))
// 
// by David Lang on 19-01-26
//
//////////

import java.io.*;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

class assign {
	
	// Class 'Client' created to instantiate client data based on user input.
	public static class Client {
		String id;
		String first_name;
		String last_name;
		int balance;
		
		// 'Client' class constructor.
		public Client (String arg_id, String arg_fname, String arg_lname,
			int arg_balance) {
			id = arg_id;
			first_name = arg_fname;
			last_name = arg_lname;
			balance = arg_balance;
		}
		
		// 'Client' class accessors.
		public String getId() {
			return id;
		}
		public String getFirstName() {
			return first_name;
		}
		public String getLastName() {
			return last_name;
		}
		public int getBalance() {
			return balance;
		}
		
		// 'Client' class modifiers.
		public void setId(String arg_id) {
			id = arg_id;
		}
		public void setFirstName(String arg_fname) {
			first_name = arg_fname;
		}
		public void setLastName(String arg_lname) {
			last_name = arg_lname;
		}
		public void setBalance(int arg_balance) {
			balance = arg_balance;
		}		
	}

	// Array 'clientArray' used to store user input data.
	public static ArrayList<Client> clientArray = new ArrayList<Client>();
	
	// Method 'loadAccount' used as random user identification generator.
	// -----
	// Return = Unique random 6-digit number.
	// -----
	public static String newId() {
		// Create random 6-digit number.
		Random rand = new Random();
		int num = rand.nextInt(999999) + 1;
		
		// Format random number to always maintain 6-digits regardless of
		// number size.  i.e. 34 = 000034.
		String output = String.format("%06d", num);
	
		// Verify that created number has not been previously assigned.
		for (Client each : clientArray) {
			if (output == each.getId()) {
				newId();
			}
		}
		return output;
	}
	
	// Method 'mainMenu' used as introductory menu for quick navigation.
	public static void mainMenu() {
    	Scanner input = new Scanner(System.in);
		
		// Main menu introduction and option display.
    	System.out.print("\n\n[[ MAIN MENU ]]" +
			"\n\n1)  Input NEW client data." +
			"\n2)  DISPLAY previously created clients' data." +
			"\n\nMenu entry:  ");
    	int selection = input.nextInt();
		
		// Series of 'if statements' taking user input 'selection' to
		// determine next accessed menu.
		if (selection == 1) {
			userInput();
		}
		else if (selection == 2) {
			outputData();
		}
		else {
			System.out.println("\nPlease try again.");
			mainMenu();
		}
	}
	
	// Method 'userInput' takes user input and saves data to file.
	public static void userInput() {
		Scanner input = new Scanner(System.in);
		
		// Series of inputs to collect user data.
		System.out.print("\nPlease key in the requested fields...\n" +
			"FIRST NAME = ");
		String temp_fname = input.nextLine();
		System.out.print("LAST NAME = ");
		String temp_lname = input.nextLine();
		System.out.print("BALANCE = ");
		int temp_bal = input.nextInt();
		System.out.print("\n");
		
		// Confirmation of correct user input data before proceeding.
		System.out.print("Your entries are:  " +
			"\n\nFIRST NAME = " + temp_fname +
			"\nLAST NAME = " + temp_lname +
			"\nBALANCE = " + temp_bal);
		System.out.print("\n\nIs this correct?" +
			"\n1)  Yes" +
			"\n2)  No" +
			"\n\nAnswer:  ");
		int selection = input.nextInt();
		
		// Series of 'if statements' taking user input 'selection' to
		// determine next process.
		if (selection == 1) {
			// Instance class 'User' from user input.
			clientArray.add(new Client(newId(), temp_fname, temp_lname,
				temp_bal));
			
			saveData();
			System.out.print("\nNew client successfully created!!!");
			mainMenu();
		}
		else if (selection == 2) {
			System.out.println("\nPlease try again.");
			userInput();
		}
		else {
			System.out.println("\nPlease try again.");
			userInput();
		}
	}
	
	// Method 'saveData' writes user data to a saved file.
	public static void saveData() {
		
		try {
			File file = new File("mod04_assign.csv");
			
			// Test to see if the save file already exists, if not create one.
			if (!file.exists()) {
				file.createNewFile();
			}
			
			// Create 'writer' object to write to 'file'.
			FileWriter file_write = new FileWriter(file, true);
			PrintWriter writer = new PrintWriter(file_write);
			
			// 'For loop' to write any user data to file.
			for (Client each : clientArray) {
				writer.append(each.getId() + "," + each.getFirstName() +
					"," + each.getLastName() + "," + each.getBalance() +
					"\n");
			}
			// Close objects.
			file_write.close();
			writer.close();
		}
		catch (IOException exc) {
			System.out.print("\nerror found\n");
			mainMenu();
		}
	}
	
	// Method 'outputData' used to return data from saved file.
	public static void outputData() {
		try {
			File file = new File("mod04_assign.csv");
			// Create 'input' object to read 'file'.
			Scanner input = new Scanner(file);
			// Designate that 'input' has a delimiter.
			input.useDelimiter(",");
			
			// 'While loop' tests 'input' for "more lines".
			while(input.hasNext()){
				// If 'while loop' is true, print from 'file' replacing
				// delimiter with " ".
				System.out.print(input.next() + " --- ");
			}
			// Close object.
			input.close();
			
			mainMenu();
		}
		catch (FileNotFoundException exc) {
			System.out.print("\nerror found\n");
			mainMenu();
		}
	}
	
    public static void main (String[] args) {
		System.out.print("\nWelcome! ...");
		mainMenu();
	}
}
