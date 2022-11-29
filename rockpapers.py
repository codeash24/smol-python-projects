import random, sys
wins, losses, ties, winsCounter,tiesCounter, lossCounter=0,0,0,0,0,0

def goodBye(move):
    if move=='q':
        print("goodbye")
        sys.exit()

def scoreBoard(tiesCounter, winsCounter, lossCounter):
    global wins, losses, ties
    wins=wins+winsCounter
    losses=losses+lossCounter
    ties=ties+tiesCounter
    return wins, losses, ties
    
def machineMove():
    myMove=random.randint(1,3)
    if myMove==1:
        myMove='r'
    elif myMove==2:
        myMove='p'
    else:
        myMove='s'
    return myMove

for i in range(5):
    print("hi, lets play rps!, please put in an input \n r for rock \n p for paper \n s for scissors \n q - goodbye")
    move=input()
    
    goodBye(move)
    myMove=machineMove()
    if move=='s' and myMove=='s' or move=='r' and myMove=='r'or move=='p' and myMove=='p':
        print('love all')
        W, L, T=scoreBoard(1,0,0)
    elif move=='p' and myMove=='r' or move=='r' and myMove=='s' or move=='s' and myMove=='r':
        print('yay')
        W, L, T=scoreBoard(0,1,0)
    else:
        print('aww')
        W, L, T=scoreBoard(0,0,1)

print("W:",W,"L:",L,"T:",T)

'''
ROCK, PAPER, SCISSORS
0 Wins, 0 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
p
PAPER versus...
PAPER
It is a tie!
0 Wins, 1 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
s
SCISSORS versus...
PAPER
You win!
1 Wins, 1 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
q
'''