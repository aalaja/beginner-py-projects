import random

def guess(x):
    comp_num = random.randint(1, x)
    my_num = 0
    while my_num != comp_num:
        my_num = int(input(f"Guess a number between 1 and {x}: "))
        if my_num < comp_num:
            print("Wrong! Your guess is too low")
        elif my_num > comp_num:
            print("Wrong! Your guess is too high")
        elif my_num == comp_num:
            print("Correct! You guessed it....you's right")

guess(10)