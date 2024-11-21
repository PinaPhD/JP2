

### Investigating the dependability of SDN-enabled IoT-Edge networks for next-generation offshore wind farms

---
<img src="https://github.com/PinaPhD/JP2/blob/main/FrontPage.png" >
---


## Contributors

1. Agrippina Mwangi (SDN/NFV Solutions Architect and Researcher) - [ResearchGate Profile](https://www.researchgate.net/profile/Agrippina-Mwangi)
2. Nadine Kabbara (IEC61850/vPAC Expert and Researcher) - [ResearchGate Profile](https://www.researchgate.net/profile/Nadine-Kabbara)


## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Pre-requisites](#requirements)
3. [Data Plane](#data-plane)
4. [Control Plane](#control-plane)
5. [Dependability Assessment](#Dependability-Assessment)
6. [Cite our Work](#cite-our-work)



## Executive Summary
> Next-generation offshore wind farms are increasingly adopting vendor-agnostic software-defined networking (SDN) to oversee their Industrial Internet of Things Edge (IIoT-Edge) networks. The SDN-enabled IIoT-Edge networks present a promising solution for high availability and consistent performance-demanding environments such as offshore wind farm critical infrastructure monitoring, operation, and maintenance. Inevitably, these networks encounter stochastic failures such as random component malfunctions, software malfunctions, CPU overconsumption, and memory leakages. These stochastic failures result in intermittent network service interruptions, disrupting the real-time exchange of critical, latency-sensitive data essential for offshore wind farm operations. Given the criticality of data transfer in offshore wind farms, this paper investigates the dependability of the SDN-enabled IIoT-Edge networks amid the highlighted stochastic failures using a two-pronged approach to: (i) observe the transient behavior using a proof-of-concept simulation testbed and (ii) quantitatively assess the steady-state behavior using a probabilistic Homogeneous Continuous Time Markov Model (HCTMM) under varying failure and repair conditions. The study finds that network throughput decreases during failures in the transient behavior analysis. After quantitatively analyzing 15 case scenarios with varying failure and repair combinations, steady-state availability ranged from 93\% to 98\%, nearing the industry-standard SLA of 99.999\%, guaranteeing up to 3 years of uninterrupted network service.



## Requirements

1. On a physical server, create several Linux-GUI x64 virtual machines using KVM virtual machine manager using the following storage and compute specifications:
    - Linux Ubuntu server 22.04 lts-Gen2 x64, 2 vCPUs (16GiB RAM), 128-512GB SSD/HDD
    - Docker ver. 24.0.7
    - Mininet Ver. 2.3.0
    - InfluxdB Ver.2.7.10
    - Python Ver.3.12.3
2.     
    

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
@article{To_Be_Updated,
  title={Investigating the dependability of SDN-enabled IoT-Edge networks for next-generation offshore wind farms},
  author={Mwangi et al., },
  journal={IEEE Transactions of Network and Service Management - Submitted},
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
