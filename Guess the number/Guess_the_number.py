import random
num = random.randint(1,20)
guess = None

while guess != num:
    guess = int(input("Guess a number between 1 and 20: "))

    if guess == num:
        print("Congratulations, you won!!!!")
        break
    else:
        print("Nope, try again")


