#While Loops Challenge 26:  Factor Generator App

print("Welcome to the Factor Generator App")

running = True

#Run the program until the user quits
while running:
    #Get user input
    number = int(input("\nEnter a number to determine all factors of that number: "))

    #Find the factors of the user's given number
    factors = []
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)

    #Print out the factors
    print("\nFactors of " + str(number) + " are: ")
    for factor in factors:
        print(factor)

    #Print a summary of the factors mathematically
    print("\nIn summary: ")
    for i in range(int(len(factors)/2)):
        print(str(factors[i]) + " * " + str(factors[-i-1]) + " = " + str(number))

    #Ask the user if they would like to quit
    choice = input("\nRun again (y/n): ").lower()
    if choice != 'y':
        running = False
        print("Thank you for using the program.  Have a great day.")
