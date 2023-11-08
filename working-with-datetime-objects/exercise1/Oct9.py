"""
Functions for working with datetime objects.

Author: Charles Levos
Date:   10/9/23
"""
import datetime


def christmas_day(year):
    """
    Returns ISO day of the week for Christmas in the given year.
    
    The ISO day is an integer between 1 and 7.  It is 1 for Monday, 7 for Sunday 
    and the appropriate number for any day in-between. 
    
    Parameter year: The year to check for Christmas
    Precondition: years is an int > 0 (and a year using the Gregorian calendar)
    """
    # HINT: Make a date object and use the isoweekday method
    #pass                    # Implement this function
    #formula for dateTime is the year first, then month number, then day

    #Created a date object
    Date=datetime.date(year,12,25)
    #convert date object to ISO formatt
    temp=Date.isoweekday()
    #return ISO format date
    return temp



def iso_str(d,t):
    """
    Returns the ISO formatted string of date and time together.
    
    When combining, the time must be accurate to the microsecond.
    
    Parameter d: The month-day-year
    Precondition: d is a date object
    
    Parameter t: The time of day
    Precondition: t is a time object
    """
    # HINT: Combine date and time into a datetime and use isoformat
  #  pass                    # Implement this function

    # create a variable month and extract from the date object month
    month=d.month
    # create a variable day and extract from the date object
    day=d.day
    year=d.year
    hour=t.hour
    minute=t.minute
    seconds=t.second
    microseconds=t.microsecond
    # created datetime object using the previous variables
    temp=datetime.datetime(year,month,day,hour,minute,seconds,microseconds)
    #convert datetime object to ISO formatt 
    temp=temp.isoformat()
    #return datetime object
    return str(temp)

# test case and function calls
currentYear=christmas_day(2023)
print(currentYear)
date=datetime.date(2023,12,25)
t=datetime.time(12,0,0)
test=iso_str(date,t)
print(test)