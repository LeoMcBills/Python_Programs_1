'''A python program that prompts a user for integer input, gets its difference from 17 and if 
the difference is negative then an absolute double result is returned'''

num = int(input("Enter a number of your choice: "))

#diff is the difference
diff = num - 17

#Conditions
if diff > 0:
    print("The number you entered was positive and the difference is ", diff)

elif diff == 0:
    print("Please enter a non zero figure.")

else:
    absolute = abs(2 * diff)
    print("The asolute  double value of the negative entered is ", absolute)
