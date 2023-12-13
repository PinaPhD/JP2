#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mininet.topo import Topo

class sdn_enabled_iot_edge_net (Topo):
    def build(self):
        # Add switches
        info('Adding switches to the SDN-enabled IoT-Edge Network...\n\n')
        s = [self.addSwitch(f's{i}') for i in range(1, 10)]
        
        # Add hosts (MUs, and LDAQs)
        info('Adding MUs, LDAQs, ECP, and vPAC nodes ...\n\n')
        
        mu1 = self.addHost('mu1',  ip='192.168.10.10/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:01')
        mu2 = self.addHost('mu2',  ip='192.168.10.15/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:02')
        mu3 = self.addHost('mu3',  ip='192.168.10.20/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:03')
        mu4 = self.addHost('mu4',  ip='192.168.10.25/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:04')
        mu5 = self.addHost('mu5',  ip='192.168.10.30/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:05')
        ldaq1 = self.addHost('ldaq1',  ip='192.168.10.35/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:06')
        ldaq2 = self.addHost('ldaq2',  ip='192.168.10.40/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:07')
        ldaq3 = self.addHost('ldaq3',  ip='192.168.10.45/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:08')
        ldaq4 = self.addHost('ldaq4',  ip='192.168.10.50/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:09')
        ldaq5 = self.addHost('ldaq5',  ip='192.168.10.55/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:10')
        vpac1 = self.addHost('vpac1',  ip='192.168.10.60/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:11')
        vpac2 = self.addHost('vpac2',  ip='192.168.10.65/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:12')
        vpac3 = self.addHost('vpac3',  ip='192.168.10.70/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:13')
        vpac4 = self.addHost('vpac4',  ip='192.168.10.75/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:14')
        vpac5 = self.addHost('vpac5',  ip='192.168.10.80/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:15')
        ecp1 = self.addHost('ecp1',  ip='192.168.10.85/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:16')
        ecp2 = self.addHost('ecp2',  ip='192.168.10.90/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:17')
        ecp3 = self.addHost('ecp3',  ip='192.168.10.95/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:18')
        ecp4 = self.addHost('ecp4',  ip='192.168.10.100/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:19')
        ecp5 = self.addHost('ecp5',  ip='192.168.10.105/24', defaultRoute='via 192.168.10.254', mac='00:00:00:00:00:20')        
        

        # Add links between switches
        info('Adding links between switches and added properties to mimick a real life network...\n\n')
        self.addLink(s[3], s[2], bw=100, delay='1ms', loss=0, max_queue_size=1000)  # s4 to s3
        self.addLink(s[3], s[4], bw=100, delay='1ms', loss=0, max_queue_size=1000)  # s4 to s5
        self.addLink(s[2], s[5], bw=100, delay='1ms', loss=0, max_queue_size=1000)  # s3 to s6
        self.addLink(s[4], s[5], bw=100, delay='1ms', loss=0, max_queue_size=1000)  # s5 to s6
        self.addLink(s[0], s[3], bw=100, delay='1ms', loss=0, max_queue_size=1000)  # s1 to s4
        self.addLink(s[1], s[2], bw=100, delay='1ms', loss=0, max_queue_size=1000)  # s2 to s3
        self.addLink(s[4], s[6], bw=100, delay='1ms', loss=0, max_queue_size=1000)  # s5 to s7
        self.addLink(s[5], s[7], bw=100, delay='1ms', loss=0, max_queue_size=1000)  # s6 to s8
        self.addLink(s[6], s[8], bw=100, delay='1ms', loss=0, max_queue_size=1000)  # s7 to s9
        self.addLink(s[7], s[8], bw=100, delay='1ms', loss=0, max_queue_size=1000)  # s8 to s9
        self.addLink(s[0], s[1], bw=100, delay='1ms', loss=0, max_queue_size=1000)  # s1 to s2


        # Add links between switches and hosts
        info('Linking Merging Units to the Switches ...\n\n')
        self.addLink(s[0], mu1)  # s1 to mu1
        self.addLink(s[0], mu2)  # s1 to mu2
        self.addLink(s[0], mu3)  # s1 to mu3
        self.addLink(s[1], mu4)  # s2 to mu4
        self.addLink(s[1], mu5)  # s2 to mu5
        
        # Add links between switches and hosts 
        info('Linking Local data acquisition modules (LDAQ) to the Switches ...\n\n')
        self.addLink(s[0], ldaq1)  # s1 to ldaq1
        self.addLink(s[0], ldaq2)  # s1 to ldaq2
        self.addLink(s[0], ldaq3)  # s1 to ldaq3
        self.addLink(s[1], ldaq4)  # s2 to ldaq4
        self.addLink(s[1], ldaq5)  # s2 to ldaq5


        # Add links between switches and hosts 
        info('Linking ECP and vPAC nodes to the switches ...\n\n')
        self.addLink(s[6], vpac1)  # s7 to vpac1
        self.addLink(s[6], vpac2)  # s7 to vpac2
        self.addLink(s[6], ecp1)    # s7 to ecp1
        self.addLink(s[6], ecp2)    # s7 to ecp2
        
        self.addLink(s[7], vpac3)  # s8 to vpac3
        self.addLink(s[7], vpac4)  # s8 to vpac4
        self.addLink(s[7], vpac5)  # s8 to vpac5
        self.addLink(s[7], ecp3)   # s8 to ecp3
        self.addLink(s[7], ecp4)   # s8 to ecp4        
        self.addLink(s[7], ecp5)    # s9 to ecp5
        
        #Then switch S9 connects to the EdgeRouter (Beyond the research work's scope)
      

if __name__ == '__main__':
    setLogLevel('info')

    # Create the topology
    topo = sdn_enabled_iot_edge_net()

    # Define the remote controller
    remoteControllerIP = '192.168.122.120'
    controller = RemoteController('c0', ip=remoteControllerIP, port=6653)

    # Start the network
    net = Mininet(topo=topo, controller=controller, switch=OVSSwitch, link=TCLink)
    net.start()

    # Run CLI
    CLI(net)

    # After the user exits the CLI, stop the network
    net.stop()