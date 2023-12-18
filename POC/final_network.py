#!/usr/bin/env python

"""
Create the SDN-enabled IoT-Edge network, and run the CLI on it.
"""

import threading
import time
import csv
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import OVSSwitch
from mininet.topolib import TreeNet
from mininet.examples.treeping64 import HostV4
from mininet.util import quietRun

def measure_throughput(network, src, dst, duration=10):
    # Start iperf server on the destination
    server_cmd = 'iperf -s -u &'
    network.get(dst).cmd(server_cmd)

    # Run iperf client on the source
    client_cmd = 'iperf -u -t %d -c %s' % (duration, network.get(dst).IP())
    result = network.get(src).cmd(client_cmd)

    # Parse result for throughput
    throughput = parse_iperf_output(result)
    return throughput

def measure_latency_and_jitter(network, src, dst, count=10):
    # Run ping command
    ping_cmd = 'ping -c %d %s' % (count, network.get(dst).IP())
    result = network.get(src).cmd(ping_cmd)

    # Parse result for latency and jitter
    latency, jitter = parse_ping_output(result)
    return latency, jitter

def parse_iperf_output(output):
    # Implement parsing logic here
    return throughput

def parse_ping_output(output):
    # Implement parsing logic here
    return latency, jitter

def collect_qos_metrics(network, interval=30, output_file='qos_metrics.csv'):
    headers = ['Time', 'Bandwidth', 'Throughput', 'Latency', 'RTT', 'Jitter']
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        while True:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            # Example: Modify with actual source and destination
            src, dst = 'h1', 'h2'

            # Collect metrics
            throughput = measure_throughput(network, src, dst)
            latency, jitter = measure_latency_and_jitter(network, src, dst)
            bandwidth = 'N/A'  # Placeholder for bandwidth calculation
            rtt = latency * 2  # Simplified RTT calculation

            # Write metrics to CSV
            writer.writerow([current_time, bandwidth, throughput, latency, rtt, jitter])
            time.sleep(interval)

if __name__ == '__main__':
    setLogLevel('info')
    network = TreeNet(depth=4, fanout=3, host=HostV4, switch=OVSSwitch, waitConnected=True)

    # Start the QoS metric collection in a separate thread
    qos_thread = threading.Thread(target=collect_qos_metrics, args=(network,))
    qos_thread.daemon = True
    qos_thread.start()

    # Start the Mininet CLI
    network.run(CLI, network)
