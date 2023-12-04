
### SDN-enabled IoT-Edge Network for next-generation offshore wind farms

#### The Introduction
Determining the dependability of the proposed SDN-enabled IoT-Edge network 
is of utmost importance to wind farm developers.

#### The Model
The proposed SDN-enabled IoT-Edge network comprises _(1,...,n)_ sensors 
sending data samples to _(1,...,n)_ ECP nodes and _(1,...,n)_ vPAC nodes. 
The ECP and vPAC nodes send back actuation signals to _(1,...,n)_ actuators. 
These data samples and actuation signals are sent through _(1,...,n)_ OpenFlow-enabled 
switches. 

For this model,
- 10 sensors
- 10 ECP nodes
- 10 vPAC nodes
- 10 actuators
- 9 switches
- 3 controllers

Any of the sensors, ECP nodes, vPAC nodes, and actuators can fail. 
It is important that _at_ _least_ 2 of each continue are working at any given time.
Otherwise, logs are collected and the O&M team gets an _emergency_ alert.
The 9 switches connect the sensors and actuators to the ECP and vPAC nodes. Further, 
the allow for the bi-directional flow of data. The are the most critical part of the proposed network.

When data samples are received at the switch port, it searches its flow table for a flow instruction 
on how to forward the data sample to the destination. When no flow is available, it sends a flow request 
to the SDN_controller which has a global view of the network. The SDN controller responds with a flow 
instruction which guides the switch on the most optimal flow path.

The three controller cluster remotely connected to the 9 switches. 

#### The Experimental Results
