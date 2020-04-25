# Program to display calendar of the given month and year

# importing calendar module
import calendar
from datetime import date, datetime

mydate = datetime.now()
year_ = mydate.strftime("%Y")
month_ = mydate.strftime("%B")




# To take month and year input from the user comment the block above and uncomment the one below
# year_ = int(input("Enter year: "))
# month_ = int(input("Enter month: "))

# display the calendar
print('Calendar for ' + str(month_) + ' ' + str(year_))
print(calendar.month(year_, month_))
