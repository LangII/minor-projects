
//////////
//
// Rasmussen College, Java Programming,
// Module 05 Project - Final Submission
//
// (( Submit all components of your Stock Market Trading Project. This
// project must include code to connect to a database even though you are
// not connecting to an actual database. Also, this project MUST have all
// of the objectives listed in the project description in order to receive
// all points. ))
// 
// by David Lang on 19-01-31
//
//////////

//////////
// MOC DATABASE STATEMENTS
// package database_console;
//////////

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Random;
import java.io.*;

//////////
// MOC DATABASE STATEMENTS
// import.java.sql.Connection;
// import java.sql.DriverManager;
// import java.sql.SQLException;
//////////

class project {
	
	// Create class 'User' to instantiate user data based on user input.
	public static class User {
		String id;
		String first_name;
		String last_name;
		String password;
		
		// 'User' class constructor.
		public User(String arg_id, String arg_fname, String arg_lname, 
			String arg_pass) {
			id = arg_id;
			first_name = arg_fname;
			last_name = arg_lname;
			password = arg_pass;
		}
		
		// 'User' class accessors.
		public String getId() {
			return id;
		}
		public String getFirstName() {
			return first_name;
		}
		public String getLastName() {
			return last_name;
		}
		public String getPassword() {
			return password;
		}
	}
	
	// Create class 'Stock' to instantiate user data based on user input.
	public static class Stock { 
		String user_id;
		String stock_symbol;
		String stock_desc;
		String stock_value;
		
		// 'Stock' class constructor.
		public Stock(String arg_user_id, String arg_symbol, String arg_desc,
			String arg_value) {
			user_id = arg_user_id;
			stock_symbol = arg_symbol;
			stock_desc = arg_desc;
			stock_value = arg_value;
		}
		
		// 'Stock' class accessors.
		public String getUserId() {
			return user_id;
		}
		public String getStockSymbol() {
			return stock_symbol;
		}
		public String getStockDesc() {
			return stock_desc;
		}
		public String getStockValue() {
			return stock_value;
		}
		
		// 'Stock' class modifiers.
		public void setUserId(String arg_user_id) {
			user_id = arg_user_id;
		}
		public void setStockSymbol(String arg_symbol) {
			stock_symbol = arg_symbol;
		}
		public void setStockDesc(String arg_desc) {
			stock_desc = arg_desc;
		}
		public void setStockValue(String arg_value) {
			stock_value = arg_value;
		}
	} 
	
	// Arrays 'userArray' and 'stockArray' used to store user input data.
	public static ArrayList<User> userArray = new ArrayList<User>();
	public static ArrayList<Stock> stockArray = new ArrayList<Stock>();
	
	// Files 'file_user' and 'file_stock' used to reference data files.
	public static File file_user = new File("userData.csv");
	public static File file_stock = new File("stockData.csv");
	
	// Global variables used for accessing 'admin options'.
	public static String admin_password = "asdf";
	public static String admin_password_conf;
	// Global variable to designate which user is currently operating program.
	public static String current_id;
	

	
	// Method 'main_menu' used as introductory menu for navigation.
	public static void mainMenu() {
    	Scanner input = new Scanner(System.in);
		
		// Main menu introduction and option display.
    	System.out.print("\n[[ MAIN MENU ]]" +
			"\n\n1)  Create NEW user account." +
			"\n2)  LOAD previously created user account." +
			"\n3)  Confirm ADMIN status." +
			"\n\nMenu entry:  ");
    	int selection = input.nextInt();
		
		// Series of 'if statements' taking user input 'selection' to
		// determine next accessed menu.
		if (selection == 1) {
			newAccount();
		}
		else if (selection == 2) {
			loadAccount();
		}
		else if (selection == 3) {
			confirmAdmin();
		}
		else if (selection == 0) {
			mainMenu();
		}
		else {
			System.out.println("\nPlease try again.");
			mainMenu();
		}
	}
	
	// Method 'newAccount' used as interface for user to create a new account
	// for stock viewing access.
	public static void newAccount() {
		String temp_fname;
		String temp_lname;
		String temp_password;
		
		Scanner input = new Scanner(System.in);
		
		// New account menu introduction.
		System.out.print("\n[[ NEW ACCOUNT MENU ]]" +
			"\n\nPlease key in the following entries...");
		
		// Series of user inputs to save user data for account.
		System.out.print("\n\nFIRST NAME entry:  ");
		temp_fname = input.nextLine();
		System.out.print("LAST NAME entry:  ");
		temp_lname = input.nextLine();
		System.out.print("PASSWORD entry:  ");
		temp_password = input.nextLine();
		
		// Confirmation of correct user input data before proceeding.
		System.out.print("\nYour entries are:  " +
			"\n\nFIRST NAME = " + temp_fname +
			"\nLAST NAME = " + temp_lname +
			"\nPASSWORD = " + temp_password);
		System.out.print("\n\nIs this correct?" +
			"\n1)  Yes" +
			"\n2)  No" +
			"\n\nMenu entry:  ");
		int selection = input.nextInt();
		
		// Series of 'if statements' taking user input 'selection' to
		// determine next accessed menu.
		if (selection == 1) {
			// Instance class 'User' from user input, then save input data
			// to 'file_user'.
			userArray.add(new User(newId(), temp_fname, temp_lname,
				temp_password));
			saveToUserFile();

			System.out.print("\nNew account successfully created!!!");
			loadAccount();
		}
		else if (selection == 2) {
			System.out.println("\nPlease try again.");
			newAccount();
		}
		else if (selection == 0) {
			mainMenu();
		}
		else {
			System.out.println("\nPlease try again.");
			newAccount();
		}
	}
	
	// Method 'loadAccount' used as random user identification generator.
	// -----
	// Return = String of unique random 6-digit number.
	// -----
	public static String newId() {
		// Create random 6-digit number.
		Random rand = new Random();
		int num = rand.nextInt(999999) + 1;
		
		// Format random number to always maintain 6-digits regardless of
		// number size.  i.e. 34 = 000034.
		String output = String.format("%06d", num);
		
		// Verify that created number has not been previously assigned.
		for (User each : userArray) {
			if (output == String.valueOf(each.getId())) {
				newId();
			}
		}
		return output;
	}
	
	// Method 'loadAccount' used as interface for user to confirm previously
	// created account data.
	public static void loadAccount() {
		String temp_fname;
		String temp_lname;
		String temp_password;
		
		Scanner input = new Scanner(System.in);
		
		// Reset 'userArray' to include all previously loaded data from
		// old activity.
		loadFromUserFile();

		// Load account menu introduction and data confirmation display.
		System.out.print("\n\n[[ LOAD ACCOUNT MENU ]]" +
			"\n\nTo verify your account, " +
			"please confirm the following entries..." +
			"\n\nFIRST NAME = ");
		temp_fname = input.nextLine();
		System.out.print("LAST NAME = ");
		temp_lname = input.nextLine();
		System.out.print("PASSWORD = ");
		temp_password = input.nextLine();

		// 'For loop' and 'if statement' used to verify user input from
		// previous display with stored user input data from 'userArray'.
		for (User each : userArray) {
			
			if ( temp_fname.equals(each.getFirstName()) &&
				temp_lname.equals(each.getLastName()) &&
				temp_password.equals(each.getPassword()) ) {
					
					// Save 'current_id' for future stock menu access.
					current_id = each.getId();
					
					System.out.print("\nUser name and password confirmed!!!");
					
					// Clear 'userArray' to avoid duplicate entries.
					userArray.clear();
					userOptions();
			}
		}
		// If user input not confirmed prompt retry.
		System.out.print("\nUser name and password were not confirmed..." +
			"\nPlease try again.");
		// Clear 'userArray' to avoid duplicate entries.
		userArray.clear();
		loadAccount();
	}
	
	// Method 'userOptions' used as interface for user to create stock entries
	// or view previously created stock entries.
	public static void userOptions() {
		Scanner input = new Scanner(System.in);
		
		// User options introduction and display of options.
		System.out.print("\n\n[[ USER OPTIONS ]]" +
			"\n\n1)  Create NEW STOCK entry." +
			"\n2)  VIEW previous stock entries." +
			"\n\nMenu entry:  ");
		int selection = input.nextInt();
		
		// Series of 'if statements' taking user input 'selection' to
		// determine next accessed menu.
		if (selection == 1) {
			newStockEntry();
		}
		else if (selection == 2) {
			viewStocks();
		}
		else if (selection == 0) {
			mainMenu();
		}
		else {
			System.out.println("\nPlease try again.");
			userOptions();
		}
	}
	
	// Method 'newStockEntry' used to take user inputs as stock entry.
	public static void newStockEntry() {
		String temp_symbol;
		String temp_desc;
		String temp_value;
		
		Scanner input = new Scanner(System.in);
	
		// New stock entry introduction.
		System.out.print("\n[[ NEW STOCK ENTRY MENU ]]" +
			"\n\nPlease key in the following entries...");
		
		// Series of user inputs to save user data for account.
		System.out.print("\n\nSTOCK SYMBOL entry:  ");
		temp_symbol = input.nextLine();
		System.out.print("STOCK DESCRIPTION entry:  ");
		temp_desc = input.nextLine();
		System.out.print("STOCK VALUE entry:  ");
		temp_value = input.nextLine();
		
		// Confirmation of correct user input data before proceeding.
		System.out.print("\nYour entries are:  " +
			"\n\nSTOCK SYMBOL = " + temp_symbol +
			"\nSTOCK DESCRIPTION = " + temp_desc +
			"\nSTOCK VALUE = " + temp_value);
		System.out.print("\n\nIs this correct?" +
			"\n1)  Yes" +
			"\n2)  No" +
			"\n\nMenu entry:  ");
		int selection = input.nextInt();
		
		// Series of 'if statements' taking user input 'selection' to
		// determine next accessed menu.
		if (selection == 1) {
			// Instance class 'Stock' from user input and save to file.
			stockArray.add(new Stock(current_id, temp_symbol, temp_desc,
				temp_value));
			saveToStockFile();
			
			System.out.print("\nNew stock entry successfully created!!!");
			userOptions();
		}
		else if (selection == 2) {
			System.out.println("\nPlease try again.");
			newStockEntry();
		}
		else if (selection == 0) {
			mainMenu();
		}
		else {
			System.out.println("\nPlease try again.");
			newStockEntry();
		}
	}
	
	// Method 'viewStocks' used to display user's previously created stock data.
	public static void viewStocks() {
		System.out.print("\nYour current stocks are...\n...");
		
		loadFromStockFile();
		
		// 'For loop' to iterate over 'stockArray' and display each
		// entry's data.
		for (Stock each : stockArray) {
			if (current_id.equals(each.getUserId())) {
				System.out.print("\nSTOCK SYMBOL = " + each.getStockSymbol() +
					"\nSTOCK DESCRIPTION = " + each.getStockDesc() +
					"\nSTOCK VALUE = " + each.getStockValue() +
					"\n...");
			}
		}
		// Clear 'stockArray' to avoid duplicate entries.
		stockArray.clear();
		userOptions();
	}
	
	// Method 'saveToUserFile' used to save all data within 'userArray' to
	// file 'file_user'.
	public static void saveToUserFile() {
		try {
			FileWriter file_write = new FileWriter(file_user, true);
			PrintWriter writer = new PrintWriter(file_write);
			
			// 'For loop' used to write each instance of object 'User' to
			// save file 'file_user'.
			for (User each : userArray) {
				writer.append(each.getId() + "," + each.getFirstName() + ","
					+ each.getLastName() + "," + each.getPassword() + "\n");
			}
			// Close 'file_write' and 'writer' objects.
			file_write.close();
			writer.close();
		}
		catch (IOException exc) {
			System.out.println("error = " + exc.getClass().getName());
		}
		// Clear 'userArray' to avoid duplicate entries.
		userArray.clear();
	}
	
	// Method 'saveToFile' used to save all data within 'stockArray' to
	// file 'file_stock'.
	public static void saveToStockFile() {
		try {
			FileWriter file_write = new FileWriter(file_stock, true);
			PrintWriter writer = new PrintWriter(file_write);
			
			// 'For loop' used to write each instance of object 'Stock' to
			// save file 'file_stock'.
			for (Stock each : stockArray) {
				writer.append(
					each.getUserId() + "," + each.getStockSymbol() + "," +
					each.getStockDesc() + "," + each.getStockValue() + "\n"
				);
			}
			// Close 'file_write' and 'writer' objects.
			file_write.close();
			writer.close();
		}
		catch (IOException exc) {
			System.out.println("error = " + exc.getClass().getName());
		}
		// Clear 'stockArray' to avoid duplicate entries.
		stockArray.clear();
	}
	
	// Method 'getLineData' used to aid in parsing csv files.  Method parses
	// individual items within lines.
	// -----
	// Returns = ArrayList of Strings of parsed items from line.
	// -----
	public static ArrayList<String> getLineData(String line) {
		ArrayList<String> items = new ArrayList<String>();
		
		// Parse through argument 'line' with "," delimiter, then add value
		// of each item parsed to 'items' list.
		try (Scanner scanner = new Scanner(line)) {
			scanner.useDelimiter(",");
			while (scanner.hasNext()) {
				items.add(scanner.next());
			}
		}
		catch (RuntimeException exc){
			System.out.println("error = " + exc.getClass().getName());
		}
		return items;
	}
	
	// Method 'loadFromUserFile' used to take previously loaded data to
	// 'file_user' and reassign data to 'userArray'.
	public static void loadFromUserFile() {
		// Establish 2D ArrayList 'data' as temp storage for file data.
		ArrayList<ArrayList<String>> data = new ArrayList<>();
		
		try (Scanner scanner = new Scanner(file_user)) {
			// Iterate over first dimension of file.
			while (scanner.hasNextLine()) {
				// Use method 'getLineData' to iterate over second dimension
				// of file and 'add' data to temp storage.
				data.add(getLineData(scanner.nextLine()));
			}
		}
		catch (FileNotFoundException exc){
			System.out.println(exc.getClass().getName());
		}
		
		// Clear 'userArray' before transfer, then transfer data from temp
		// storage 'data' to 'userArray'.
		userArray.clear();
		for (ArrayList each : data) {
			userArray.add(new User(
				String.valueOf(each.get(0)), String.valueOf(each.get(1)),
				String.valueOf(each.get(2)), String.valueOf(each.get(3))
				));
		}
	}
	
	// Method 'loadFromStockFile' used to take previously loaded data to
	// 'file_stock' and reassign data to 'stockArray'.
	public static void loadFromStockFile() {
		// Establish 2D ArrayList 'data' as temp storage for file data.
		ArrayList<ArrayList<String>> data = new ArrayList<>();
		
		try (Scanner scanner = new Scanner(file_stock)) {
			// Iterate over first dimension of file.
			while (scanner.hasNextLine()) {
				// Use method 'getLineData' to iterate over second dimension
				// of file and 'add' data to temp storage.
				data.add(getLineData(scanner.nextLine()));
			}
		}
		catch (FileNotFoundException exc){
			System.out.println(exc.getClass().getName());
		}
		
		// Clear 'userArray' before transfer, then transfer data from temp
		// storage 'data' to 'userArray'.
		stockArray.clear();
		for (ArrayList each : data) {
			stockArray.add(new Stock(
				String.valueOf(each.get(0)), String.valueOf(each.get(1)),
				String.valueOf(each.get(2)), String.valueOf(each.get(3))
				));
		}
	}

	// Method 'confirmAdmin' used as interface to confirm administrative
	// status and proceed to admin options.
	public static void confirmAdmin() {
		Scanner input = new Scanner(System.in);
		
		// Admin confirmation introduction and admin password confirmation.
		System.out.print("\n[[ ADMIN CONFIRMATION ]]" +
			"\n\nTo verify admin access, " +
			"please confirm the admin password..." +
			"\n\nADMIN PASSWORD = ");
		project.admin_password_conf = input.next();
		
		// Series of 'if statements' to confirm admin password and proceed to
		// admin options menu or return to main menu of password not confirmed.
		if (admin_password.equals(admin_password_conf)) {
			System.out.print("\nAdmin access confirmed!!!");
			adminOptions();
		}
		else {
			System.out.print("\nAdmin access not confirmed..." +
				"\nReturning to main menu...");
			mainMenu();
		}
	}
	
	// Method 'adminOptions' used as interface for admin to modify user entries
	// or view previously created user entries.
	public static void adminOptions() {
		Scanner input = new Scanner(System.in);
		
		// Admin options introduction and display of options. 
		System.out.print("\n\n[[ ADMIN OPTIONS ]]" +
			"\n\n1)  Create NEW user entry." +
			"\n2)  VIEW previous user entries." +
			"\n\nMenu entry:  ");
		int selection = input.nextInt();
		
		// Series of 'if statements' taking user input 'selection' to
		// determine next accessed menu.
		if (selection == 1) {
			newAccount();
		}
		else if (selection == 2) {
			viewAccount();
		}
		else if (selection == 0) {
			mainMenu();
		}
		else {
			System.out.println("\nPlease try again.");
			adminOptions();
		}
	}
	
	// Method 'viewAccount' used to display user's previously created user data.
	public static void viewAccount() {
		System.out.print("\nCurrent user entries are...\n...");
		
		loadFromUserFile();
		
		// 'For loop' to iterate over 'userArray' and display each
		// entry's data.
		for (User each : userArray) {
			System.out.print("\nID = " + each.getId() +
				"\nFIRST NAME = " + each.getFirstName() +
				"\nLAST NAME = " + each.getLastName() +
				"\nPASSWORD = " + each.getPassword() +
				"\n...");
		}
		// Clear 'userArray' to avoid duplicate entries.
		userArray.clear();
		adminOptions();
	}
	
	// Method 'main' used as program introduction.
    public static void main(String[] args) {
		
		//////////
		// MOC DATABASE STATEMENTS
		// String host = "jdbc:derby://localhost:1527/Employees";
		// String uName = "admin";
		// String uPass = "admin";
		// Connection con = DriverManager.getConnection(host, uName, uPass);
		//////////
		
		System.out.println("\nWelcome to STOCK TRACKING" +
		"\n\n(( If at any time you would like to return to the main menu, " +
		"key in 0 into any menu entry. ))");
    	mainMenu();
	}
}

