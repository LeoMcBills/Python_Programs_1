import calendar
'''To write a program that usually deals with dates, it's a good idea to import the inbuilt
Calendar model'''

y = int(input("Enter year: "))
m = int(input("Enter month: "))

#The year and month is stored in the variable today which in the next step is called for its value
print(calendar.month(y, m))

