from random import *
print("How many times do you wanna flip the coin?")
heads = 0
tails = 0
n = int(input())
for i in range(n):
    p = randint(0,1)
    if p == 0:
        heads+=1
    elif p == 1:
        tails+=1
print("You have got",heads,"heads and",tails,"tails.")
