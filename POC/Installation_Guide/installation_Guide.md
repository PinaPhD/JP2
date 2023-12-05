  
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

