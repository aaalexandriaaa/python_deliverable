from functools import reduce
#  https://git.generalassemb.ly/SEI-CC/SEI-CC-8/blob/master/work/w08/d1/02-py-pac-poe-lab%20(optional)/py-pac-poe-lab.md

# Win Combo Array
win_combos = [
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [3, 4, 5],
    [6, 7, 8]
]

# welcome message
print(' ---------------------- \n Let us play Py-Pac-Poe! \n ----------------------')

# initialize the board array
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
choices = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']

# set up function to ouput player board choices
def output_char(idx):
    if board[idx] == 0:
        return ' '
    elif board[idx] == -1:
        return 'X'
    else:
        return 'O'

# print out current board 
print(f'    A   B   C \n 1) {output_char(0)} | {output_char(1)} | {output_char(2)}\n 2) {output_char(3)} | {output_char(4)} | {output_char(5)}\n 3) {output_char(6)} | {output_char(7)} | {output_char(8)}')

# initialize player turn
player = -1
print("It's X's turn!" if player == -1 else "It's O's turn!")

# input player choice
def handle_player_input():
    global player, win_combos
    player_choice = input(f'Make your move (example B2): ')
    if player_choice[0] in ("ABCabc") and player_choice[1] in "123":
        print("GOOD JOB")
        player_choice_column = player_choice[0].lower()
        player_choice_row = int(player_choice[1])
        # print(player_choice_column, player_choice_row)
        # print("It's X's turn!" if player == -1 else "It's O's turn!")
        player *= -1
        # print("It's X's turn!" if player == -1 else "It's O's turn!")
        # win state function
        for arr in win_combos:
            arr_total = 0
            for char in arr:
                arr_total += board[char]
            if abs(arr_total) == 3:
                print("WIN CONDITION MET")
    else:
        print(f'invalid move. please enter your input in the form of A3')
        handle_player_input()

handle_player_input()