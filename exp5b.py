import socket
import threading


def receive_messages(client_socket):
    """Continuously listens for incoming messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("\nDisconnected from server.")
                break
            # Print incoming message without breaking the prompt line
            print(f"\r{message}\n> ", end="", flush=True)
        except Exception:
            break


def chat_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(('localhost', 55555))
        print("Connected to chat server. Type 'exit' to quit.\n")
    except Exception as e:
        print(f"Unable to connect to server: {e}")
        return

    # Background daemon thread to listen for messages
    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client_socket,),
        daemon=True
    )
    receive_thread.start()

    # Main loop for user input
    while True:
        try:
            message = input("> ")
            if message.strip().lower() == "exit":
                break
            if message.strip():  # Avoid sending empty strings
                client_socket.sendall(message.encode('utf-8'))
        except Exception as e:
            print(f"Error sending message: {e}")
            break

    client_socket.close()
    print("Connection closed.")


if __name__ == '__main__':
    chat_client()