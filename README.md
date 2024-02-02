

### Investigating the dependability of SDN-enabled IoT-Edge networks for next-generation offshore wind farms

---

#### ABSTRACT

> Next-generation offshore wind farms are increasingly adopting vendor-agnostic software-defined networking (SDN) to oversee their IoT-Edge networks.
> Inevitably, these SDN-enabled IoT-Edge networks encounter stochastic failures such as random component malfunction, software glitches, fluctuating resource usage, and sudden, unpredictable spikes in network traffic. These stochastic failures cause intermittent network service interruptions, disrupting the real-time exchange of critical, delay-sensitive data, essential for offshore wind farm operations.
> A proof-of-concept simulation testbed is developed to assess the transient behavior of the proposed network amid stochastic failure. This paper proposes an effective detection, migration, recoverability, and maintainability strategy for self-healing. To assess the steady-state behavior, a probabilistic Homogeneous Continuous Time Markov Model (HCTMM) was evaluated under variable failure and repair conditions. 
>The HCTMM, tested across 15 scenarios with varied failure-repair rates, shows system availability, $\mathcal{A} \geq 93.0\%$, for scenarios specific to the control plane and $\mathcal{A} \geq 99.35\%$ for data plane cases which tends to the industry service level agreement for system availability set at $\mathcal{A} = 99.999\%$ (5 nines).

> Keywords: `IoT-Edge, SDN, NFV, IEEE802.1 TSN, IEC61850, vPAC, HCTMM, offshore wind, dependability`


<img src="https://github.com/PinaPhD/JP2/blob/main/FrontPage.png" >


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
