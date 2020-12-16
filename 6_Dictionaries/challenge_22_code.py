#Dictionaries Challenge 22:  Database Admin Program

print("Welcome to the Database Admin Program")

#Create a dictionary to hold all username:password key-value pairs
log_on_information = {
    'mooman74':'alskes145',
    'meramo1986':'kehns010101',
    'nickyD':'world1star',
    'george2':'booo3oha',
    'admin00':'admin1234',
    }

#Get user input
username = input("Enter your username: ")

#Simulate logging on...
#Get user password
if username in log_on_information.keys():
    password = input("Enter your password: ")
    if password == log_on_information[username]:
        print("\nHello " + username + "!  You are logged in!")
        if username == 'admin00':
            #Show the whole database to the admin account
            print("\nHere is the current user database:")
            for key, value in log_on_information.items():
                print("Username: " + key + "\t\tPassword: " + value)
        else:
            #Allow standard user to change their password
            password_change = input("Would you like to change your password (yes/no): ").lower().strip()
            if password_change == 'yes':
                new_password = input("What would you like your new password to be (min 8 chars): ")
                if len(new_password) >= 8:
                    log_on_information[username] = new_password
                else:
                    print(new_password + " is not the minimum eight characters.")
                print("\n" + username + " your password is " + log_on_information[username] + ".")
            else:
                print("\nThank you, goodbye.")
    #User did not enter their password correctly
    else:
        print("Password incorrect!")
#User not in database
else:
    print("Username not in database.  Goodbye.")
