

## Investigating the dependability of SDN-enabled IoT-Edge networks for next-generation offshore wind farms


<img src="https://github.com/PinaPhD/JP2/blob/main/FrontPage.png" >



## Contributors

1. Agrippina Mwangi (SDN/NFV Solutions Architect and Researcher) - [ResearchGate Profile](https://www.researchgate.net/profile/Agrippina-Mwangi)
2. Nadine Kabbara (IEC61850/vPAC Researcher) - [ResearchGate Profile](https://www.researchgate.net/profile/Nadine-Kabbara)


## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Testbed Design](#Testbed-Design)
3. [Data Plane](#data-plane)
4. [Control Plane](#control-plane)
5. [Dependability Assessment](#Dependability-Assessment)
6. [Cite our Work](#cite-our-work)



## Executive Summary
> Next-generation offshore wind farms are increasingly adopting vendor-agnostic software-defined networking (SDN) to oversee their Industrial Internet of Things Edge (IIoT-Edge) networks. The SDN-enabled IIoT-Edge networks present a promising solution for high availability and consistent performance-demanding environments such as offshore wind farm critical infrastructure monitoring, operation, and maintenance. Inevitably, these networks encounter stochastic failures such as random component malfunctions, software malfunctions, CPU overconsumption, and memory leakages. These stochastic failures result in intermittent network service interruptions, disrupting the real-time exchange of critical, latency-sensitive data essential for offshore wind farm operations. Given the criticality of data transfer in offshore wind farms, this paper investigates the dependability of the SDN-enabled IIoT-Edge networks amid the highlighted stochastic failures using a two-pronged approach to: (i) observe the transient behavior using a proof-of-concept simulation testbed and (ii) quantitatively assess the steady-state behavior using a probabilistic Homogeneous Continuous Time Markov Model (HCTMM) under varying failure and repair conditions. The study finds that network throughput decreases during failures in the transient behavior analysis. After quantitatively analyzing 15 case scenarios with varying failure and repair combinations, steady-state availability ranged from 93% to 98%, nearing the industry-standard SLA of 99.999%, guaranteeing up to 3 years of uninterrupted network service.



## Testbed Design

1. On a physical server, create several Linux-GUI x64 virtual machines using KVM virtual machine manager using the following storage and compute specifications:
    - Linux Ubuntu server 22.04 lts-Gen2 x64, 2 vCPUs (16GiB RAM), 128-512GB SSD/HDD
    - Docker ver. 24.0.7
    - Mininet Ver. 2.3.0
    - InfluxdB Ver.2.7.10
    - Python Ver.3.12.3

    

## Data Plane
- On one of the VMs with Mininet Installation run the [network topology](https://github.com/PinaPhD/JP2/blob/main/Dependability_Assessment/Topology/network_topology.py) for an offshore wind farm as illustrated in the homepage figure (reduce model with 20 WTGs communicating with one OSS).
- At the Mininet prompt, run xterm on select mininet hosts to initialize traffic generation using the following data sets:
    - [MQTT sensor data traffic](https://github.com/PinaPhD/A-threshold-triggered-DQN-self-healing-framework/tree/main/DataPlane/IIoT_ECP_Socket)
    - [IEC61850 SV/GOOSE docker based data traffic](https://github.com/PinaPhD/JP2/tree/main/Dependability_Assessment/vPAC_Node)

- To monitor network performance, use the [iperf3](https://iperf.fr/) tool for active measurements of network latency, throughput, jitter, packet loss (loss of datagrams).


## Control Plane


## Dependability Assessment






---



##### Cite our Work

```bibtex
@ARTICLE{mwangi2024tnsm,
  author={Mwangi, Agrippina and Kabbara, Nadine and Coudray, Patrick and Gryning, Mikkel and Gibescu, Madeleine},
  journal={IEEE Transactions on Network and Service Management}, 
  title={Investigating the Dependability of Software-Defined IIoT-Edge Networks for Next-Generation Offshore Wind Farms}, 
  year={2024},
  volume={5},
  number={6},
  pages={1-14},
  keywords={Wind farms;Sensors;Stochastic processes;Industrial Internet of Things;Wind turbines;Servers;Probabilistic logic;Industrial IoT;software-defined networking;edge computing;IEEE802.1 Time Sensitive Networking;IEC61850;vPAC;Homogeneous CTMM;offshore wind;dependability},
  doi={10.1109/TNSM.2024.3458447}
  }
```


```bibtex
@Article{mwangi2024en,
AUTHOR = {Mwangi, Agrippina and Sahay, Rishikesh and Fumagalli, Elena and Gryning, Mikkel and Gibescu, Madeleine},
TITLE = {Towards a Software-Defined Industrial IoT-Edge Network for Next-Generation Offshore Wind Farms: State of the Art, Resilience, and Self-X Network and Service Management},
JOURNAL = {Energies},
VOLUME = {17},
YEAR = {2024},
NUMBER = {12},
ARTICLE-NUMBER = {2897},
URL = {https://www.mdpi.com/1996-1073/17/12/2897},
ISSN = {1996-1073},
DOI = {10.3390/en17122897}
}
```


```bibtex
@ARTICLE{kabbara2024ojia,
  author={Kabbara, Nadine and Mwangi, Agrippina and Ştefanov, Alexandru and Gibescu, Madeleine},
  journal={IEEE Open Journal of Industry Applications}, 
  title={A Real-Time Implementation and Testing of Virtualized Controllers for Software-Defined IEC 61850 Digital Substations}, 
  year={2024},
  volume={5},
  number={},
  pages={300-310},
  keywords={Substations;IEC Standards;Virtualization;Real-time systems;Communication networks;Protection;Power systems;Cyber-physical power systems;digital substations;IEC 61850;software-defined network (SDN);virtual intelligent electronic devices (IED);virtualization},
  doi={10.1109/OJIA.2024.3426321}}
```


```bibtex
@inproceedings{mwangi2023building,
  title={Building Resilience for SDN-Enabled IoT Networks in Offshore Renewable Energy Supply},
  author={Mwangi, Agrippina and Fumagalli, Elena and Gryning, Mikkel and Gibescu, Madeleine},
  booktitle={2023 IEEE 9th World Forum on Internet of Things (WF-IoT)},
  pages={1--2},
  year={2023},
  organization={IEEE}
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
```

