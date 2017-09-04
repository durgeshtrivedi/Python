# -StartPython.py *- coding: utf-8 -*-
"""
Spyder Editor

#%% starts a new cell. Use second green triangle to run just the cell that
your mouse has last clicked in (or Ctrl-Enter on a PC or Command-Return on a
Macintosh or Menu>Run>Run Cell)
"""
#%%
def hello():
    print("Hello, world!")
    name = input("What is your name ?")
    print(name)
    x = 5; y = 6
    
    if x < 6 and y == 6 :
        print("The statement is correct")
    
    if x == 5 :
        print("X == 5")
    elif x < 5:
      print ("X is not 5")
    else: 
        print("Its y")      
        
    print("This is X Equal to Y", x == y)
    print("This Y greather y", y > 6)

  
#%%
def myname():
    print("My name is Bill")
    x = 0
  """  while x <= 2:
        print(x, end=" ")
        x +=1  """
    #count = 10
    for value in range(10,0,-1):
        print(value,end= " ")
#%%
def ourschool():
    print("Coursera is our school")
#%%  
  
""" This will run forever. In this case Ctrl-C will stop it, but sometimes
that doesn't work. In that case, click away IP Console to stop; click yes to 
kill kernel. Open a new IPConsole on the Console menu to restart """
#%%
def forever():
    while True:
        pass
  
#%% 
    