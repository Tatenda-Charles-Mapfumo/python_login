# This is a program to register the user and allow the user to login after successfully logging in

# Code created by Tatenda Mapfumo

# github profile Tatenda-Charles-Mapfumo

# Program was created using while loops, if statements, else statements and elif statements

while True:
    # User Create Details / User Registration
    name = input("Enter your name: \n").capitalize()
    surname = input("Enter your surname: \n").capitalize()
    user_name = input("Create your username: \n")
    password = input("Create a password: \n")
    # User password registration validation
    password_confirm = input("Confirm your password: \n")

    while True:
        # Password confirmation validation
        if password == password_confirm:
            print(f'Hi {name} {surname}, you have successfully registered! your username is {user_name} and your password is {password} \n \n')
            break
        else:
        # Password validation prompt
            while True:
                print('Please confirm password again \n')
                password_confirm = input("Confirm your password: \n")
                break

    # Login prompt after successfully logging in
    my_prompt = input("Do you wish to login? Enter Y/N: \n").capitalize()

    if my_prompt == 'Y':
        while True:
            user_name_login = input("Enter your username: \n")
            if user_name_login == user_name:
                user_password = input("Enter your password: \n")
                if user_password == password:
                    print(f'Hi {name} {surname}, you have successfully logged in \n')
                    break
                break
            else:
                print("Username not found, please re-enter username or register \n")
                break
    elif my_prompt == 'N':
        print("Thank you, we hope to see you again \n")
        break
    else:
        print("You have made an invalid entry \n")
        break


# Created using pyCharm version 2023.1

# Python 3.10.8