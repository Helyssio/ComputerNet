# ComputerNet


servertalk : 
The code is a server-side implementation using Python's socket library. It creates a socket object and binds it to a specified IP address and port.
The server listens for incoming connections and, when a client connects, accepts the connection. The server receives data from the client and handles "Ping" and "kill" requests accordingly.
It sends "Pong" in response to "Ping" and acknowledges other data with "ACK.". The server can be terminated when "kill" is received.

clienttalk : 
The code is a client-side implementation in Python. It creates a socket object and connects to the server specified by server_addr and server_port.
The client sends "Ping" to the server, measures round-trip time, and handles potential timeouts. It reads sensor data from a file for the current day, sending it in chunks to the server.
The connection is terminated by sending "kill" to the server.

module : 
This module provides utility functions for both the client and server codes.
send_to_server(data, socket) sends data to the server via the provided socket, measuring the round-trip time and handling timeouts.
generate_sensor_data() generates sensor data and appends it to a file for the current day.

generate_sensor_data :
This code is a script to generate sensor data using the functions provided in the module : module.
It creates a set of sensor data for the current day, simulating wheel rotation counts.
This data is appended to a file with a name corresponding to the current date.
