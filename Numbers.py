print(2.0978)
print(-2.0978)
# When working with numbers, you can enter whole numbers and decimals.
print("I will count the buses now")
print("Buses", 20+30/6)
print("Cars", 100-25*3%4)
print("Is 5 greater than 7?", 5 > 7)
print("Is 5+3 greater than 5+5?", 5+3 < 5+5)
# Mr Monish's Numbers/Math section
# + is add, - is minus, / is divide, * is multiply, % is percent or out of 100, < > is less than or greater than,
# <= => is greater or equals to/ is less than or equals to.
print(3+5*2)
#This is going to give an answer of 13 because multiply comes first, then addition.
print((3+5)*2)
# Putting paranthesis would tell python to add 3 to 5 first, before multiplying by two, resulting in the answer of 16
print(10%3)
# This is called the modulates symbol.
# What this does is that it will divide 10 by 3, and we know it ends in a fraction. So, there is a remainder of 1
# The modulates symbol would give the remainder.
print(20%3)
# Here is another example.
number1=5
print(number1+5)
# Numbers could also be stored in variables.
number2=10
print(str(number2)+" is my favorite number.")
# This would convert a number into a string.

# print(number2+" is my favorite number.")

# Running the code above wouldn't work, only when you turn number2 into a string, would it work.
number3=-5
print(abs(number3))
# This would give the absolute value
print(pow(3,3))
# This would do 3 raised to the power of three, which means, 3x3x3.
print(max(5,10))
# What max does, is that it will choose between the two numbers, and show the larger one, in this case, 10.
print(min(5,10))
# What this does is basically vice versa of max, it would choose the smaller number, and show it, which is 5.
print(round(4.3))
print(round(4.7))
# This would round the number, off to the nearest integer (whole number).
from math import *
# This is a module. It would give you access to more functions.
print(floor(3.9))
#Include <from math import *> in order to do these.
#Floor will round the number of to its lowest possible number.
print(ceil(3.1))
# What Ceil does is essentially it would round the decimal to the highest number possible.
print(sqrt(49))
print(sqrt(48))
# This would return the square root of a number
# If it ends in a decimal, the answer would be the exact same on a standard 12 digit calculator.

#number2=input("Enter another number: ")
#result=number1+number2
#print(result)

# When you recieve input, python is going to automatically convert the two numbers into strings