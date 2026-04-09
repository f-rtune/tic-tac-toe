game_state = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
turn = 1
usedNums1 = []
usedNums2 = []
player1score = 0
player2score = 0


def display(game_state):
    print('\n')
    for row in game_state:
        print('|' + '|'.join(row) + '|')


def play(turn):

    global player1score
    global player2score

    won = False
    inp = int(input())

    if not (1 <= inp <= 9) or str(inp).isdigit() == False:
        print('Error, invalid input.')
        play(turn)

    if inp in (usedNums1 or usedNums2):
        print('Error, space is already in use.')
        play(turn)

    if turn == 1 and len(usedNums1) == 3:
        lastX = usedNums1.pop(0)
        game_state[(lastX-1)//3][(lastX-1) % 3] = ' '

    if turn == 2 and len(usedNums2) == 3:
        lastO = usedNums2.pop(0)
        game_state[(lastO-1)//3][(lastO-1) % 3] = ' '

    if turn == 1:
        usedNums1.append(inp)
    elif turn == 2:
        usedNums2.append(inp)

    if turn == 1:
        game_state[(inp-1)//3][(inp-1) % 3] = 'X'
    else:
        game_state[(inp-1)//3][(inp-1) % 3] = 'O'

    display(game_state)

    # --- ROW

    for row in game_state:
        if row.count('X') == 3:
            print('Player 1 wins.')
            won = True
            player1score += 1

        if row.count('O') == 3:
            print('Player 2 wins.')
            won = True
            player2score += 1

    # --- COLUMN
    for c in range(3):
        if game_state[0][c] == game_state[1][c] == game_state[2][c] == 'X':
            print('Player 1 wins.')
            won = True
            player1score += 1

        if game_state[0][c] == game_state[1][c] == game_state[2][c] == 'O':
            print('Player 2 wins.')
            won = True
            player2score += 1

    # --- SE DIAGONAL

    if game_state[0][0] == game_state[1][1] == game_state[2][2] == 'X':
        print('Player 1 wins.')
        won = True
        player1score += 1

    if game_state[0][0] == game_state[1][1] == game_state[2][2] == 'O':
        print('Player 2 wins.')
        won = True
        player2score += 1

    # --- SW DIAGONAL

    if game_state[0][2] == game_state[1][1] == game_state[2][0] == 'X':
        print('Player 1 wins.')
        won = True
        player1score += 1

    if game_state[0][2] == game_state[1][1] == game_state[2][0] == 'O':
        print('Player 2 wins.')
        won = True
        player2score += 1

    if not won:
        turn = (3 - turn)
        play(turn)
    else:
        return


print('Welcome to Tic-Tac-Toe!')
display(game_state)
game_state = [[' ' for _ in range(3)] for _ in range(3)]


while True:
    play(turn)

    print(f'The score is {player1score}-{player2score}.')

    inp = input('\nPlay again? (Y/N): ')
    if inp == 'Y':
        game_state = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        display(game_state)
        game_state = [[' ' for _ in range(3)] for _ in range(3)]
        usedNums1, usedNums2 = [], []
        turn = 1

    else:
        print('then die')
        break
