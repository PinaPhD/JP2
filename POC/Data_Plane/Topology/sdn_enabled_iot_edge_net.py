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
        # Function to create hosts
        def create_hosts(prefix, count, switch):
            global last_ip_octet
            for i in range(1, count + 1):
                ip = f'192.168.10.{last_ip_octet}/24'
                host = self.addHost(f'{prefix}{i}', ip=ip)
                self.addLink(switch, host)
                last_ip_octet += 1

        # Add the first set of hosts (mu)
        create_hosts('mu', 5, s[0])

        # Add the second set of hosts (ldaq)
        create_hosts('ldaq', 5, s[0])

        # Add the third set of hosts (vpac)
        create_hosts('vpac', 5, s[6])

        # Add the fourth set of hosts (ecp)
        create_hosts('ecp', 5, s[7])

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
        self.addLink(s[0], mu[0])  # s1 to mu1
        self.addLink(s[0], mu[1])  # s1 to mu2
        self.addLink(s[0], mu[2])  # s1 to mu3
        self.addLink(s[1], mu[3])  # s2 to mu4
        self.addLink(s[1], mu[4])  # s2 to mu5
        self.addLink(s[1], mu[5])  # s2 to mu6
        
        # Add links between switches and hosts 
        info('Linking Local data acquisition modules (LDAQ) to the Switches ...\n\n')
        self.addLink(s[0], ldaq[0])  # s1 to ldaq1
        self.addLink(s[0], ldaq[1])  # s1 to ldaq2
        self.addLink(s[0], ldaq[2])  # s1 to ldaq3
        self.addLink(s[1], ldaq[3])  # s2 to ldaq4
        self.addLink(s[1], ldaq[4])  # s2 to ldaq5
        self.addLink(s[1], ldaq[5])  # s2 to ldaq6


        # Add links between switches and hosts 
        info('Linking ECP and vPAC nodes to the switches ...\n\n')
        self.addLink(s[6], vpac[0])  # s7 to vpac1
        self.addLink(s[6], vpac[1])  # s7 to vpac2
        self.addLink(s[6], ecp[0])    # s7 to ecp1
        self.addLink(s[6], ecp[1])    # s7 to ecp2
        self.addLink(s[7], vpac[2])  # s8 to vpac3
        self.addLink(s[7], vpac[3])  # s8 to vpac4
        self.addLink(s[7], vpac[4])  # s8 to vpac5
        self.addLink(s[7], ecp[2])   # s8 to ecp3
        self.addLink(s[7], ecp[3])   # s8 to ecp4
        self.addLink(s[8], ecp[4])    # s9 to ecp5
      

if __name__ == '__main__':
    setLogLevel('info')

    # Create the topology
    topo = SDNEnabledIoTEdgeNet()

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