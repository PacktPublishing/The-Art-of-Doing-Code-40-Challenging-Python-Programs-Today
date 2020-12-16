#For Loops Challenge 13:  Factorial Calculator App
import math

print("Welcome to the Factorial Calculator App")

#Get user input
number = int(input("\nWhat number would you like to compute the factorial of: "))

#Display the mathematical relationship of a factorial
print(str(number) + "! = ", end="")
for i in range(1, number):
    print(str(i), end="*")
print(str(number))

#Using the math library
fact = math.factorial(number)
print("\nHere is the result from the math library: ")
print("The factorial of " + str(number) + " is " + str(fact) + "!")

#Using my own algorithm
fact = 1
for i in range(1, number+1):
    fact = fact*i
print("\nHere is the result from my own algorithm: ")
print("The factorial of " + str(number) + " is " + str(fact) + "!")

#Summary
print("\nIt is shown twice that " + str(number) + "! = " + str(fact) + " (with excitement!)")
