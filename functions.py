score1 = int(input(f"Enter a score: "))
score2 = int(input(f"Enter a second score: "))

#the function
def avg(score1, score2):
    return (score1 + score2)/2

#takes the avg of the score1 & 2 and prints result
result = avg(score1, score2)
print(result)
