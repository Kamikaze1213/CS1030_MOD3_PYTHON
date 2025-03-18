from random import randint


chosen = randint(1,3)
#print(chosen)


player = input('rock (r), paper (p) or scissors (s)?')


if(chosen == 1):
     computer = 'r'

elif(chosen == 2):
    computer = 'p'

else:
    computer = 's'
if(player == computer):
    print("draw")

elif (player)

