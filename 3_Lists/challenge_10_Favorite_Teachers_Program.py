#Lists Challenge 10:  Favorite Teachers Program

print("Welcome to the Favorite Teachers Program")
fav_teachers = []

#Get user input
fav_teachers.append(input("\nWho is your first favorite teacher: ").title())
fav_teachers.append(input("Who is your second favorite teacher: ").title())
fav_teachers.append(input("Who is your third favorite teacher: ").title())
fav_teachers.append(input("Who is your fourth favorite teacher: ").title())

#Summary of list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(fav_teachers, reverse=True)))
print("\nYour top two teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teacher is: " + fav_teachers[-1] + ".")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")

#Insert a new favorite teacher
fav_teachers.insert(0, input("\nOops, " + fav_teachers[0] + " is no longer your first favorite teacher.  Who is your new FAVORITE teacher: ").title())

#Summary of list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(fav_teachers, reverse=True)))
print("\nYour top two teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teacher is: " + fav_teachers[-1] + ".")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")

#Remove a specific teacher
fav_teachers.remove(input("\nYou've decided you no longer like a teacher.  Which teacher would you like to remove from your list: ").title())

#Summary of list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(fav_teachers, reverse=True)))
print("\nYour top two teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teacher is: " + fav_teachers[-1] + ".")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")
