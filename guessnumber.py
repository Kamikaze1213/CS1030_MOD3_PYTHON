import random

number = random.randint(0, 100)

print("Guess the magic number between 0 and 100")

guess = -1

#THIS CODE MAKES A LOOP IF GUESS IS NOT THE NUMBER
while guess != number:
    guess = int(input("\nEnter your guess: "))

    
    if guess == number:
        print(f"Yes, the number is {number}")
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
#THE ELSE CODE IS BASICALLY FOR ANY OTHER NUMBER BESIDES ELIF AND IF