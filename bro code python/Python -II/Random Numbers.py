import random

# print(help(random)) -- find all methods...




# Random guess
low = 1
high = 100
num1 = random.randint(low, high) # for integer(need two ranges)
num2 = random.random()  # for float number(no need for range).
#print(num1,"\n",num2)



# Rock, Paper, Scissors: 
options = ("rock", "paper", "scissors")
rps = random.choice(options)
#print(rps)



# For Cards:
cards = ["2","3","4","5","6","7","8","9","10","A","J","K","Q"]
random.shuffle(cards)
print(cards)
