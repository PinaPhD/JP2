

### Investigating the dependability of SDN-enabled IoT-Edge networks for next-generation offshore wind farms
#### ABSTRACT


<img src="https://github.com/PinaPhD/JP2/blob/main/ReadMe_Logical.png" width="800" height="500">


---

##### Part 1: Probabilistic quantitative HCTMC system model
[HCTMC Model](https://github.com/PinaPhD/JP2/blob/main/HCTMC_MODEL/hctmc_system_model.sm)


##### Part 2: Proof-of-concept simulation testbed

[Proof Of Concept Simulation Testbed](https://github.com/PinaPhD/JP2/tree/main/POC/)

##### Part 3: Methodology FlowChart
 To begin with, a probabilistic quantitative PRISM®-based HCTMC system model assesses the probability and impact of potential failures. This is followed by a proof-of-concept simulation on a testbed, which examines how these modeled failures affect the network service quality. This systematic analysis gathers crucial insights into the network’s performance under stress, enabling us to propose best practices that would bolster the system’s dependability.

![Methodology](https://github.com/PinaPhD/JP2/blob/main/Methodology.png)

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
