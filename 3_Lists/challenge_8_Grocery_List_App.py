#Lists Challenge 8:  Grocery List App
import datetime

#Create the datetime object and store the current date and time
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

#Welcome message
foods = ["Meat", "Cheese"]
print("Welcome to the Grocery List App")
print("Current Date and Time: " + month +  "/" + day + "\t" + hour + ":" + minute)
print("You currently have " + foods[0] + " and " + foods[1] + " in your list.")

#Get user input
food = input("\nType of food to add to the grocery list: ")
foods.append(food.title())
food = input("Type of food to add to the grocery list: ")
foods.append(food.title())
food = input("Type of food to add to the grocery list: ")
foods.append(food.title())

#Print and sort the list
print("\nHere is your grocery list: ")
print(foods)
foods.sort()
print("Here is your grocery list sorted: ")
print(foods)

#Simulate Shopping
print("\nSimulating grocery shopping...")
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list...")

print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list...")

print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list...")

#The store is out of an item...
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
no_item = foods.pop()
print("\nSorry, the store is out of " + no_item + ".")
new_food = input("What food would you like instead: ").title()
foods.insert(0, new_food)

print("\nHere is what remains on your grocery list: ")
print(foods)
