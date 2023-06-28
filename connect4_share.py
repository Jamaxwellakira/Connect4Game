import connect4


# consists of the functions that are the same in both user interfaces.
# Examples would include a function that prints the current game board to the Python shell
# and a function that asks the user what move he or she would like to make next.


def drop(game_state: connect4.GameState, column: int) -> connect4.GameState:
    """drops a piece down the states column"""
    try:
        game_state = connect4.drop(game_state, column - 1)
        print_board(game_state, connect4.columns(game_state))
    except ValueError:
        print("That column doesn't exist, please choose another column")
    except connect4.InvalidMoveError:
        print('That column is full, please choose another column')
    except connect4.GameOverError:
        print('The game is over, you cannot make another move')
    finally:
        return game_state


def pop(game_state: connect4.GameState, column: int) -> connect4.GameState:
    """pops a piece down the states column"""
    try:
        game_state = connect4.pop(game_state, column - 1)
        print_board(game_state, connect4.columns(game_state))
    except ValueError:
        print("That column doesn't exist, please choose another column")
    except connect4.GameOverError:
        print('The game is over, you cannot make another move')
    except connect4.InvalidMoveError:
        print('That column is empty or does not have one of your pieces, please choose another column')
    finally:
        return game_state


def get_winner(game_state: connect4.GameState) -> str:
    """Gets the winner of the game once there is one"""
    if connect4.winner(game_state) != connect4.EMPTY:
        get_win = connect4.winner(game_state)
        if get_win == connect4.RED:
            return 'Red Won'
        elif get_win == connect4.YELLOW:
            return 'Yellow Won'
        else:
            return None


def print_board(game_state: connect4.GameState, column: int, started=True) -> None:
    """Prints game board"""
    game = game_state
    game_board = game[0]
    for num in range(1, column):
        if num >= 9:
            print(num, end=' ')
        else:
            print(num, end='  ')
    print(column)
    i = 0
    while i < connect4.rows(game_state):
        j = 0
        while j < connect4.columns(game_state):
            if game_board[j][i] == connect4.EMPTY:
                print('.', end='  ')
            elif game_board[j][i] == connect4.RED:
                print('R', end='  ')
            elif game_board[j][i] == connect4.YELLOW:
                print('Y', end='  ')
            j += 1
        i += 1
        print()
