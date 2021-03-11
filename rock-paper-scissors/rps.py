import random

def rps():
    comp_pick = random.choice(['r','p','s'])
    my_pick = input("Choose 'R' for Rock, 'P' for paper or 'S' for Scissors: ").lower()
    

    if my_pick == comp_pick:
        return 'Play Again'

    if win_conditions(my_pick, comp_pick):
        return 'Victory is Mine!'

    return 'You Lose!'

def win_conditions(player, opponent):
    if (player ==  'r' and opponent == 's') \
        or (player ==  's' and opponent == 'p') or (player ==  'p' and opponent == 'r'):
        return True

print(rps())
