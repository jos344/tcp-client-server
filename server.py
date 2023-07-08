import socket

HOST = '127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT)) # pass tuple

# start listening for incoming connections
# 5 how many unaccepted connections do we allow before we reject new ones
server.listen(5)

while True:
    # accept every connection that we have
    # server.accept() method listens to incoming clients that wants to connect and returns address of client
    # communication_socket is endpoint on the server
    communication_socket, address = server.accept()
    print(f'Connected to {address}')
    # recv - how many bytes
    message = communication_socket.recv(1024).decode('utf-8')
    print(f'Message from client is: {message}')
    communication_socket.send(f"Got your message! Thank you!".encode("utf-8"))
    communication_socket.close()
    print(f"Connection with {address} ended!")

    





    
    





