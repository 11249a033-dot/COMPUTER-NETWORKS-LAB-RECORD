import socket


def file_transfer_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(('localhost', 12345))
        filename = input("Enter the filename to send: ")

        # Open file first to ensure it exists before sending metadata to server
        with open(filename, 'rb') as file:
            # Send the filename first so the server knows what to name the received file
            client_socket.sendall(filename.encode('utf-8'))

            # Wait for server acknowledgment or brief pause before streaming binary content
            print(f"Sending '{filename}'...")

            v  True:
                chunk = file.read(1024)
                if not chunk:
                    break
                client_socket.sendall(chunk)

            print(f"File '{filename}' sent successfully.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found on local machine.")
    except ConnectionRefusedError:
        print("Error: Could not connect to server. Is the receiver running on port 12345?")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()


if __name__ == '__main__':
    file_transfer_client()