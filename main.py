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
randNo = random.randint(1, 3) 
if randNo == 1:
    computer = 's'
elif randNo == 2:
    computer = 'p'
elif randNo == 3:
    computer = 'r'

you = input("Your Turn: Scissor(s) Paper(p) or Rock(r)?")
a = gameWin(computer, you)

print(f"Computer chose {computer}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
