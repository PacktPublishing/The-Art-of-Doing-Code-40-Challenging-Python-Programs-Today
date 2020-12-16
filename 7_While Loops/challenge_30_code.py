#While Loops Challenge 30:  Power Ball Simulator App
import random

print("---------------------Power Ball Simulator---------------------")

#Determine the size of the lottery
#Get the number of white-balls
white_balls = int(input("How many white-balls to draw from for the 5 winning numbers (Normally 69): "))
if white_balls < 5:
    white_balls = 5

#Get the number of red-balls
red_balls = int(input("How many red-balls to draw from for the Power Ball (Normally 26): "))
if red_balls < 1:
    red_balls = 1

#Calculate the odds of winning this specific lottery
odds = 1
for i in range(5):
    #Example multiplication for generating odds to win
    #(69*68*67*66*65)*26/120  normal power ball
    #(20*19*18*17*16)*4/120   20 white balls, 4 red balls
    odds *= white_balls - i
odds *= red_balls/120
print("You have a 1 in " + str(odds) + " chance of winning this lottery.")

#Get ticket interval
ticket_interval = int(input("Purchase tickets in what interval: "))

#Generate the winning lottery numbers
#Get the white-balls for the ticket
winning_numbers = []
while len(winning_numbers) < 5:
    number = random.randint(1, white_balls)
    if number not in winning_numbers:
        winning_numbers.append(number)
winning_numbers.sort()

#Get the red-ball for the ticket
number = random.randint(1, red_balls)
winning_numbers.append(number)

#Simulate the power ball drawing
print("\n----------Welcome to the Power Ball----------")
print("\nTonight's winning numbers are: ", end="")
for number in winning_numbers:
    print(str(number), end=' ')

input("\nPress 'Enter' to begin purchasing tickets!!!")

#initialize variables to aid in the selling of tickets
tickets_purchased = 0
active = True
tickets_sold = []

#Run the lottery if we haven't purchased the winning ticket and we still want to play
while winning_numbers not in tickets_sold and active == True:
    #Make a new lottery ticket for the user to buy
    lottery_numbers = []
    #Get the white-balls for the ticket
    while len(lottery_numbers) < 5:
        number = random.randint(1, white_balls)
        if number not in lottery_numbers:
            lottery_numbers.append(number)
    lottery_numbers.sort()

    #Get the red-ball for the ticket
    number = random.randint(1, red_balls)
    lottery_numbers.append(number)

    #This current ticket has not yet been sold
    if lottery_numbers not in tickets_sold:
        tickets_purchased += 1
        tickets_sold.append(lottery_numbers)
        print(lottery_numbers)
    #The ticket has already been sold and is a loser; don't sell again
    else:
        print("Losing ticket generated; disregard...")

    #Check if the user wants to continue buying tickets at the indicated interval
    if tickets_purchased % ticket_interval == 0:
        print(str(tickets_purchased) + " tickets purchased so far with no winners...")
        choice = input("\nKeep purchasing tickets (y/n): ")
        if choice != 'y':
            active = False
    
#The lottery is now over
#We purchased the winning ticket and we won the lottery
if lottery_numbers == winning_numbers:
    print("\nWinning ticket numbers: ", end='')
    for number in lottery_numbers:
        print(str(number), end=' ')
    print("\nPurchased a total of " + str(tickets_purchased) + " tickets.")
#We didn't purchase the winning ticket and we gave up
else:
    print("\nYou bought " + str(tickets_purchased) + " tickets and still lost!")
    print("Better luck next time!")
