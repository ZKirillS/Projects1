import random

a=random.randint(1,9)
b=int(input('Select a number from 1 to 9:'))
while True:
    if b!=a:
        print("Better luck next time");
        break
    elif b==a:
        print("Winner");
        break       
