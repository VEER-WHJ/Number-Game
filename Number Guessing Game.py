import random
a=random.randint(1, 100)
chances=0
while chances<5:
    guess=int(input("Guess a number  ")) 
    if(guess==a):
        print("YOU WIN!")
        break
    elif(guess<a):
        print("Too low")
    elif(guess>a):
        print("Too high")
    else:
        print("Say an integer value")
    chances=chances+1

if(chances==5):
    print("You lose! The number was ", a)
        