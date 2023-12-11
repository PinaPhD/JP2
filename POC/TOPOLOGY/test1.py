from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.topo import Topo

class SimpleSDNTopo(Topo):
    def build(self):
        # Creating switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # Creating hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Adding links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, h3)
        self.addLink(s4, h4)

def run_topology():
    setLogLevel('info')
    topo = SimpleSDNTopo()

    # Connect to a remote controller
    net = Mininet(topo=topo, controller=None)  # Disable the default controller
    remoteControllerIP = '192.168.16.30'  # Replace with your controller's IP
    remoteControllerPort = 6653  # controller's port, typically 6653
    net.addController('c0', controller=RemoteController, ip=remoteControllerIP, port=remoteControllerPort)

    net.start()

    # Running the MQTT publish script on each host
    script_map = {
		'h1': 'python3 /home/odl-sdnc/JP2/POC/ECP_Node/PUB/LDAQ_MQTT.py &', 
		'h2': 'python3 /home/odl-sdnc/JP2/POC/ECP_Node/SUB/ECP_MQTT.py &'
		}

    for host in net.hosts:
        if host.name in script_map:
            host.cmd(script_map[host.name])
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    run_topology()
