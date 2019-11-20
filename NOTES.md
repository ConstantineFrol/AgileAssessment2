=== 1. Sign in ==========================
Step One ~~~ Registration
Step Two ~~~ Log In
Step Three ~ 3 Wrong input, wait 1 min and repeat
Step Four ~~ Or Log in Or Register(Can't reg. more than once)

=== 2. Clock in ==========================
Step One
Step Two
Step Three
Step Four

=== 1. Calculation ==========================
Step One
Step Two
Step Three
Step Four

=== 1. Write into file ==========================
Step One
Step Two
Step Three
Step Four


Menu:

ans=True
while ans:
    print("""
    1.Add a Student
    2.Delete a Student
    3.Look Up Student Record
    4.Exit/Quit
    """)
    ans=raw_input("What would you like to do? ")
    if ans=="1":
      print("\nStudent Added")
    elif ans=="2":
      print("\n Student Deleted")
    elif ans=="3":
      print("\n Student Record Found")
    elif ans=="4":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")

Timer:

import time
run = raw_input("Start? > ")
mins = 0
# Only run if the user types in "start"
if run == "start":
    # Loop until we reach 20 minutes running
    while mins != 20:
        print(">>>>>>>>>>>>>>>>>>>>> {}".format(mins))
        # Sleep for a minute
        time.sleep(60)
        # Increment the minute total
        mins += 1
    # Bring up the dialog box here

Validation Username & Password:

# I believe this is what you're trying to do
complete = False
user = {"some username" : "some password", "more username" : "more password"}

while not complete:
    username = input("What is the username?")
    password = input("What is the password?")
    conf_username = input("Repeat the username?")
    conf_password = input("Repeat the password?")
    # since in your question you said you wanted to ask the user to repeat
    if username != conf_username or password != conf_password:
        print("username or password does not match") # print a message if different inputs
        continue # restarts
    if not username in user: # check to see if user does not exists
        print("Input username again!")
        continue
    if password == user[username]: # check to see if password match
        print("User has been identified, Welcome",username)
        complete = True
    else:
        print("Input password again")

Object of User:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)