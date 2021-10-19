# We are going to try to watch out for errors
# Basically handle them

try:
    number=int(input("Enter a Number: "))
    print(number)
except:
    print("Invalid Input")
# This would throw out invalid input, rather than break your program.
# But there is a problem with this.
# It would give out invalid input everytime there is an error with input.
try:
    value = 10 / 0
    number=int(input("Enter a Number: "))
    print(number)
except:
    print("Invalid Input")
# As you can see, despite me typing in a integer, the program crashes.
try:
    #value = 10 / 0
    number=int(input("Enter a Number: "))
    print(number)
except ZeroDivisionError:
    print("Divided By Zero")
except ValueError:
    print("Invalid Input")
# This is how to fix the problem: By specifying the type of Error you want to catch.
try:
    #value = 10 / 0
    number=int(input("Enter a Number: "))
    print(number)
except ZeroDivisionError as zerodiverr:
    print(zerodiverr)
except ValueError as valerr:
    print(valerr)
    # This is another method.
    # It would give out an error but not crash your program
