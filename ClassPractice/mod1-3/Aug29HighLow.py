import random

rand = random.randint(1,100)
ans = False
UserIn = None
trys = 0



while ans is False:
    userIn = int(input("Guess a number between 1-100: "))
    print(userIn)
    trys += 1

    if userIn == rand:
        ans = True
        print("You are correct, you took ",  trys,  " trys! ")
    elif userIn > rand: 
        print("too high try again")
        

    else: 
         print("too low try again")
         

