# -*- coding: utf-8 -*-
#%%
def stringFormatting():
    newstring = "The string is split \n in to \n three parts"
    print(newstring)
    print(newstring[0:1:2])
    tabstring = "1\t2\t3\t"
    print(tabstring)
    
    anotherstring = """ hello mulit line 
                          string 
                              in 3 lines """
    print(anotherstring)
    print(''' The pet owner said "No, no 'e's uh...,he's resting''' )

    number = "1, 2, 3, 4, 5, 6, 7, 8, 9"
    print(number[0::3])
    print(number[1::3])
    
    print("Hello " *4)
    today = "HOW are you doing today"
    print ("day" in today)
    print ("HOW" in today)
    print("how" in today)    
    
    age = 24 
    print("My age is" + str(age))
    print ("My age in year 2017 is {0} ".format(age))
    print("There  are {0} days in months {1} {2} {3} ".format(31,"Jan", "March" ,"May"))
    print(""" Jan : {2}
       Feb: {0}
       March: {2}
       April: {1}
       May : {2}
       Jun :{1}""".format(28,30,31))
    for i in range(1,12):
        print("No {0} squared is {1}  and cubed is {2}".format(i,i**2,i**3))
    
    for i in range(1,12):
        print("No {0:2} squared is {1:2}  and cubed is {2:4}".format(i,i**2,i**3))
        
    for i in range(1,12):
        print("No {0:2} squared is {1:<4}  and cubed is {2:<4}".format(i,i**2,i**3))
        
    for i in range(1,12):
        print("No {} squared is {:2}  and cubed is {:4}".format(i,i**2,i**3)) # it default follow the order
        
    print("Value of PI is Aproximate {0:12.50f}".format(22/7))    
    