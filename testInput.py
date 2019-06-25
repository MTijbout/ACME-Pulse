# Python 3
import getpass

txt = input("Enter your username: ")
pwd = getpass.getpass("Enter your password: ")

# Note that in version 3, the print() function
# requires the use of parenthesis.
print("Username = ", txt)
print("Password = ", pwd)
