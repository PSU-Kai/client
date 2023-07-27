import socket

def start_client(host, port):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    while True:
        message = input("Enter a message (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        # Send the message to the server
        client_socket.sendall(message.encode('utf-8'))

        # Receive the echoed message from the server
        echoed_message = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {echoed_message}")

    # Close the connection with the server
    client_socket.close()

if __name__ == "__main__":
    # Replace 'server_public_ip' with the public IP address of the server
    HOST = '131.252.223.181'
    PORT = 8090       # Use the same port number as in the server
    start_client(HOST, PORT)
