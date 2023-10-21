import time
import random

server_addr = '127.0.0.1' # Loopback address
server_port = 5000
data_path = "./sensor_data/"
rang = 100

def send_to_server(data, socket):
    # Send data to the server
    try:
        start = time.time()
        print(f"Sending data: {data}")
        socket.send(data.encode())

        # Receive data from the server
        data = socket.recv(1024)
        end = time.time()
        print(f"Received data: {data.decode()}")
        return (end - start)*1000
    except socket.timeout:
        print("Timeout")
        return -1

def generate_sensor_data():
    date = time.strftime("%Y-%m-%d")
    f = open(data_path + date + ".txt", "a")
    f.truncate(0)
    f.write('Timestamp, Wheel Rotation Count')

    count = random.randint(0,100)
    for i in range(0,rang):
        count = count + random.randint(0,5)
        f.write('\n' + date + " " + time.strftime("%H:%M:") + f'{i:02d}' + ', ' + count.__str__())
    f.close()