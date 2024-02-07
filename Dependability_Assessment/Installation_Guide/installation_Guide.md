#### PART ONE: SETTING UP THE CONTROLLER CLUSTER - ODL ARGON (ver.18.0)

```bash
sudo apt-get -y update && sudo apt-get -y upgrade
sudo apt-get -y install unzip
sudo apt-get -y install openjdk-17-jre OR sudo apt install openjdk-17-jdk
sudo update-alternatives --config java
ls -l /etc/alternatives/java
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
source ~/.bashrc
echo $JAVA_HOME
```

##### Go to the official OpenDaylight Website and copy the link to Argon (https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.18.2/karaf-0.18.2.tar.gz)

```bash
curl -XGET -O https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.18.2/karaf-0.18.2.tar.gz
```


Allow it to download, then unzip it:
```bash
tar -xvf karaf-0.18.2.tar.gz
cd karaf-0.18.2/bin/
./karaf
```


###### Now the ODL-Argon is up and running. 


Install the relevant features: 

```bash
feature:install odl-openflowplugin-app-topology odl-openflowplugin-app-topology-manager odl-openflowplugin-drop-test odl-openflowplugin-app-bulk-o-matic odl-openflowplugin-app-table-miss-enforcer odl-openflowplugin-nxm-extensions

feature:install odl-restconf odl-restconf-all odl-mdsal-model-odl-l2-types odl-mdsal-apidocs
 odl-openflowplugin-app-bulk-o-matic odl-openflowplugin-app-table-miss-enforcer odl-openflowplugin-nxm-extensions

```
`feature:install odl-mdsal-apidocs odl-mdsal-model-odl-l2-types odl-openflowplugin-app-arbitratorreconciliation odl-openflowplugin-app-bulk-o-matic odl-openflowplugin-app-config-pusher odl-openflowplugin-app-forwardingrules-manager odl-openflowplugin-app-forwardingrules-sync odl-openflowplugin-app-lldp-speaker odl-openflowplugin-app-reconciliation-framework odl-openflowplugin-app-southbound-cli odl-openflowplugin-app-table-miss-enforcer odl-openflowplugin-app-topology odl-openflowplugin-app-topology-lldp-discovery odl-openflowplugin-app-topology-manager odl-openflowplugin-drop-test odl-openflowplugin-eric-extensions odl-openflowplugin-flow-services odl-openflowplugin-flow-services-rest odl-openflowplugin-libraries odl-openflowplugin-nsf-model odl-openflowplugin-nxm-extensions odl-openflowplugin-onf-extensions odl-openflowplugin-southbound` 

---
  
#### Typical user features

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

