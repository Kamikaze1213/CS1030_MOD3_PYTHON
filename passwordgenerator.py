import random
import string
#of course, the codes above are going to just import the strings and random

amount = int(input("Enter how many passwords: "))

length = int(input("Length?: "))

#This is gonna get all the lists for the characters needed for creating a password
characters = list(string.ascii_letters + string.digits + string.punctuation)

#so this code will run the nested for loop for the amount that is given
for j in range(amount):
    password = ""

   #this code below just going to create a random password with the given length 
    for i in range(length):
        password += random.choice(characters)

    
    print(password)