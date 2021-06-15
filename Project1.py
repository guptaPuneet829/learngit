import random
def gamewin(computer,you):
    if(computer==you):
        return None
    elif computer=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif computer=='s':
        if you=='g':
            return True
        elif you=='w':
            return False
    elif computer=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
print("Computer Turn: Snake(s) Water(w) or Gun(g)?")
randNumber=random.randint(1,3)
if randNumber==1:
    computer='s'
elif randNumber==2:
    computer='w'
elif randNumber==3:
    computer='g'
you=input("Your Turn: Snake(s) Water(w) or Gun(g)?")
k=gamewin(computer,you)
print(f"Computer choose {computer}")
print(f"You choose {you}")
if k==None:
    print("Game is tie")
elif k:
    print("You win!")
else:
    print("You lose!")
                


