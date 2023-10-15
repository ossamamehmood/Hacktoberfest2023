# import the calendar class
import calendar

# Define a function that takes 3 arguments
def count_days(year, month, whichday):

    # Add a counter() method and set variable appropriately
    counter = 0
    # Store the calendar.weekday(year, month, day) in the whichday variable
    whichday = calendar.weekday(year=2020, month=9, day=3)
    counter += whichday # The same as counter + counter = whichday
    print(whichday)
    # Return the whichday variable
    return whichday
# Call the count_days function
count_days(year=2020, month=9, whichday=count_days)
