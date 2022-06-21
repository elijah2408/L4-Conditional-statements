isHungry = input("Y/N: Are you hungry? ")
isBored = input("Y/N: Are you bored? ")

if(isHungry == "Y" or isHungry == "y"):
  print("Go eat")
else:
  print("Dont eat")
if(isBored == "Y" or isBored == "y"):
  print ("Go to sleep")
else:
  print("Do nothing")
  
userNumber = int(input( "Give me a number: "))
if(userNumber >= 0):
  print("Your number is positive")
else:
  print("Your number is negative")
  
#ask user for thier age.
#If the user is older than 17 or older, let them know the can watch all the movies.
#If they're younger than 17 but older than 13, let them know they can watch G-rated and PG-13.
#If they're younger than 13, they're olny allowed to watch just G-rated movies.

userAge = int(input("Enter your age: "))

if(userAge >= 17):
  print("You can watch all movies!")
elif(userAge <17 and userAge >= 13):
  print("You can watch G-rated and PG-13 movies!")
else:
   print("You can only watch G-rated movies.")