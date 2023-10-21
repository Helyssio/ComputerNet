import socket
import module

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = module.server_addr
port = module.server_port 
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()

# Receive data from the client
data = client_socket.recv(1024)
print(f"Received data: {data.decode()}")
if(data.decode() == "Ping"):
    data = "Pong"
    print(f"Sending data: {data}")
    try: client_socket.send(data.encode())
    except socket.timeout: print("Timeout")

while(True):
    data = client_socket.recv(1024)
    if(data.decode() == "kill"):
        data = "ACK"
        try: client_socket.send(data.encode())
        except: pass
        break
    print(f"Received data: {data.decode()}")
    data = "ACK"
    try: client_socket.send(data.encode())
    except socket.timeout: print("Timeout")

# Close the client socket
client_socket.close()
