from math import *
num1=float(input("Enter First Number: "))
op=input("Enter the Operator(+, -, /, *): ")
num2=float(input("Enter the second Number: "))
# This is the input. It allows for decimals and integers to be entered.
if op == "+":
    print(num1+num2)
elif op== "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid Operator")
# These are the functions to make the calculator run.


