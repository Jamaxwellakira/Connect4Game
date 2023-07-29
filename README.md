# Connect4Game
a Python-shell-based game that you will initially be able to play on your own computer, but will extend so that you can play via the Internet by connecting to a central, shared server.
One of two programs will allow you to play one game of Connect Four using only Python shell interaction (i.e., no networks or sockets). The user will need to specify the size of the board, after which the game begins. The user is repeatedly shown the current state of the game — whose turn it is and what the board looks like.
The second program will instead allow you to play a game of Connect Four via a network, by connecting to a server that I've provided. Your program always acts as a client.
When the second program starts, the user will need to specify the host (circinus-32.ics.uci.edu), along with the port(4444).
Additionally, the user should be asked to specify a username. The username can be anything the user would like, except it cannot contain whitespace characters (e.g., spaces or tabs). So, for example, boo or HappyTonight are legitimate usernames, but Hello There is not.
Once the user has specified where to connect, the program should attempt to connect to the server. If the connection is unsuccessful, print an error message specifying why and end the program. If, on the other hand, the connection is successful, the game should proceed, with the client acting as the red player (and moving first) and the server — which acts as an artificial intelligence — acting as the yellow player. (Of course, the user will need to specify the size of board before the game starts.) For red player moves, 
the user should specify the move at the Python shell, as in your first program; for yellow player moves, the program should instead communicate with the server and let the server determine what move should be made.
As in the first program, the game proceeds, one move at a time, until the game ends, at which point the program ends.
