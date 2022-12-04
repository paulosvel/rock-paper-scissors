import random
playerscore = 0
cpuscore = 0
cpupick = ["Rock","Paper","Scissors"]
print("Rock Paper Scissors by Paulosvel")
while (playerscore < 5 and cpuscore < 5):
   while True:
    playerpick = input("Pick r for Rock, p for Paper, s for Scissors: ")
    if (playerpick == "r" or playerpick == "p" or playerpick == "s"):
     break
    else:
     print("Invalid input pick again:")
  
   cpuhand = random.choice(cpupick)
  
   if (playerpick == "r" and cpupick == "Rock") or (playerpick == "p" and cpupick == "Paper") or (playerpick == "s" and cpupick == "Scissors"):
    print("It's a tie try again!")
   elif (playerpick == "r" and cpupick == "Scissors") or (playerpick == "s" and cpupick == "Paper") or (playerpick == "p" and cpupick == "Rock"):
    playerscore = playerscore+1
    print("You Won!",playerscore)
   else:
    cpuscore = cpuscore + 1
    print("You lost",cpuscore)  
print("Your score: ",playerscore,"Cpu Score: ",cpuscore)

