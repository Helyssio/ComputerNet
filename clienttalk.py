import socket
import module
import time

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_host = module.server_addr  # Use the server's IP address
server_port = module.server_port
client_socket.connect((server_host, server_port))
client_socket.settimeout(1) # Set timeout to 1 second

# Send Ping to the server
try:
    rtt = module.send_to_server("Ping", client_socket)
    if(rtt == -1): raise Exception("Timeout")
    else: print(f"Round trip time: {rtt} ms")
except Exception as e:
    print(e)
    client_socket.close()
    exit()

# Read sensor data from file of this day
date = time.strftime("%Y-%m-%d")
f = open(module.data_path + date + ".txt", "r")
lines = f.readlines()
while(len(lines) > 0):
    data = ""
    while(True):
        if(len(lines) > 0 and len(lines[0]) + len(data) < 1024): # 1024 is the maximum size of data that can be sent
            data = data + lines.pop(0)
        else:
            break

    try:
        rtt = module.send_to_server(data, client_socket)
        if(rtt == -1): raise Exception("Timeout")
        else: print(f"Round trip time: {rtt} ms")
    except Exception as e:
        print(e)
        client_socket.close()
        f.close()
        exit()
f.close()

# Send kill to the server to terminate the connection
try:
    rtt = module.send_to_server("kill", client_socket)
    if(rtt == -1): raise Exception("Timeout")
    else: print(f"Round trip time: {rtt} ms")
except Exception as e:
    print(e)
    client_socket.close()
    exit()

# Close the client socket
client_socket.close()
