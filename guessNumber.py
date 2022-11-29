import random 
guess=random.randint(1,20)

for i in range(7):
    # input
    print('I am guessing a number between 1 and 20'+ ' guess what it is')
    number=int(input())
    
    if number==guess:
        print('you rock!, the number is '+ str(guess))
        break
    
    elif number-guess==1 or guess-number==1:
        print('real close buddy, just by a point')
    
    elif number<=guess:
        print('you guessed low')
    
    elif number>=guess:
        print('guessed high')
    