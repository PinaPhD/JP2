

### Investigating the dependability of SDN-enabled IoT-Edge networks for next-generation offshore wind farms

---

#### ABSTRACT

>Next-generation offshore wind farms are increasingly adopting vendor-agnostic software-defined networking (SDN) to oversee their IIoT-Edge networks. 
>Inevitably, the SDN-enabled IIoT-Edge networks encounter stochastic failures such as random component malfunctions, software glitches, and fluctuating resource usage.These stochastic failures can result in intermittent network service interruptions, disrupting the real-time exchange of critical, latency-sensitive data that is essential for offshore wind farm operations.
>This paper designs a model abstraction that maps the stochastic failures at the control and data plane to an effective strategy that uses a monitoring agent to detect, recover, and maintain the network model to restore it to a fully operational state upon failure.
>A two-pronged approach is used to investigate the dependability of the proposed network model by assessing: (i) the transient behavior using a proof-of-concept simulation testbed and (ii) the steady-state behavior using a probabilistic Homogeneous Continuous Time Markov Model (HCTMM) under varying failure and repair conditions. 
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
