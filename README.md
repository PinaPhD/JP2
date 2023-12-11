

### Investigating the dependability of SDN-enabled IoT-Edge networks for next-generation offshore wind farms
#### ABSTRACT


<img src="https://github.com/PinaPhD/JP2/blob/main/ReadMe_Logical.png" width="700" height="400">


#### METHODOLOGY

##### Part 1: Probabilistic quantitative HCTMC system model
[HCTMC Model](https://github.com/PinaPhD/JP2/blob/main/HCTMC_MODEL/hctmc_system_model.sm)


##### Part 2: Proof-of-concept simulation testbed

[proof-of-concept](https://github.com/PinaPhD/JP2/tree/main/POC/)

- On a physical server, three VMs were instantiated such that VM-A hosted $C_1$, VM-B hosted $C_2$, and VM-C hosted $C_3$. The OpenDaylight SDN controller (ODL SDNC) is used in this setup. ODL SDNC has a distributed-flat architecture. This implies that the SDN cluster comprises SDN controllers interacting as peers, unlike the hierarchical architecture where some SDN controllers are masters overseeing agent (or sub-level) controllers.
   
- VM-D is instantiated within the same physical server to run the Mininet network emulator. This network topology remotely connects to VM-A, VM-B, and VM-C using the southbound interface OpenFlow v1.3 protocol. 

- 9 switches are configured in the Mininet network topology and each switch is linked to a primary and backup controller as discussed in the switch redundancy configuration failover mode. 

- Switch and controller failures are introduced in the setup to understand its behavior within a 5-hour mission time. For the sensitivity analysis, one parameter is changed at a time and the impact is measured by observing these metrics: throughput, latency, packet loss, controller response time, and switch failover time. Further, during the fault injection scenarios, the time taken for failover is measured to describe the performance deviation from normal behavior. 


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


#### Setting up Containernet

```bash
sudo apt install ansible git aptitude -y
git clone https://github.com/containernet/containernet.git
cd containernet
sudo ansible-playbook -i "localhost," -c local install.yml
sudo python3 examples/containernet_example.py
```


#### Cite our Work

```bibtex
@article{JP22024,
  title={Investigating the dependability of SDN-enabled IoT-Edge networks for next-generation offshore wind farms},
  author={Mwangi et al., },
  journal={IEEE Transactions of Industrial Informatics},
  year={2024},
  ...
}
```

```bibtex
@inproceedings{mwangi2023system,
  title={A system-based framework for optimal sensor placement in smart grids},
  author={Mwangi, Agrippina and Sundsgaard, Konrad and Vilaplana, Jose Angel Leiva and Viler{\'a}, Kaio Vin{\'\i}cius and Yang, Guangya},
  booktitle={2023 IEEE Belgrade PowerTech},
  pages={1--6},
  year={2023},
  organization={IEEE}
}

@inproceedings{kabbara2023specifications,
  title={Specifications of a Simulation Framework for Virtualized Intelligent Electronic Devices in Smart Grids Covering Networking and Security Requirements},
  author={Kabbara, Nadine and Mwangi, Agrippina and Gibescu, Madeleine and Abedi, Ali and Stefanov, Alexandru and Palensky, Peter},
  booktitle={2023 IEEE Belgrade PowerTech},
  pages={1--6},
  year={2023},
  organization={IEEE}
}

```
