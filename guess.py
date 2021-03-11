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


def computer_guess(x):
    low_num = 1
    high_num = x
    answer = ''

    while answer != 'c':
        number = random.randint(low_num, high_num)
        answer = input(f"Is {number} too high (H), too low (L), or correct (C)").lower()
        if answer == 'h':
            high_num = number - 1
            print("The number is too high")
        elif answer == 'l':
            low_num = number + 1
            print("The number is too low")

    print("That's the correct number")


computer_guess(10)