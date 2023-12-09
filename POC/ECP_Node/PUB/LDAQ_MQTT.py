#!/usr/bin/python

import paho.mqtt.publish as publish
import time
import random
import threading


MQTT_BROKER = "localhost"  # Change this to the IP of your MQTT broker if it's not local
MQTT_PORT = 1883


# MQTT Topics for Wind Turbine (WT) parameters with 50Hz sampling rate
WT_topics = [
    "WT/Temp/GearOil",
    "WT/Temp/GearBearing",
    "WT/Temp/Generator",
    "WT/Temp/Nacelle",
    "WT/Temp/Ambient",
    "WT/TowerVibration/XY",
    "WT/ShaftDisplacement/Vertical",
    "WT/ShaftDisplacement/Horizontal",
    "WT/PitchPosition",
    "WT/RotorSpeed",
    "WT/GeneratorSpeed",
    "WT/WindSpeed",
    "WT/YawingDirection"
]

# Additional MQTT Topics for parameters with 20kHz sampling rate
high_freq_topics = [
    "WT/EC/Va", "WT/EC/Vb","WT/EC/Vc",
    "WT/EC/Ia","WT/EC/Ib","WT/EC/Ic",
    "WT/Vibration",
    "WT/Displacement"
]

# Combine all topics into one list if needed
all_topics = WT_topics + high_freq_topics

# Function to generate random data for each sensor type
def generate_sensor_data(sensor_type):
    # Assuming the range of sensor readings is 0-100 for simplicity
    # You should modify these ranges according to the actual sensor specifications
    if "Temp" in sensor_type:
        return random.uniform(-50, 150)  # Example range for temperature
    elif "Vibration" in sensor_type or "ShaftDisplacement" in sensor_type:
        return random.uniform(0, 10)  # Example range for vibration or displacement
    elif "PitchPosition" in sensor_type or "YawingDirection" in sensor_type:
        return random.uniform(0, 360)  # Example range for pitch position or yawing direction
    elif "Speed" in sensor_type:
        return random.uniform(0, 2000)  # Example range for speed
    elif "Voltage" in sensor_type or "Current" in sensor_type:
        return random.uniform(0, 1000)  # Example range for voltage or current
    else:
        return random.uniform(0, 100)  # Default range for any other sensor type


def publish_50Hz_data():
    try:
        while True:  # Start an infinite loop
            for topic in WT_topics:
                # Generate a random message or use a sensor reading
                value=generate_sensor_data()
                publish.single(topic, message, hostname=MQTT_BROKER, port=MQTT_PORT)
 	    #Sending the sensor data every 20ms 
	    time.sleep(0.02)  
    except KeyboardInterrupt:
        print("Publishing stopped by user")

def publish_20kHz_data():
    while True:
        for topic in high_freq_topics:
            value = generate_random_value()
            publish.single(topic, value, hostname=MQTT_BROKER, port=MQTT_PORT)
        #Sending the sensor data every 50 microseconds
	time.sleep(0.00005)  

# Set up threads for publishing
def start_publishing():
    thread_50Hz = threading.Thread(target=publish_50Hz_data)
    thread_20kHz = threading.Thread(target=publish_20kHz_data)

    thread_50Hz.start()
    thread_20kHz.start()

    thread_50Hz.join()
    thread_20kHz.join()

# Run the publish function
if __name__ == '__main__':
    try:
        start_publishing()
    except KeyboardInterrupt:
        print("Publishing stopped by IoT Subscriber.")

