import socket

connect4_socket = socket.socket()


def connect_server(sock: tuple) -> None:
    connect_address = (sock[0], sock[1])
    connect4_socket.connect(connect_address)


def write_to_socket(write: str) -> None:
    output_stream = connect4_socket.makefile('w')
    output_stream.write(write)
    output_stream.flush()


def read_socket() -> str:
    input_stream = connect4_socket.makefile('r')
    return input_stream.readline() + '\r\n'


def close_socket() -> None:
    connect4_socket.makefile('w').close()
    connect4_socket.makefile('r').close()
