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
    days = 0
    #get days on this year
    for m in range(1, time.localtime.tm_mon) :
        if m == 2 :
            if isLeapYear(yearToday) :
                days += 29
            else :
                days += 28
        elif m in [1, 3, 5, 7, 8, 19, 12] : 
            days += 31
        else :
            days += 30

    for yr in range(int(splitBday[0]) + 1, yearToday) :
        #print(yr)
        if isLeapYear(yr) :
            days += 366
        else :
            days += 365
    return days

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