import random
com = random.randint(1, 100)

while True:
    hum = int(input("guess ur number :- "))

    if hum == com:
        print("congrats u have won the game !")
        break;

    elif hum < com:
        print("soryy wrong guess ur number is too lower")   
    elif hum > com:
        print("soryy wrong guess ur number is too higher")  