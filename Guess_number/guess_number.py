def func(n,c):
 c-=1
 if(c>0 or n==x):
    if(n>x):
      print("lower than this")
      if c>1:
        n=int(input("you have "+str(c)+" chances left:\n"))
      else:
        n=int(input("you have "+str(c)+" chance left:\n"))
        
      func(n,c)
    elif(n<x):
      print("upper than this")
      if c>1:
        n=int(input("you have "+str(c)+" chances left:\n"))
      else:
        n=int(input("you have "+str(c)+" chance left:\n"))
      
      func(n,c)
    else:
      print("you win,score is "+str(2*(c+1))+" out of 10")
 else:
   print('you lost, the number was '+str(x))

import random
x=int(random.randrange(0,101))
n=int(input("guess the number from 0 to 100:\n"))
c=int(5)
func(n,c)   