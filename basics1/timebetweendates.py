'''A program to calculate the  number of days in a range of given years'''

from datetime import date

before = date(2022, 3, 6)
now = date(2033, 6, 8)

diff = now - before
print(diff.days)
