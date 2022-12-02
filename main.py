import random
playerscore = 0
cpuscore = 0
cpupick = ["Rock","Paper","Scissors"]
print("Rock Paper Scissors by Paulosvel")
playerpick = input("Pick r for Rock, p for Papper, s for Scissors: ")
cpupick = random.choice(cpupick)
if (playerpick == 'r' and cpupick == 'Rock') or (playerpick == 'p' and cpupick == 'Paper') or (playerpick == 's' and cpupick == 'Scissors'):
 print("It's a tie try again!")
elif playerpick == 'r' and cpupick == 'Scissors':
    playerscore = playerscore+1
    print(playerscore)
