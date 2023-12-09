from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link

def customTopology():
    net = Mininet(controller=RemoteController, switch=OVSSwitch)

    # Create Controllers
    c1 = net.addController('c1', controller=RemoteController, ip='192.168.16.10', port=6633)
    c2 = net.addController('c2', controller=RemoteController, ip='192.168.16.11', port=6633)
    c3 = net.addController('c3', controller=RemoteController, ip='192.168.16.12', port=6633)

    # Create Switches
    switches = [net.addSwitch('s%d' % n) for n in range(1, 10)]

    # Create Hosts
    LDAQ_hosts = [net.addHost('LDAQ%d' % n) for n in range(1, 4)]
    A_hosts = [net.addHost('A%d' % n) for n in range(1, 4)]
    VPAC_hosts = [net.addHost('VPAC%d' % n) for n in range(1, 4)]
    ECP_hosts = [net.addHost('ECP%d' % n) for n in range(1, 4)]

    # Edge router
    edgeRouter = net.addHost('edgeRouter')

    # Connect Switches in a Ring Topology
    for i in range(8):
        net.addLink(switches[i], switches[i + 1])
    net.addLink(switches[8], switches[0])

    # Connect Hosts to Switches
    for host in LDAQ_hosts:
        net.addLink(switches[0], host)
    for host in A_hosts:
        net.addLink(switches[1], host)
    for host in VPAC_hosts:
        net.addLink(switches[6], host)
    for host in ECP_hosts:
        net.addLink(switches[7], host)

    # Connect edge router to S9
    net.addLink(switches[8], edgeRouter)

    # Connect S3 and S4, S5 and S6
    net.addLink(switches[2], switches[3])
    net.addLink(switches[4], switches[5])

    # Assign Controllers to Switches
    for switch in switches[:3]:
        switch.start([c1])
    for switch in switches[3:6]:
        switch.start([c2])
    for switch in switches[6:]:
        switch.start([c3])

    net.build()
    c1.start()
    c2.start()
    c3.start()

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    customTopology()
