import random

def is_win (player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    
def play():
    user = input('Select "r" (rock), "p" (paper), or "s" (scissors): ')
    possible_choices = ['r', 'p', 's']

    if not (user in possible_choices) : 
        print (f'The only valid inputs are {possible_choices}')
        
    else:
        opponent = random.choice(possible_choices)

        if (user == opponent):
            print(f'Your opponent chose {opponent}, it is a tie!')

        elif (is_win(user, opponent)):
            print(f'Your opponent chose {opponent}, you won!')

        else:
            print(f'Your opponent chose {opponent}, you lost :(')

play()