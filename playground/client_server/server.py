import socket


def start_server() -> None:
    # Create a socket object
    server_socket = socket.socket(
        # IPv4
        socket.AF_INET,
        # TCP
        socket.SOCK_STREAM,
    )

    # Get local machine name
    host = socket.gethostname()
    port = 9999

    # Bind the socket to the port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()
        print(f"Got a connection from {addr}")

        msg = "Thank you for connecting" + "\r\n"
        client_socket.send(msg.encode("ascii"))

        client_socket.close()


if __name__ == "__main__":
    start_server()
