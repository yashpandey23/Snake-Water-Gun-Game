"""
0 water
-1 guns
1 snake 
"""
# We all have played snake, water gun game in our childhood. If you haven’t, google the 
# rules of this game and write a python program capable of playing this game with the 
# user. 

import random

computer = random.choice([-1 , 0 , 1])
print(f"Welcome to the game of snaks guns and water \n For choosing snake enter : s \n For choosing water enter : w \n For choosing gun enter : g")

my_choose = input("Enter the choise you want to choose : ")

yourdisc = {"s" : 1 , "w" : 0 , "g" : -1}
reverseddisc = {1 : "sankes" , 0 : "water" , -1 : "games"}
you = yourdisc[my_choose]

print (f"you choose the word : {reverseddisc[you]} \ncomputer choose the word : {reverseddisc[computer]}")

# the if statemnt is started 

if (computer == you ):
    print("It is draw")
else :
    if (computer == -1 and you == 1):
        print("You Loss the games!")    
    elif(computer == -1 and you == 0):
         print("You won the games!")    
    elif(computer == 1 and you == -1):
         print("You won the games!")  
    elif(computer == 1 and you == 0):
         print("You loss the games!")  
    elif(computer == 0 and you == 1):
         print("You won the games!")  
    elif(computer == 0  and you == -1):
         print("You Loss the games!")  
    else :
         print("Something went wrong : ")         