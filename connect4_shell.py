# shell_connect4
import connect4
from connect4_share import print_board, get_winner, drop, pop


def board_size() -> tuple:
    'asks for user input to input board size of game'
    while True:
        size = input('What do you want the size of the board to be in cxr format? ')
        size_list = size.split('x')
        if len(size_list) == 2:
            if connect4.MIN_COLUMNS <= int(size_list[0]) <= connect4.MAX_COLUMNS and connect4.MIN_ROWS <= int(
                    size_list[1]) <= connect4.MAX_ROWS:
                game = connect4.new_game(int(size_list[0]), int(size_list[1]))
                return game, size_list
            else:
                print('Game board rows and columns have to be between 4 and 20')
                raise ValueError
        else:
            print('Sorry that is an incorrect format for the size of the game board')
            raise ValueError


def start_game(game_state: connect4.GameState) -> None:
    """Starts the game and prints the turn and board every round
        until game ends"""
    while True:
        try:
            if get_winner(game_state) is not None:
                print(get_winner(game_state))
                break
            move = input('Say whether you want to drop or pop and which column: ')
            move_split = move.split(' ')
            if 'drop' in move:
                game_state = drop(game_state, int(move_split[1]))
            elif 'pop' in move:
                game_state = pop(game_state, int(move_split[1]))
        except IndexError:
            print('That input was not correct, try again')


if __name__ == '__main__':
    game_board = board_size()
    game_state = game_board[0]
    print_board(game_board[0], connect4.columns(game_state))
    start_game(game_board[0])
