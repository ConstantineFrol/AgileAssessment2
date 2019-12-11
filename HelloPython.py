#!/usr/bin/python
# R00131068

import datetime
import os
import re
import sys

# Global variables
from numpy import var

now = datetime.datetime.now()
user = []


# Menu
def displayMenu():
    ans = True
    while ans:
        print("""
        1.Register
        2.Clock in
        3.Exit/Quit
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            registrationProcess()
        elif ans == "2":
            print("")
            clockInProcess()
        elif ans == "3":
            print("\n Goodbye")
            ans = False
        else:
            print("\n Not Valid Choice Try again")


# End Menu

# Registration Process
def registrationProcess():
    complete = False
    while not complete:
        username = input("Please type in username\n")
        if username not in user:
            password = input("Please type in password\n")
        else:
            print("! User with such name Already Exist !\n")
            continue
        conf_username = input("Repeat the username?\n")
        conf_password = input("Repeat the password?\n")

        if username != conf_username or password != conf_password:
            print("username or password does not match\n")
            continue
        if username in user:
            print("User has been identified, Welcome", username)
            complete = True
        else:
            user.append("User: " + username)
            user.append("Password: " + password)
            print("User created successfully\n")
            for usr in user:
                print(usr)
            displayMenu()


# End Registration Process

# Clocking in Process
def clockInProcess():
    statTime = 8
    if now.hour < statTime:
        print(now.hour)
    elif now.hour == statTime:
        storeDataProcess("%Y-%m-%d %H:%M")
    elif (now.hour == statTime and now.minute >= 1):
        print(now.hour)
        storeDataProcess("%Y-%m-%d %H:%M")
    elif now.hour >= (statTime + 6) and now.hour < (statTime + 7):
        print(now.hour)
        storeDataProcess("%Y-%m-%d %H:%M")
    elif (now.hour == (statTime + 7) and now.minute <= 5):
        print(now.hour)
        storeDataProcess("%Y-%m-%d %H:%M")
    elif (now.hour == (statTime + 7) and now.minute >= 5):
        print(now.hour)
        storeDataProcess("%Y-%m-%d %H:%M")
    elif (now.hour == (statTime + 9) and now.minute <= 5):
        print(now.hour)
        storeDataProcess("%Y-%m-%d %H:%M")
    elif now.hour > (statTime + 9):
        print(now.hour)
        storeDataProcess("%Y-%m-%d %H:%M")


# End of Clocking Process

# Store Records on File
def storeDataProcess(var):
    filepath = '/Users/gog/Documents/GitHub/AgileAssessment2/ClockingMachine/shifts.txt'
    mode = 'a' if os.path.exists(filepath) else 'w'
    with open(filepath, mode) as f:
        f.write(now.strftime(var + "\n"))
        f.close()


# End Store Records on File

displayMenu()

print("The End")
print("The End")

