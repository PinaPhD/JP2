#!/usr/bin/env python3
import socket

# Receiver host's IP address and port
receiver_ip = "10.0.0.15"
receiver_port = 3540

# Create a socket for receiving data
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the specified address and port
receiver_socket.bind((receiver_ip, receiver_port))

try:
    while True:
        # Receive data from the sender
        data, sender_address = receiver_socket.recvfrom(1024)

        # Process and print the received data
        print(f"Received data from {sender_address}: {data.decode()}")

except KeyboardInterrupt:
    print("Stopping the receiver...")
finally:
    receiver_socket.close()

