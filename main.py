# This is a program to register the user and allow the user to login after successfully logging in

# Code created by Tatenda Mapfumo

# github profile Tatenda-Charles-Mapfumo

# Program was created using while loops, if statements, else statements and elif statements

while True:
    # User Create Details / User Registration
    name = input("Enter your name: ").capitalize()
    surname = input("Enter your surname: ").capitalize()
    user_name = input("Create your username: ")
    password = input("Create a password: ")
    # User password registration validation
    password_confirm = input("Confirm your password: ")

    while True:
        # Password confirmation validation
        if password == password_confirm:
            print(f'Hi {name} {surname}, you have successfully registered! your username is {user_name} and your password is {password}')
            break
        else:
        # Password validation prompt
            print('Please confirm password again')
            password_confirm = input("Confirm your password: ")
            break

    # Login prompt after successfully logging in
    my_prompt = input("Do you wish to login? Enter Y/N: ").capitalize()

    if my_prompt == 'Y':
        while True:
            user_name_login = input("Enter your username: ")
            if user_name_login == user_name:
                user_password = input("Enter your password: ")
                if user_password == password:
                    print(f'Hi {name} {surname}, you have successfully logged in')
                    break
                break
            else:
                print("Username not found, please re-enter username or register")
                break
    elif my_prompt == 'N':
        print("Thank you, we hope to see you again")
        break
    else:
        print("You have made an invalid entry")
        break


# Created using pyCharm version 2023.1

# Python 3.10.8