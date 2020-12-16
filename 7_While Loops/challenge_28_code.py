#While Loops Challenge 28:  Prime Number App
import time

print("Welcome to the Prime Number App")

running = True

#Run the program as long as the user wants
while running:
    #Get user input
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    option = input("Enter your choice 1 or 2: ")

    #Determine if a single number is prime
    if option == '1':
        number = int(input("\nEnter a number to determine if it is prime or not: "))

        #Prime status check
        prime_status = True
        for i in range(2, number):
            if number % i == 0:
                prime_status = False
                break
            
        #Print summary
        if prime_status:
            print(str(number) + " is prime!")
        else:
            print(str(number) + " is not prime!")

    #Determine primes within a range of values and time the calculations
    elif option == '2':
        l_bound = int(input("\nEnter the lower bound of your range: "))
        u_bound = int(input("Enter the upper bound of your range: "))

        primes = []

        #Get the current time
        start_time = time.time()

        #Check prime status of all numbers within l_bound and u_bound
        for prime_candidate in range(l_bound, u_bound + 1):
            #1 is not prime
            if prime_candidate > 1:
                prime_status = True
                for i in range(2, prime_candidate):
                    if prime_candidate % i == 0:
                        prime_status = False
                        break
            else:
                prime_status = False
            #Prime candidate is in fact prime!
            if prime_status:
                primes.append(prime_candidate)

        #Get the current time
        end_time = time.time()

        #Determine the time the calculations took
        delta_time = round(end_time - start_time, 4)

        print("\nCalculations took a total of " + str(delta_time) + " seconds.")
        print("The following numbers between " + str(l_bound) + " and " + str(u_bound) + " are prime: ")
        input("Press enter to continue.")

        for prime in primes:
            print(prime)

    #Not a valid choice entered by the user
    else:
        print("\nThat is not a valid option.")

    #Quit the program if the user does not enter in y
    choice = input("Would you like to run the program again (y/n): ").lower()
    if choice != 'y':
        running = False
        print("\nThank you for using the program.  Have a nice day.")
