# -*- coding: utf-8 -*-
#%%
def flowControl():
    name = input("what is your name")
    age = int(input("whats your age,{}".format(name)))
     
    if age > 18:
        print("You have the rights for voting")
    else:
        print("Come after {}".format(18 - age))
         
   
    if  16 <= age <= 65:
        print("Have a good day at work")
   
    parrot = "How are you"
    letter = "y"
    value  = "g"

    if letter in parrot :
        print("Letter {0} is in Parrot".format(letter))
  
    if value not in parrot:
        print("Value {0} is not in parrot".format(value))
