import socket
def echo_server():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    print("Server listening on port 65432...")
    connection, client_address = server_socket.accept()
    print(f"Connected by {client_address}")
    while True:
       data = connection.recv(1024)
       if not data:
           break
       print(f"Received: {data.decode()}")
       connection.sendall(data)
    connection.close()
if __name__ == '__main__':
    echo_server()