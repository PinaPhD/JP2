
#!/usr/bin/env python3

from mininet.net import Mininet
from mininet.node import Node, Controller, OVSSwitch, OVSKernelSwitch, Host
from mininet.cli import CLI
from mininet.link import Intf, TCLink
from mininet.log import setLogLevel, info
from mininet.node import Node, CPULimitedHost
from mininet.util import irange, dumpNodeConnections
from mininet.topo import Topo
import time
import os


class SDN_Enabled_IoT_Edge_Network(Topo):

        def build(self):
                #Defining the 9 forwarding devices and the gateway router
                info('Adding switches and routers to the SDN-enabled IoT-Edge Network for next generation offshore wind farms \n\n')
                fd1 = self.addSwitch('FD1')
                fd2 = self.addSwitch('FD2')
                fd3 = self.addSwitch('FD3')
                fd4 = self.addSwitch('FD4')
                fd5 = self.addSwitch('FD5')
                fd6 = self.addSwitch('FD6')
                fd7 = self.addSwitch('FD7')
                fd8 = self.addSwitch('FD8')
                fd9 = self.addSwitch('FD9')
                #RG1 = self.addHost('Gateway',cls=LinuxRouter, ip='10.3.4.1/16')
                #RG2 = self.addHost('ISP',cls=LinuxRouter,ip='10.2.4.1/16')
                #RG3 = self.addHost('ENTERPRISE-selfWORK',cls=LinuxRouter,ip='10.2.4.2/16')

                """
                Defining the merging units (MUs) and protection,fault equipment
                """
                info('Adding Merging Units to the AWF Offshore Digital Substation selfwork ... \n\n')
                #Merging Units (MU Hosts)
                mu1 = self.addHost('MU1')
                mu2 = self.addHost('MU2')
                mu3 = self.addHost('MU3')

                ldaq1 = self.addHost('LDAQ1')
                ldaq2 = self.addHost('LDAQ2')
                ldaq3 = self.addHost('LDAQ3')

                #Protection and Fault Recording Equipment (PR and FR Hosts)
                info('Adding Protection and Fault recording equipment to the Onshore Control room ... \n\n')
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


                """
                Adding hosts to the forwarding devices and linking the routers
                """


                #Part 2: The Distribution layer FD links
                info('Linking the distribution layer forwarding devices ... \n\n')
                self.addLink(fd4,fd3)    #LC-LC fiber patch cords at 1Gbps duplex (ODS)
                self.addLink(fd4,fd5)   #A single model subsea optical fiber cable on 2gbps
                self.addLink(fd3,fd6)   #A single model subsea optical fiber cable on 2gbps
                self.addLink(fd5,fd6)    #LC-LC fiber patch cords at 1Gbps duplex (OCR)

                #Linking the distribution layer and the access layer
                self.addLink(fd1,fd4)
                self.addLink(fd2,fd3)
                self.addLink(fd5,fd7)
                self.addLink(fd6,fd8)
                self.addLink(fd7,fd9)
                self.addLink(fd8,fd9)
                self.addLink(fd1,fd2)

                #Part 3: The Access layer FD links - OFFSHORE WIND FARM PICO DATA CENTER
                info('Linking the access layer forwarding devices with their attached nodes or hosts ... \n\n')
                self.addLink(fd1,mu1)
                self.addLink(fd1,mu2)
                self.addLink(fd1,mu3)

                self.addLink(fd2,ldaq1)
                self.addLink(fd2,ldaq2)
                self.addLink(fd2,ldaq3)

                self.addLink(fd7,VPAC1)
                self.addLink(fd7,VPAC2)
                self.addLink(fd7,VPAC3)
                self.addLink(fd7,VPAC4)

                self.addLink(fd8,VPAC5)
                self.addLink(fd8,ECP1)
                self.addLink(fd8,ECP2)
                self.addLink(fd8,ECP3)
                self.addLink(fd8,ECP4)

                info("Linking the gateway to the protection and fault recording devices in the OT onshore control room ... \n\n")
                self.addLink(fd9,ECP5)
                self.addLink(fd9,ECP6)
                self.addLink(fd9,ECP7)

topos = {'sdniotedge': SDN_Enabled_IoT_Edge_Network}
