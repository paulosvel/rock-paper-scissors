import random
playerscore = 0
cpuscore = 0
cpupick = ["Rock","Paper","Scissors"]
print("Rock Paper Scissors by Paulosvel")
while (playerscore < 5 and cpuscore < 5):
   cpuhand = random.choice(cpupick)
   while True:
    playerpick = input("Pick r for Rock, p for Paper, s for Scissors: ")
    if (playerpick == "r" or playerpick == "p" or playerpick == "s"):
     break
    else:
     print("Invalid input pick again:") 
   if (playerpick == "r" and cpuhand == "Rock") or (playerpick == "p" and cpuhand == "Paper") or (playerpick == "s" and cpuhand == "Scissors"):
    print("It's a tie try again!")
   elif (playerpick == "r" and cpuhand == "Scissors") or (playerpick == "s" and cpuhand == "Paper") or (playerpick == "p" and cpuhand == "Rock"):
    playerscore = playerscore+1
    print("You Won!",playerscore)
   else:
    cpuscore = cpuscore + 1
    print("You lost",cpuscore)  
print("Your score: ",playerscore,"Cpu Score: ",cpuscore)