'''
1 : snake
-1 : water
0 : gun
'''

import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = youDict[youstr]

print(f"Your choice: {reverseDict[you]} \nComputer Choice: {reverseDict[computer]}")

if(computer == you):
    print("It's a draw!")

else:
    if(computer == -1 and you == 1):
        print("Congo, You Win!")
    elif(computer == -1 and you == 0):
        print("You Lose, Better luck next time!")
    elif(computer == 0 and you == -1):
        print("Congo, You Win!")
    elif(computer == 0 and you == 1):
        print("You Lose, Better luck next time!")
    elif(computer == 1 and you == 0):
        print("Congo, You Win!")
    elif(computer == 1 and you == -1):
        print("You Lose, Better luck next time!")
    else:
        print("Something went wrong")