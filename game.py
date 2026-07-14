secretNumber=7
guess=None
while guess !=secretNumber:
    guess=int(input("enter a number"))
    if guess<secretNumber:
        print("too low")
    elif guess>secretNumber:
        print("too high")
    else:
        print("you guessed it right")
        break
print("congrats")
