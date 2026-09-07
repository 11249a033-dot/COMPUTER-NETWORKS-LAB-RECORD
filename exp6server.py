import socket
import os


def file_transfer_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to a specific address and port
        server_socket.bind(('localhost', 12345))
        # Listen for incoming connections
        server_socket.listen(1)
        print("Server listening on port 12345...")

        # Accept a connection from a client
        connection, client_address = server_socket.accept()
        print(f"Connected by {client_address}")

        try:
            # Receive the file name (first chunk sent by client)
            filename = connection.recv(1024).decode('utf-8')
            if not filename:
                print("No filename received. Closing connection.")
                return

            # Clean filename to prevent path traversal issues
            safe_filename = os.path.basename(filename)
            output_path = f"received_{safe_filename}"
            print(f"Receiving file: {safe_filename}")

            # Open file in binary write mode
            with open(output_path, 'wb') as file:
                while True:
                    data = connection.recv(1024)
                    if not data:
                        break
                    file.write(data)

            print(f"File received and saved as '{output_path}'")

        except Exception as e:
            print(f"Error while receiving data: {e}")
        finally:
            connection.close()

    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()


if __name__ == '__main__':
    file_transfer_server()