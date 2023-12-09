#!/usr/bin/env python3

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topo import Topo

class SDN_Enabled_IoT_Edge_Network(Topo):

    def build(self):
        # Add switches
        fd1 = self.addSwitch('FD1')
        fd2 = self.addSwitch('FD2')
        fd3 = self.addSwitch('FD3')
        fd4 = self.addSwitch('FD4')
        fd5 = self.addSwitch('FD5')
        fd6 = self.addSwitch('FD6')
        fd7 = self.addSwitch('FD7')
        fd8 = self.addSwitch('FD8')
        fd9 = self.addSwitch('FD9')

        # Add hosts
        mu1 = self.addHost('MU1')
        mu2 = self.addHost('MU2')
        mu3 = self.addHost('MU3')
        ldaq1 = self.addHost('LDAQ1')
        ldaq2 = self.addHost('LDAQ2')
        ldaq3 = self.addHost('LDAQ3')
        ECP1 = self.addHost('ECP1')
        ECP2 = self.addHost('ECP2')
        VPAC1 = self.addHost('VPAC1')
        VPAC2 = self.addHost('VPAC2')
        VPAC3 = self.addHost('VPAC3')
        VPAC4 = self.addHost('VPAC4')
        VPAC5 = self.addHost('VPAC5')
        ECP3 = self.addHost('ECP3')
        ECP4 = self.addHost('ECP4')
        ECP5 = self.addHost('ECP5')
        ECP6 = self.addHost('ECP6')
        ECP7 = self.addHost('ECP7')

        # Add links
        self.addLink(fd4, fd3)
        self.addLink(fd4, fd5)
        self.addLink(fd3, fd6)
        self.addLink(fd5, fd6)
        self.addLink(fd1, fd4)
        self.addLink(fd2, fd3)
        self.addLink(fd5, fd7)
        self.addLink(fd6, fd8)
        self.addLink(fd7, fd9)
        self.addLink(fd8, fd9)
        self.addLink(fd1, fd2)
        self.addLink(fd1, mu1)
        self.addLink(fd1, mu2)
        self.addLink(fd1, mu3)
        self.addLink(fd2, ldaq1)
        self.addLink(fd2, ldaq2)
        self.addLink(fd2, ldaq3)
        self.addLink(fd7, VPAC1)
        self.addLink(fd7, VPAC2)
        self.addLink(fd7, VPAC3)
        self.addLink(fd7, VPAC4)
        self.addLink(fd8, VPAC5)
        self.addLink(fd8, ECP1)
        self.addLink(fd8, ECP2)
        self.addLink(fd8, ECP3)
        self.addLink(fd8, ECP4)
        self.addLink(fd9, ECP5)
        self.addLink(fd9, ECP6)
        self.addLink(fd9, ECP7)

def main():
    topo = SDN_Enabled_IoT_Edge_Network()
    net = Mininet(topo=topo, controller=None)
    net.addController('c0', controller=RemoteController, ip='192.168.16.10', port=6653)

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    main()
