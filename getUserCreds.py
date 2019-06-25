# Python 3
import getpass

def user_creds():
    print()
    uname = input("Enter your username: ")
    pwd = getpass.getpass("Enter your password: ")

    # Note that in version 3, the print() function
    # requires the use of parenthesis.
    #print("Username = ", uname)
    #print("Password = ", pwd)
    return (uname, pwd)
