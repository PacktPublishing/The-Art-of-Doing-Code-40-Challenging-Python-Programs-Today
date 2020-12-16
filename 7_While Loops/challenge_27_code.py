#While Loops Challenge 27:  Even Odd Number Sorter App

print("Welcome to the Even Odd Number Sorter App")

running = True

#Run the program as longs as the user wants
while running:
    #Get user input
    num_string = input("\nEnter in a string of numbers separated by a comma (,) : ")
    num_string = num_string.replace(' ', '')
    num_list = num_string.split(",")

    #Initialize lists to hold even/odd values
    evens = []
    odds = []

    #Calculate whether the number is even or odd
    print("\n----  Result Summary ----")
    for number in num_list:
        number = int(number)
        if number % 2 == 0:
            evens.append(number)
            print("\t" + str(number) + " is even!")
        else:
            odds.append(number)
            print("\t" + str(number) + " is odd!")

    #Sort the lists evens and odds
    evens.sort()
    odds.sort()

    #Show the even numbers
    print("\nThe following " + str(len(evens)) + " numbers are even: ")
    for even in evens:
        print("\t" + str(even))

    #Show the odd numbers
    print("\nThe following " + str(len(odds)) + " numbers are odd: ")
    for odd in odds:
        print("\t" + str(odd))

    #Quit the program if the user does not enter in 'y'
    choice = input("\nWould you like to run the program again (y/n): ").lower()
    if choice != 'y':
        running = False
        print("Thank you for using the program.  Goodbye.")    
