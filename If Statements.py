gendermale=True
if gendermale:
    print("Your Gender is male.")
# This is an if statement. Anything with an indentation is going to show if the if statement above is true.
# If not, it wouldn't print anything.
gendermale=False
if gendermale:
    print("Your Gender is male.")
else:
    print("You are not a male.")
# Else will happen if the if statement is not satisfied.
gendermale=True
heighttall=False
if gendermale or heighttall:
    print("Your Gender is male or tall or both.")
else:
    print("You are not a male or tall.")
# This is how to check both statements. If one or both statements are ture, the else statement will not run.
# If both statements are false, then it would run else.
opt1=True
opt2=True
if opt1 and opt2:
    print("Both options are satisfied.")
else:
    print("One or no Option has been satisfied.")
# This is similar to or, except both statements need to be true for it to display the if.
gendermale=True
heighttall=False
if gendermale and heighttall:
    print("Your Gender is male and tall.")
elif gendermale and not (heighttall):
    print("You are a short male.")
elif gendermale and not (heighttall):
    print("You are not a male, but you are tall.")
else:
    print("You are not a male or tall.")
# This will see if you are tall, and male specifically.
# Elif basically stands for else if.
def maxnumber(number1,number2,number3):
    if number1 >= number2 and number2 >= number3:
        return number1
    elif number2 >= number1 and number2>= number3:
        return number2
    else:
        return number3
print(maxnumber(5,6,7))
# This function would return the largest number.
def dogcat(text1):
    if "dog" == text1:
        return text1
    else:
        return "cat"
print(dogcat("dog"))
# This function would check if the word matches the one in the function.
spell1=input("What is a vehicle with four wheels: ")
def car(text1):
    if "car" == text1:
        return "Correct!"
    elif "car" == text1:
        return "Correct!"
    else:
        return "Wrong!"
print(car(spell1))
# This is how to make a spelling bee game/guessing game.
# == is equal
# != is not equal
# > is greater than
# < is less than
# >= is greater than or equal to
# <= is less than or equal to






