# -*- coding: utf-8 -*-
"""
- @Author: Agrippina W. Mwangi
- @Affiliation: Energy & Resources Group, Copernicus Institute of Sustainable Development, Utrecht University
- @Date of Creation: November 2023
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import random
from math import pi
from datetime import datetime, timedelta
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle
from scipy.linalg import null_space
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from scipy.linalg import solve

"""
Transient behaviour assessment from the proof of concept simulation testbed
"""

#Importing iperf3 measurement files from the proof of concept simulation testbed (pre-processed files)
baseline = pd.read_csv('Data/baseline.csv')
baseline_ploss1 = pd.read_csv('Data/baselineploss1.csv')
baseline_ploss10 = pd.read_csv('Data/baselineploss10.csv')
packetloss_1percent = pd.read_csv('Data/1packetloss.csv')
packetloss_10percent = pd.read_csv('Data/10packetloss.csv')
switch_fail = pd.read_csv('Data/switch_fail_3.csv')

#Observing the switch behaviour amid stochastic failure
sns.set(style="darkgrid")

plt.figure(figsize=(12, 4))
sns.lineplot(x='Time', y='Transfer (GBytes)', label='Baseline', data=baseline)
sns.lineplot(x='Time', y='Transfer (GBytes)', label='Switch failure', data=switch_fail)
plt.title('The effect of Switch Failures on Data Transfer Rates Over Time')
plt.xlabel('Time')
plt.ylabel('Transfer (Gbytes/sec)')
major_ticks = baseline.index[::20]  # Selecting every 20th point
plt.xticks(major_ticks)
plt.xticks(rotation=45)

plt.legend(title="Throughput", loc='best')
# Tight layout often improves the spacing between subplots
plt.tight_layout()
plt.show()

#Observing the network degradation
sns.set(style="darkgrid")

plt.figure(figsize=(12, 5))
sns.lineplot(x='Time', y='Transfer (GBytes)', label='Baseline', data=baseline_ploss1)
sns.lineplot(x='Time', y='Transfer (GBytes)', label='1% packet loss', data=packetloss_1percent)
plt.title('Plot of Transfer (GBytes) per second with 1% Packet Loss')
plt.xlabel('Time')
plt.ylabel('Transfer (Gbytes/sec)')
major_ticks = baseline_ploss1.index[::20]  # Selecting every 20th point
plt.xticks(major_ticks)
plt.xticks(rotation=45)


plt.legend(title = "Degraded Network", loc="best")
# Tight layout often improves the spacing between subplots
plt.tight_layout()
plt.show()


sns.set(style="darkgrid")

plt.figure(figsize=(12, 5))
sns.lineplot(x='Time', y='Transfer (GBytes)', label='Baseline', data=baseline_ploss10)
sns.lineplot(x='Time', y='Transfer (GBytes)', label='1% packet loss', data=packetloss_10percent)
plt.title('Plot of Transfer (GBytes) per second with 1% Packet Loss')
plt.xlabel('Time')
plt.ylabel('Transfer (Gbytes/sec)')
major_ticks = baseline_ploss1.index[::20]  # Selecting every 20th point
plt.xticks(major_ticks)
plt.xticks(rotation=45)


plt.legend(title = "Degraded Network", loc="best")
# Tight layout often improves the spacing between subplots
plt.tight_layout()
plt.show()


"""
Steady-state behaviour: A probabilistic homogeneous continuous time markov chain

Transition Rate Sources:

* V. B. Mendiratta, L. J. Jagadeesan, R. Hanmer, and M. R. Rahman,
“How reliable is my software-defined network? models and failure
impacts,” in 2018 IEEE International Symposium on Software Reliability
Engineering Workshops (ISSREW), pp. 83–88, IEEE, 2018.

* G. Nencioni, B. E. Helvik, A. J. Gonzalez, P. E. Heegaard, and
A. Kamisinski, “Availability modelling of software-defined backbone
networks,” in 2016 46th Annual IEEE/IFIP International Conference
on Dependable Systems and Networks Workshop (DSN-W), pp. 105–
112, IEEE, 2016

* T. A. Nguyen, T. Eom, S. An, J. S. Park, J. B. Hong, and D. S. Kim,
“Availability modeling and analysis for software defined networks,” in
2015 IEEE 21st Pacific Rim International Symposium on Dependable
Computing (PRDC), pp. 159–168, IEEE, 2015.

*F. Xiao, Z. Zhang, and X. Yin, “Reliability evaluation of the centralized
substation protection system in smart substation: RELIABILITY EVAL-
UATION OF CENTRALIZED SUBSTATION PROTECTION SYS-
TEM,” IEEJ Transactions on Electrical and Electronic Engineering,
vol. 12, pp. 317–327, May 2017.

"""

'''
From the highlighted sources, the stochastic component failure attributed to CPU, MEMORY, HARDWARE failure and 
resource fluctuation or overconsumption 
'''

import pandas as pd

# Defining the rates and components
rates_updated = {
    # General component failure rates
    'λCPU': 36.378*10**-6,                  # CPU failure rate
    'λCPU-THRESHOLD': 0.7205*10**-6,        # CPU consumption above the threshold
    'λMEM': 36.378*10**-6,                  # Memory failure rate
    'λMEM-THRESHOLD': 0.7205*10**-6,        # Memory consumption above the threshold
    'λFD': 5*10**-6,                        # Forwarding Device hardware failure rate
    'λCON': 16.67*10**-6,                   # Controller VM failure rate
    'λFIBER': 14.28*10**-6,                 # Fiber optic link failure rate
    'λSF': 36.378*10**-6,                   # Software failure rate
    
    # Controller specific
    'λVM': 16.67*10**-6,                    # Controller VM failure rate
    
    # Forwarding Device specific
    'λHW': 5*10**-6,                        # Forwarding Device Hardware failure rate
}

# Create DataFrame from updated rates
failures_updated = pd.DataFrame(list(rates_updated.items()), columns=['Component', 'Failure Rate'])

# Assume each component's failure rates apply to each individual controller and Forwarding Device
num_controllers = 3
num_forwarding_devices = 9

# Identify component failure rates relevant to controllers and Forwarding Devices
controller_components = ['λCPU', 'λCPU-THRESHOLD', 'λMEM', 'λMEM-THRESHOLD', 'λCON', 'λVM', 'λSF']
forwarding_device_components = ['λCPU', 'λCPU-THRESHOLD', 'λMEM', 'λMEM-THRESHOLD', 'λFD', 'λHW', 'λSF']

columns = ['Component', 'Failure Rate', 'C1', 'C2', 'C3', 'FD1', 'FD2', 'FD3', 'FD4', 'FD5', 
           'FD6', 'FD7', 'FD8', 'FD9']
data = []

# Scale the failure rates in the DataFrame by 1e-5
scale_factor = 1e-5

# Populate data for each component, marking applicable components with their failure rate or 0 if not applicable
for component, rate in rates_updated.items():
    row = [component, rate]
    # Determine applicability for controllers (C1, C2, C3)
    row.extend([rate if component in controller_components else 0] * num_controllers)
    # Determine applicability for Forwarding Devices (FD1 to FD9)
    row.extend([rate if component in forwarding_device_components else 0] * num_forwarding_devices)
    data.append(row)

# Create the adjusted DataFrame with the correct columns
failures_adjusted = pd.DataFrame(data, columns=columns)

# Remove the 'Failure Rate' column from the adjusted DataFrame
failures_adjusted.drop('Failure Rate', axis=1, inplace=True)

# Apply scaling to all numeric columns except 'Component' column
for column in failures_adjusted.columns[1:]:  # Skip 'Component' column
    failures_adjusted[column] = failures_adjusted[column].apply(lambda x: x * scale_factor if x != 0 else x)

failures_adjusted


#Using the Baseline HCTMM Model Parameters (Table III)
rates = {
    'λC': 50 / 365 / 24 / 60,   # Controller failure rate, converted from per year to per minute
    'λS': 25 / 365 / 24 / 60,   # Switch failure rate, converted from per year to per minute
    'λdc': 3600 / 3600 / 60,    # Controller failure detection rate, normalized to per minute
    'λm': 2073 / 3600 / 60,     # Switch migration rate, normalized to per minute
    'λds': 3600 / 3600 / 60,    # Switch failure detection rate, normalized to per minute
    'μS': 25 / 3600 / 60 / 60,       # Switch add/repair rate, normalized to per minute
    'μC': 32 / 3600 / 60 / 60,       # Controller add/repair rate, normalized to per minute
    'δC': 9 / 3600 / 60 / 60,        # detC to fdetC, normalized to per minute
    'αC': 4145 / 3600 / 60 / 60,     # fdetC to detC, normalized to per minute
    'δS': 9 / 3600 / 60,        # detS to fdetS, normalized to per minute
    'αS': 4145 / 3600 / 60,     # fdetS to detS, normalized to per minute
    'μP': 12 / 3600 / 60,       # Assumed transition rate μP, normalized to per minute
}

#Defining the possible states of the HCTMM model
# Define the number of states (Working, Degraded1, Degraded2,Failed)
num_states = 9
cf = 0.97   #Coverage factor: probability that the repair restores the system to its original state

# Initialize the transition rate matrix with zeros
Q = np.zeros((num_states, num_states))


Q[0, 1] = rates['λdc'] + rates['λm']  # W -> detC
Q[1, 2] = rates['δC']                 # detC to fdetC
Q[2, 1] = rates['αC']                 # fdetC to detC
Q[1, 3] = rates['λm']                 # detC to migS
Q[3, 4] = rates['λC']                 # migS to D1
Q[4, 0] = rates['λC']                 # D1 -> W
Q[4, 1] = rates['λC']                 # D1 -> detC
Q[0, 5] = rates['λds']                #W to detS
Q[5, 6] = rates['δS']                 #detS to fdetS
Q[6, 5] = rates['αS']                 #fdetS to detS
Q[5, 7] = rates['λS']                 #detS to D2
Q[7, 0] = rates['μS']                 #D2 to W
Q[3, 8] = rates['λC']                 #migS to F
Q[8, 0] = cf*rates['μC']              #F to W  (RμC)


# Set the diagonal elements to the negative sum of the other rates in the row
for i in range(num_states):
    Q[i, i] = -np.sum(Q[i, :])
    

Q_df = pd.DataFrame(Q, index=['W', 'detC', 'fdetC', 'migS', 'D1', 'detS', 'fdetS', 'D2', 'F'], 
                       columns=['W', 'detC', 'fdetC', 'migS', 'D1', 'detS', 'fdetS', 'D2', 'F'])

row_sums = Q_df.sum(axis=1)
#Q_df


plt.figure(figsize=(14,6))
sns.heatmap(Q_df, annot=True, fmt=".8f", linewidths=.5,cmap='viridis')
plt.title('Transition Rate Matrix Heatmap (Baseline)')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()


#Extracting 15 relevant test case scenarios for sensitivity analysis
data = {
    "W": [0.835348, 0.683357, 0.608196, 0.752306, 0.601651, 0.509643, 0.242107, 0.569143, 0.251691, 0.551410, 0.589836, 0.412051, 0.724266, 0.710102, 0.357879],
    "detC": [0.015635, 0.059016, 0.039265, 0.056211, 0.037471, 0.075485, 0.431954, 0.100241, 0.026448, 0.040368, 0.020883, 0.065687, 0.062160, 0.052509, 0.134116],
    "fdetC": [0.033076, 0.081102, 0.014967, 0.040331, 0.179774, 0.212136, 0.254912, 0.109708, 0.010867, 0.071035, 0.022898, 0.032698, 0.036936, 0.067042, 0.225683],
    "migS": [0.010013, 0.144455, 0.025067, 0.036133, 0.026991, 0.108981, 0.025025, 0.047115, 0.026927, 0.013256, 0.028400, 0.012346, 0.108818, 0.033722, 0.024392],
    "D1": [2.434093e-07, 7.523393e-07, 3.751728e-08, 3.005067e-07, 4.995114e-08, 3.861437e-07, 5.927990e-07, 2.534061e-06, 2.830005e-07, 2.473096e-08, 3.666146e-07, 1.926607e-07, 3.321703e-05, 5.936272e-07, 5.623995e-07],
    "DetS": [0.059393, 0.024633, 0.203373, 0.077328, 0.058366, 0.066929, 0.033042, 0.100314, 0.579376, 0.124190, 0.146120, 0.228595, 0.032043, 0.039357, 0.209467],
    "fdetS": [0.046520, 0.007433, 0.109123, 0.037680, 0.095737, 0.026811, 0.012904, 0.073430, 0.104687, 0.199735, 0.191814, 0.248616, 0.035500, 0.097255, 0.048451],
    "D2": [0.000013, 0.000002, 0.000006, 0.000010, 0.000007, 0.000008, 0.000013, 0.000029, 0.000002, 0.000006, 0.000039, 0.000005, 0.000090, 0.000006, 0.000007],
    "F": [3.005020e-06, 1.905334e-06, 3.329833e-06, 9.699632e-07, 3.239335e-06, 6.445912e-06, 4.279833e-05, 1.840958e-05, 2.651417e-06, 9.022927e-07, 1.022303e-05, 1.698633e-06, 1.545603e-04, 6.467690e-06, 5.754386e-06]
}
index = ["Scenario-I", "Scenario-2", "Scenario-3", "Scenario-4", "Scenario-5", "Scenario-6", "Scenario-7", "Scenario-8", "Scenario-9", "Scenario-10", "Scenario-11", "Scenario-12", "Scenario-13", "Scenario-14" , "Scenario-15" ]

ssp_scenarios = pd.DataFrame(data,index=index)

# Now let's create the violin plot
plt.figure(figsize=(10, 5))
sns.violinplot(data=ssp_scenarios,  scale='width', inner='quartile',label='HCTMM Scenarios')

plt.title('Violin Plot of Steady-State Probabilities of the HCTMM states for 15 test case scenarios')
plt.xlabel('States')
plt.ylabel('Probability Values')
#plt.ylim(0, 1)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend
plt.show()



"""
This work is under the Innovative Tools for Cyber-Physical Energy Systems project funded by the European Union's Horizon 2020 research and innovation programme under the Marie Sklodowska Curie grant agreement No 956433.
"""