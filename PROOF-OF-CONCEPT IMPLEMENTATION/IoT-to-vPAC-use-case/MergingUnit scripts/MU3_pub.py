#!/usr/bin/env python3
import socket
import time
import random

# Sender host's IP address and port
sender_ip = "10.0.0.5"
sender_port = 3546

# Receiver host's IP address and port
print("MERGING UNIT SENDING SV STREAMS TO THE ONSHORE CONTROL ROOM PAC DEVICES")
receiver_ip = "10.0.0.16"
receiver_port = 3540

# Create a socket for sending data
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create random CT and VT data
def generate_data():
    data_points = []
    for _ in range(80):
        current = random.uniform(0.0, 100.0)  # Simulated current value (0 to 100 A)
        voltage = random.uniform(200.0, 250.0)  # Simulated voltage value (200 to 250 V)
        data_points.append(f"Current: {current} A, Voltage: {voltage} V")
    return data_points

try:
    while True:
        # Generate 80 random CT and VT data points
        data_points = generate_data()

        # Create a data packet with all data points
        data_packet = "\n".join(data_points)

        # Send the data to the receiver
        sender_socket.sendto(data_packet.encode(), (receiver_ip, receiver_port))

        # Sleep to maintain the desired sample rate (80 data points every 20ms)
        time.sleep(0.02)

except KeyboardInterrupt:
    print("Stopping the sender...")
finally:
    sender_socket.close()

