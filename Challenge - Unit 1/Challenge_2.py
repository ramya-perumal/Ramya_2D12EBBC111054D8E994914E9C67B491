# Challenge 2:
# Write a program that determines whether a year entered by the user
# is a leap year or not using ifelif-else statements.


def isLeapYear(year):
  if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    return True
  else:
    return False


yr = int(input("Enter the year : "))

if (isLeapYear(yr)):
  print("Given year {}  is leap year".format(yr))
else:
  print("Given year {}  is NOT leap year".format(yr))
