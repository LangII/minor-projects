"""
SALES STAT CALCULATOR
for Dr. Sengupta's Foundations of Software Design course
at Rasmussen College
by David Lang
2018-08-05
"""

# Declare global variables.
days = {
	'sun': 0,
	'mon': 0,
	'tue': 0,
	'wed': 0,
	'thu': 0,
	'fri': 0,
	'sat': 0
	}
day_trigger = ""
day_sales = 0
days_by_sales = []

"""
Output:
	Processes user input to decide whether to run 'getDayTrigger' function or
	run 'displayTotals' function.
"""
def querryInput():
	# Declare local variables.
	querry = ""
	
	# Set 'querry' as user input.
	querry = input("Would you like to input daily sales or view totals?" + \
	"\n(type 'input' or 'view' as response)\n")
	
	# If user input is 'input' run 'getDayTrigger', if user input is 'view'
	# run 'displayTotals', if neither then repeat display to get user input.
	if querry == 'input':
		getDayTrigger()
	elif querry == 'view':
		displayTotals()
	else:
		print("\nPlease key in response as 'input' or 'view'.  Thank you.\n")
		querryInput()

"""
Output:
	Processes user input to determine which day of the week the user would
	like to update sales of.
"""
def getDayTrigger():
	# Globalize variables.
	global day_trigger
	
	# Set 'day_trigger' as user input.
	day_trigger = input("\nWhich day would you like to enter for sales?\n" + \
	"sun, mon, tue, wed, thu, fri, or sat\n")
	
	# Verify accurate user input as requested.  If not, repeat original user
	# input request.
	if day_trigger not in days:
		print("\nPlease key in abbreviation for weekday exactly like " + \
		"it's displayed.\nThank you.")
		getDayTrigger()
	else:
		getDaySales()

"""
Output:
	Processes user input to update the daily sales display.
"""
def getDaySales():
	# Globalize variables.
	global day_sales
	
	# Set day_sales as user input.  If user input is not submitted as an
	# integer request repeat of user input.
	try:
		day_sales = int(input("\nWhat was the sales for '" + day_trigger + \
		"' that you would like to enter?\n"))
	except ValueError:
		print("\nPlease input your answer in number value only.  " + \
		"Thank you.")
		getDaySales()
	
	# Update display of daily sales.
	days[day_trigger] = day_sales
	
	# Move on to display of daily sales.
	displayTotals()

"""
Output:
	Process calculations on user input to determine values on variables 
	'total_sales', 'avg_sales_input', and 'avg_sales_week' then return as list.
"""
def calcTotals():
	# Declare local variables.
	total_sales = 0
	avg_input_trigger = 0
	avg_sales_input = 0
	avg_sales_week = 0

	# Run for loop to add all days of sales from user input and apply to
	# variable 'total_sales'.
	for each in days:
		total_sales += days[each]

		# While in for loop also increase 'avg_input_trigger' by 1 for every
		# day with user input to be used in calculating input average.
		if days[each] != 0:
			avg_input_trigger += 1
	
	# If statement used to avoid a 'ZeroDivisionError'.
	if avg_input_trigger == 0:
		return [0, 0, 0]
	
	# Update values for output variables.
	avg_sales_input = int(total_sales / avg_input_trigger)
	avg_sales_week = int(total_sales / 7)
	
	# Return as list for singular return statement and ease of calling
	# function's index.
	return [total_sales, avg_sales_input, avg_sales_week]

"""
Output:
	Displays updated daily sales based on previous user input.
"""
def displayTotals():
	# Set variable 'totals' to be array of statistics from 'calcTotals'.
	totals = calcTotals()

	# Make a list of days in order of sales from highest to lowest.
	days_by_sales = sorted(days, key=days.get, reverse=True)

	# Final output of total daily sales and additional statistics based on
	# user input.
	print("")
	print("-" * 50)
	print("")
	print("SALES PER DAY".ljust(25) + "SALES/DAY IN ORDER".rjust(25))
	print(("-" * 13).ljust(25) + ("-" * 18).rjust(25))
	print("sun = " + str(days['sun']).ljust(25) + \
	(str(days[days_by_sales[0]]) + " = " + days_by_sales[0] + \
	" #1").rjust(19))
	print("mon = " + str(days['mon']).ljust(25) + \
	(str(days[days_by_sales[1]]) + " = " + days_by_sales[1] + \
	" #2").rjust(19))
	print("tue = " + str(days['tue']).ljust(25) + \
	(str(days[days_by_sales[2]]) + " = " + days_by_sales[2] + \
	" #3").rjust(19))
	print("wed = " + str(days['wed']).ljust(25) + \
	(str(days[days_by_sales[3]]) + " = " + days_by_sales[3] + \
	" #4").rjust(19))
	print("thu = " + str(days['thu']).ljust(25) + \
	(str(days[days_by_sales[4]]) + " = " + days_by_sales[4] + \
	" #5").rjust(19))
	print("fri = " + str(days['fri']).ljust(25) + \
	(str(days[days_by_sales[5]]) + " = " + days_by_sales[5] + \
	" #6").rjust(19))
	print("sat = " + str(days['sat']).ljust(25) + \
	(str(days[days_by_sales[6]]) + " = " + days_by_sales[6] + \
	" #7").rjust(19))
	print("")
	print("total sales = " + str(totals[0]))
	print("avg sales/day (for days of input) = " + str(totals[1]))
	print("avg sales/day (for whole week) = " + str(totals[2]))
	print("")
	print("-" * 50)
	print("")
	
	# Return to original request of user input.
	querryInput()

# Start program with introduction and run initial request for user input.
print("***  Daily Sales Stat Calculator  ***\n")
querryInput()
