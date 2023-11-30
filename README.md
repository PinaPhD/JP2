

### Investigating the dependability of SDN-enabled IoT-Edge networks for next-generation offshore wind farms
#### ABSTRACT



---

#### METHODOLOGY
- On a physical server, three VMs were instantiated such that VM-A hosted $C_1$, VM-B hosted $C_2$, and VM-C hosted $C_3$. The OpenDaylight SDN controller (ODL SDNC) is used in this setup. ODL SDNC has a distributed-flat architecture. This implies that the SDN cluster comprises SDN controllers interacting as peers, unlike the hierarchical architecture where some SDN controllers are masters overseeing agent (or sub-level) controllers.
   
- VM-D is instantiated within the same physical server to run the Mininet network emulator. This network topology remotely connects to VM-A, VM-B, and VM-C using the southbound interface OpenFlow v1.3 protocol. 

- 9 switches are configured in the Mininet network topology and each switch is linked to a primary and backup controller as discussed in the switch redundancy configuration failover mode. 

- Switch and controller failures are introduced in the setup to understand its behavior within a 5-hour mission time. For the sensitivity analysis, one parameter is changed at a time and the impact is measured by observing these metrics: throughput, latency, packet loss, controller response time, and switch failover time. Further, during the fault injection scenarios, the time taken for failover is measured to describe the performance deviation from normal behavior. 


#### PART ONE: SETTING UP THE CONTROLLER CLUSTER - ODL ARGON (ver.18.0)


- sudo apt-get -y update && sudo apt-get -y upgrade
- sudo apt-get -y install unzip
- sudo apt-get -y install openjdk-17-jre OR sudo apt install openjdk-17-jdk
- sudo update-alternatives --config java
- ls -l /etc/alternatives/java
- echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
- source ~/.bashrc
- echo $JAVA_HOME

---
Go to the official OpenDaylight Website and copy the link to Argon (https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.18.2/karaf-0.18.2.tar.gz)

---

curl -XGET -O https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.18.2/karaf-0.18.2.tar.gz

Allow it to download, then unzip it:
 - tar -xvf karaf-0.18.2.tar.gz

- cd karaf-0.18.2/bin/
- ./karaf

---
Now the ODL-Argon is up and running. 
---

Install the relevant features: 

feature:install 
- odl-restconf-all 
- odl-openflowplugin-app-topology 
- odl-openflowplugin-app-topology-manager 
- odl-mdsal-apidocs

---
#### Setting up Containernet
---
- sudo apt install ansible git aptitude -y
- git clone https://github.com/containernet/containernet.git
- cd containernet
- sudo ansible-playbook -i "localhost," -c local install.yml
- sudo python3 examples/containernet_example.py

#### Cite our Work

```bibtex
@article{JP22024,
  title={Investigating the dependability of SDN-enabled IoT-Edge networks for next-generation offshore wind farms},
  author={Mwangi et al., },
  journal={IEEE Transactions of Industrial Informatics},
  year={2024},
  ...
}

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

