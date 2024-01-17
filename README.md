

### Investigating the dependability of SDN-enabled IoT-Edge networks for next-generation offshore wind farms

---

#### ABSTRACT

Offshore wind farms are increasingly adopting
vendor-agnostic software-defined networking (SDN) to oversee
their IoT-Edge networks. Given the challenging offshore context,
it is essential to ensure consistent data exchange in the proposed
SDN-enabled IoT-Edge networks, despite stochastic failures such
as random component malfunction, software glitches, fluctuating
resource usage, and inconsistent network traffic. This paper
demonstrates how these failures occurring in both the control and
data planes result in intermittent network service disruptions.
Further, the paper proposes an effective recoverability and
maintainability strategy and evaluates the proposed network’s
steady-state behavior using a probabilistic Homogeneous Con-
tinuous Time Markov Model (HCTMM). The HCTMM, tested
across 15 scenarios with varied failure-repair rates, shows system
availability, A ≥ 93.0%, for scenarios specific to the control plane
and A ≥ 99.35% for data plane cases which tends to the industry
service level agreement for system availability set at A = 99.999%
(5 nines). Moreover,

- Index Terms—IoT-Edge, SDN, NFV, TSN, IEC61850, vPAC,
HCTMM, offshore wind, dependability.

<img src="https://github.com/PinaPhD/JP2/blob/main/ReadMe_Logical.png" width="800" height="500">


---

##### Part 1: Probabilistic quantitative HCTMC system model
[HCTMC Model](https://github.com/PinaPhD/JP2/blob/main/HCTMC_MODEL/)


##### Part 2: Proof-of-concept simulation testbed

[Proof Of Concept Simulation Testbed](https://github.com/PinaPhD/JP2/tree/main/POC/)

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
