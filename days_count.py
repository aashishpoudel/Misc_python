
"""
### @Author - Aashish
### Asks for the event date and
### Displays the number of days towards some event

"""

from datetime import datetime, date
import string
import re

now = datetime.now()  #now type is string
current_month = now.month
current_day = now.day
current_year = now.year
event_mmddyyyy = ""


def isformatMMDDYYYY(mystr_mmddyy):
    pattern = r'\d\d\/\d\d\/\d\d\d\d'
    if re.match(pattern, mystr_mmddyy):
        return True
    else:
        return False


myinput = False
while(myinput==False):
    event_mmddyyyy = input("Enter event date in MM/DD/YYYY format:")
    if not isformatMMDDYYYY(event_mmddyyyy):
        print("The input not in MM/DD/YYYY format. \nEnter again \n")
        continue
    myinput = True


pattern = r'(\d\d)\/(\d\d)\/(\d\d\d\d)'
myMatch = re.search(pattern, event_mmddyyyy)
event_month = myMatch.group(1)
event_day = myMatch.group(2)
event_year = myMatch.group(3)

current = {"year": current_year, "month": current_month, "day": current_day}
event = {"year": event_year, "month": event_month, "day": event_day}

#print("Current Date is " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))
#print("Event Date is " + event_month + "/" + event_day + "/" + event_year)

current_date = datetime(current_year, current_month, current_day)
event_date = datetime(int(event_year), int(event_month), int(event_day))
delta = current_date - event_date

days_count = delta.days

print("Number of days remaining is: " + str(delta))
print(current_date)
print(event_date)


