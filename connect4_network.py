from connect4_shell import board_size
import connect4_share
import connect4_socket
import connect4


def connect() -> None:
    """connects to server based on user input"""
    while True:
        try:
            host = input('What is the host you are trying to connect to?: ')
            socket = input('What is the socket of the host you are trying to connect to?: ')
            connect4_socket.connect_server((host, int(socket)))
            hello_message()
            connect4_socket.close_socket()
            break
        except ValueError:
            break


def hello_message() -> None:
    """send the hello message to the server"""
    while True:
        try:
            username = input('Write your username: ')
        except ' ' in username:
            print('Your username cannot have a space, try again')
        finally:
            connect4_socket.write_to_socket('I32CFSP_HELLO ' + username + '\r\n')
            print(connect4_socket.read_socket())
            ai_start_game()
            break


def ai_start_game() -> None:
    ai_game_board = board_size()  # gets board size
    ai_board = ai_game_board[1]  # gets the tuple of cxr
    new_game = connect4.new_game(int(ai_board[0]), int(ai_board[1]))  # new game board
    connect4_share.print_board(new_game, connect4.columns(new_game))  # prints the board
    connect4_socket.write_to_socket(
        'AI_GAME ' + ai_board[0] + ' ' + ai_board[1] + '\r\n')  # writes to socket to start game
    print(connect4_socket.read_socket())  # gets socket input
    while True:
        if connect4_share.get_winner(new_game) is not None:
            print(connect4_share.get_winner(new_game))
            break
        try:
            if new_game.turn == connect4.RED:
                move = input('Say whether you want to drop or pop and which column: ')
                move_split = move.split(' ')
                if move_split[0] == 'drop':
                    connect4_socket.write_to_socket(move.upper() + '\r\n')
                    new_game = connect4_share.drop(new_game, int(move_split[1]))
                    connect4_share.print_board(new_game, connect4.columns(new_game))
                    print(connect4_socket.read_socket())
                if move_split[0] == 'pop':
                    connect4_socket.write_to_socket(move.upper() + '\r\n')
                    new_game = connect4_share.pop(new_game, int(move_split[1]))
                    connect4_share.print_board(new_game, connect4.columns(new_game))
                    print(connect4_socket.read_socket())
            elif new_game.turn == connect4.YELLOW:
                server_move = connect4_socket.read_socket()
                print(server_move)
                server_split = server_move.split(' ')
                if server_split[0] == 'DROP':
                    new_game = connect4_share.drop(new_game, int(server_split[1]))
                if server_split[0] == 'POP':
                    new_game = connect4_share.pop(new_game, int(server_split[1]))
        except IndexError:
            print('That input was not correct, try again')


if __name__ == '__main__':
    connect()
