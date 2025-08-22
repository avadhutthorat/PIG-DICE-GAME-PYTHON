import random

MIN_NUM = 1
MAX_NUM = 6
def roll():
    randomNum = random.randint(MIN_NUM, MAX_NUM)
    return randomNum


# How many players are playing
while True:
    players = input('\n Enter no. of players (2-4) : ')
    if(players.isdigit()):
        players = int(players)
        if( 2 <= players <= 4):
            break
        else:
            print('Enter no between 2 - 4')
    else:
        print('Invalid input')

print(players)

MAX_SCORE = 50
players_data = [0 for _ in range(players)]
print(players_data)

while max(players_data) < MAX_SCORE:
    for player_idx in range(players):
        print(end='\n\n')
        print(f'************* {player_idx + 1} Playing ********************', end='\n')
        print(f"Your Live score = {players_data[player_idx]}")
        current_score = 0

        while True:
            should_roll = input(f'\nDo you want to roll Player {player_idx + 1} (y / n) : ')
            if should_roll.lower() != 'y':
                break

            value = roll()

            if value > 1:
                current_score += value
                print('You rolled ', value)
            else:
                current_score = 0
                print('Your current turn has ended because of value 1')
                break

            print(f'Player {player_idx + 1}"s current score is {current_score}')

        players_data[player_idx] += current_score 
        print(f'Player {player_idx + 1}"s total score is {players_data[player_idx]}') 

won = players_data.index(max(players_data))
print(f'Final scores - {players_data}', end='\n\n') 
print(f'Player {won + 1} won !!!!!')         




