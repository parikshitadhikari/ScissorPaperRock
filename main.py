import random

def gameWin(computer, you):

    if computer == you:
        return None
    
    elif computer == 's':
        if you=='p':
            return False
        elif you=='r':
            return True   
   
    elif computer == 'p':
        if you=='r':
            return False
        elif you=='s':
            return True
    
    elif computer == 'r':
        if you=='s':
            return False
        elif you=='p':
            return True

print("Computer Turn: Scissor(s) Paper(p) or Rock(r)?")
randomNum = random.randint(1, 3) 
if randomNum == 1:
    computer = 's'
elif randomNum == 2:
    computer = 'p'
elif randomNum == 3:
    computer = 'r'

you = input("Your Turn: Scissor(s) Paper(p) or Rock(r)?")
a = gameWin(computer, you)

print(f"Computer choose {computer}")
print(f"You choose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
