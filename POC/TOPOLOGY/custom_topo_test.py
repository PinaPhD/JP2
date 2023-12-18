from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

def customTopology():
    net = Mininet(controller=RemoteController, switch=OVSSwitch, link=TCLink)

    # Add controllers
    c0 = net.addController('c0', controller=RemoteController, ip='IP_OF_PRIMARY_CONTROLLER')
    c1 = net.addController('c1', controller=RemoteController, ip='IP_OF_SECONDARY_CONTROLLER_1')
    c2 = net.addController('c2', controller=RemoteController, ip='IP_OF_SECONDARY_CONTROLLER_2')

    # Add switches
    switches = [net.addSwitch('s%d' % n) for n in range(1, 10)]

    # Add hosts
    inputHosts = [net.addHost(name) for name in ['mu1', 'mu2', 'mu3', 'mu4', 'mu5', 'ldaq1', 'ldaq2', 'ldaq3', 'ldaq4', 'ldaq5']]
    outputHosts = [net.addHost(name) for name in ['ecp1', 'ecp2', 'ecp3', 'ecp4', 'ecp5', 'vpac1', 'vpac2', 'vpac3', 'vpac4', 'vpac5']]

    # Add links (Switch to Switch and Host to Switch)
    # This part should be customized based on your redundancy requirements and topology layout
    for i in range(len(switches)-1):
        net.addLink(switches[i], switches[i+1])

    # Example of linking hosts to switches
    for host in inputHosts:
        net.addLink(host, switches[0])

    for host in outputHosts:
        net.addLink(host, switches[-1])

    # Start the network
    net.build()
    for controller in [c0, c1, c2]:
        controller.start()
    for switch in switches:
        switch.start([c0, c1, c2])

    # Run CLI
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    customTopology()
