#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.log import SetLogLevel, info
from mininet.cli import CLI
from mininet.topo import Topo


SetLogLevel( 'info' )


#Configure the 2-controller cluster
c0 = RemoteController('c0',ip='192.168.122.120',port=6653)
c1 = RemoteController('c1',ip='192.168.122.121',port=6653)
c2 = RemoteController('c2',ip='192.168.122.122',port=6653)

#Creating a link to the Edge Router
class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    # pylint: disable=arguments-differ
    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()

  

#Creating the network topology
class sdnnet( Topo ):
    def build( self, **_opts ):

        defaultIP = '192.168.1.1/24'  # IP address for r0-eth1
        edge_router = self.addNode( 'r0', cls=LinuxRouter, ip=defaultIP )
        
          
        #Creating and adding hosts to the topology
        m1 = self.addHost('m1', ip='10.0.1.10/24', defaultRoute='via 10.0.1.1')
        m2 = self.addHost('m2', ip='10.0.1.11/24', defaultRoute='via 10.0.1.1')
        m3 = self.addHost('m3', ip='10.0.1.12/24', defaultRoute='via 10.0.1.1')
        m4 = self.addHost('m4', ip='10.0.1.13/24', defaultRoute='via 10.0.1.1')
        m5 = self.addHost('m5', ip='10.0.1.14/24', defaultRoute='via 10.0.1.1')
        
        q1 = self.addHost('q1', ip='10.0.2.20/24', defaultRoute='via 10.0.2.1')
        q2 = self.addHost('q2', ip='10.0.2.21/24', defaultRoute='via 10.0.2.1')
        q3 = self.addHost('q3', ip='10.0.2.22/24', defaultRoute='via 10.0.2.1')
        q4 = self.addHost('q4', ip='10.0.2.23/24', defaultRoute='via 10.0.2.1')
        q5 = self.addHost('q5', ip='10.0.2.24/24', defaultRoute='via 10.0.2.1')
        
        e1 = self.addHost('e1', ip='10.0.3.20/24', defaultRoute='via 10.0.3.1')
        e2 = self.addHost('e2', ip='10.0.3.31/24', defaultRoute='via 10.0.3.1')
        e3 = self.addHost('e3', ip='10.0.3.32/24', defaultRoute='via 10.0.3.1')
        e4 = self.addHost('e4', ip='10.0.3.33/24', defaultRoute='via 10.0.3.1')
        e5 = self.addHost('e5', ip='10.0.3.34/24', defaultRoute='via 10.0.3.1')
        
        v1 = self.addHost('v1', ip='10.0.4.40/24', defaultRoute='via 10.0.4.1')
        v2 = self.addHost('v2', ip='10.0.4.41/24', defaultRoute='via 10.0.4.1')
        v3 = self.addHost('v3', ip='10.0.4.42/24', defaultRoute='via 10.0.4.1')
        v4 = self.addHost('v4', ip='10.0.4.43/24', defaultRoute='via 10.0.4.1')
        v5 = self.addHost('v5', ip='10.0.4.44/24', defaultRoute='via 10.0.4.1')
        
        
        #creating the ethernet switch network
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        
        
        #Linking the switches to each other
        self.addLink(s1,s2)
        self.addLink(s1,s3)
        self.addLink(s2,s4)
        self.addLink(s4,s5)
        self.addLink(s6,s7)
        self.addLink(s5,s6)
        self.addLink(s3,s6)
        self.addLink(s7,s8)
        self.addLink(s5,s9)
        self.addLink(s8,s9)
        
        #Linking the switches to hosts
        self.addLink(m1,s1)
        self.addLink(m2,s1)
        self.addLink(m3,s2)
        self.addLink(m4,s1)
        self.addLink(m5,s2)
        
        self.addLink(q1,s1)
        self.addLink(q2,s1)
        self.addLink(q3,s2)
        self.addLink(q4,s1)
        self.addLink(q5,s2)
        
        self.addLink(e1,s7)
        self.addLink(e2,s7)
        self.addLink(e3,s8)
        self.addLink(e4,s8)
        self.addLink(e5,s8)
        
        self.addLink(v1,s7)
        self.addLink(v2,s7)
        self.addLink(v3,s8)
        self.addLink(v4,s8)
        self.addLink(v5,s8)
        
        #Linking the last switch to the edge router
        self.addLink( s9, edge_router, intfName2='r0-eth1', params2={ 'ip' : defaultIP})
        

    def run():
        topo = NetworkTopo()
        net = Mininet( topo=topo, controller=RemoteController, waitConnected=True)    
        #connects to the three controllers
        
        net.start()
        info( '*** Routing Table on Router:\n' )
        info( net[ 'r0' ].cmd( 'route' ) )
        CLI( net )
        net.stop()
        
if __name__ == '__main__':
    setLogLevel( 'info' )
    run()