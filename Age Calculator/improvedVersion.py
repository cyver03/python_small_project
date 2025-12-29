from calendar import isleap
from datetime import datetime
from datetime import date
import time

age = 0
yearToday = date.today().year
monthToday = date.today().month
dayToday = date.today().day
splitBday = []

def isLeapYear(year) : 
    return isleap(year)

def getNumberOfDays() :
    birth_year = int(splitBday[0])
    birth_month = int(splitBday[1])
    birth_day = int(splitBday[2])
    
    days = 0
    
    if birth_year == yearToday:
        if birth_month == monthToday:
            days = dayToday - birth_day
        else:
            for m in range(birth_month, monthToday):
                if m == birth_month:
                    days += getDays(m, birth_year) - birth_day
                else:
                    days += getDays(m, birth_year)
            days += dayToday
    else:
        # Days from birth to end of birth year
        days += getDays(birth_month, birth_year) - birth_day
        for m in range(birth_month + 1, 13):
            days += getDays(m, birth_year)
        
        # Full days in years between
        for yr in range(birth_year + 1, yearToday):
            days += 365 + (1 if isLeapYear(yr) else 0)
        
        # Days in current year from start to today
        for m in range(1, monthToday):
            days += getDays(m, yearToday)
        days += dayToday
    
    return days

def getDays(m, year):
    if m == 2 :
        if isLeapYear(year) :
            return 29
        else :
            return 28
    elif m in [1, 3, 5, 7, 8, 10, 12] :
        return 31
    else : 
        return 30

def getNumberOfMonths() :
    firstMonth = 12 - int(splitBday[1])
    secondYear = int(splitBday[0]) + 1
    return ((yearToday - secondYear) * 12) + firstMonth + monthToday

def validateDateInput(bday) :
    try :
        datetime.strptime(bday, '%Y-%m-%d')
        return True
    except ValueError :
        print("Invalid input. Please enter a validate birth date.")
        return False 
    
name = input("Enter your name:")

try :
    age = int(input("Enter your age : "))
except ValueError :
    print("Invalid input. Please enter a valid age.")

birthDate = input("Enter your birth date (YYYY-MM-DD): ")
if not validateDateInput(birthDate) :
    exit()

splitBday = birthDate.split('-')

print(f"\nHello, {name} your birthday is {birthDate}.", end=" ")
print(f"Your age is {age} or in months {getNumberOfMonths()} or in days {getNumberOfDays()}\n")