#!/usr/bin/env python3

""" 
@Author: Agrippina Mwangi
@Task: Collecting log on network state and resource consumption
"""

from flask import Flask, jsonify
import requests
import csv

app = Flask(__name__)

# Data storage
data_file = 'experiment_data.csv'
fieldnames = ['Time', 'Workload', 'CPU Utilization', 'Memory Utilization', 'Response Time', 'Throughput']

# Initialize CSV file with headers
with open(data_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Function to fetch data from OpenDaylight controller
def get_odl_data():
    odl_url = 'http://your_opendaylight_controller_ip:port/restconf/operational/path/to/data'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Basic YWRtaW46YWRtaW4='}  # Replace with your credentials

    response = requests.get(odl_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from OpenDaylight. Status code: {response.status_code}")

# Endpoint to fetch data from OpenDaylight and store in CSV
@app.route('/collect_data', methods=['POST'])
def collect_data():
    try:
        # Get data from OpenDaylight
        odl_data = get_odl_data()

        # Open CSV file in append mode
        with open(data_file, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write data to CSV
            writer.writerow({
                'Time': odl_data['time'],
                'Workload': odl_data['workload'],
                'CPU Utilization': odl_data['cpu_utilization'],
                'Memory Utilization': odl_data['memory_utilization'],
                'Response Time': odl_data['response_time'],
                'Throughput': odl_data['throughput']
            })

        return jsonify({'message': 'Data received and stored successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
