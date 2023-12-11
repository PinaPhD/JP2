  
#### Typical user features
---
* odl-openflowplugin-flow-services-rest               #OF plugin with REST API
* odl-openflowplugin-flow-app-table-miss-enforcer     #Adds default flow to controller
* odl-openflowplugin-nxm-extensions                   #NICIRA extensions for OVS
* odl-openflowplugin-drop-test                        #Test application for pushing flows on packet-in
* odl-openflowplugin-app-bulk-o-matic                 #Test application for pushing bulk flows 

###### Updating the netplan configurations
```bash
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      dhcp4: no
      addresses:
        - 192.168.1.10/24
      gateway4: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
``` 

#### Methodology
- On a physical server, three VMs were instantiated such that VM-A hosted $C_1$, VM-B hosted $C_2$, and VM-C hosted $C_3$. The OpenDaylight SDN controller (ODL SDNC) is used in this setup. ODL SDNC has a distributed-flat architecture. This implies that the SDN cluster comprises SDN controllers interacting as peers, unlike the hierarchical architecture where some SDN controllers are masters overseeing agent (or sub-level) controllers.
   
- VM-D is instantiated within the same physical server to run the Mininet network emulator. This network topology remotely connects to VM-A, VM-B, and VM-C using the southbound interface OpenFlow v1.3 protocol. 

- 9 switches are configured in the Mininet network topology and each switch is linked to a primary and backup controller as discussed in the switch redundancy configuration failover mode. 

- Switch and controller failures are introduced in the setup to understand its behavior within a 5-hour mission time. For the sensitivity analysis, one parameter is changed at a time and the impact is measured by observing these metrics: throughput, latency, packet loss, controller response time, and switch failover time. Further, during the fault injection scenarios, the time taken for failover is measured to describe the performance deviation from normal behavior. 

