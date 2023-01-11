#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number = 4
playername = input("what is your name?")
numberofguess = 0
print ("hello",playername,"write number between 1 to 10")
while numberofguess < 3:
    guess = int(input())
    numberofguess += 1
    if guess < number:
        print ("your guess is too low")
    if guess > number:
        print ("your guess is too high")
    if guess == number:
        print ("you win")
else:
            print ("try again")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




