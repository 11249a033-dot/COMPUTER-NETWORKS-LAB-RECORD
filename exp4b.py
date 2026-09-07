import socket

def echo_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))

    while True:
        # Get message from the user
        message = input("Enter a message: ")

        # Send the message to the server
        client_socket.sendall(message.encode())

        # Exit if the user types 'exit'
        if message.lower() == 'exit':
            break

        # Receive the echoed message from the server
        data = client_socket.recv(1024)
        print("Echoed from server:", data.decode())

    # Close the socket
    client_socket.close()

if __name__ == '__main__':
    echo_client()