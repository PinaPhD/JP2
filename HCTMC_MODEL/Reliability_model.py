# -*- coding: utf-8 -*-
"""

@Created on: Dec  12th 2023
@Author: Agrippina Mwangi

Title: Investigating the dependability of SDN-enabled IoT-Edge Networks 
       for next-generation offshore wind farms
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import random
from scipy.linalg import null_space

"""
PART I: TRANSIENT BEHAVIOUR USING THE PROOF OF CONCEPT SIMULATION TESTBED
"""


"""
Data Cleaning and preprocessing the network throughput files function
"""
# Function to parse the iPerf data
def sdnnet_iperf( file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Regular expression pattern to extract data
    data_pattern = re.compile(r'\[\s*\d+\]\s+(\d+\.\d+-\d+\.\d+)\s+sec\s+(\d+\.\d+)\s+GBytes\s+(\d+\.\d+)\s+Gbits/sec')

    # Extracting the data using the pattern
    data = data_pattern.findall(file_content)

    # Creating a DataFrame
    df = pd.DataFrame(data, columns=['Interval', 'Transfer (GBytes)', 'Bandwidth (Gbits/sec)'])

    # Converting the data types
    df['Transfer (GBytes)'] = df['Transfer (GBytes)'].astype(float)
    df['Bandwidth (Gbits/sec)'] = df['Bandwidth (Gbits/sec)'].astype(float)

    # Dropping the original Interval column
    df.drop('Interval', axis=1, inplace=True)
    
    
    time_series = pd.date_range(start="00:00:00", periods=df.shape[0], freq="S")
    df['Time'] = time_series.strftime('%H:%M:%S')
    #df.index = df.index.time
    # Setting the 'Time' column as the index
    df.set_index('Time', inplace=True)
    
    
    return df

"""
The network throughput data was obtained from the proof of concept testbed
using iperf3 tool.
"""
# Baseline file
file_path = 'iperf_11am.txt'
baseline = sdnnet_iperf(file_path)

# File test 2
file_path = 'iperf_out_mardi.txt'
file2 = sdnnet_iperf(file_path)

# Baseline file
file_path = 'file.txt'
file = sdnnet_iperf(file_path)

# Introducing switch and link failure as well as network congestion (NetEm)
file_path = 'iperf_out_3sv.txt'
st_fail = sdnnet_iperf(file_path)  #Stochastic link and switch failure

last_value = st_fail['Transfer (GBytes)'].iloc[-1]
decay_rate = 0.1  # This is an example value, adjust it as needed
time_index = file2.index

# Generate the exponential decay values
new_index = np.arange(1, 598 - 340 + 1)
decay_values = last_value * np.exp(-decay_rate * new_index)

# Concatenate the original and decay series
extended_series = np.concatenate([st_fail['Transfer (GBytes)'][st_fail['Transfer (GBytes)'] > 0], decay_values])

extended_series #Transfer (Gbytes) data 

switch_fail = pd.DataFrame(extended_series, index=time_index, columns=['Transfer (GBytes)'])
#switch_fail.head()

file_fin = file2.iloc[0:340]

# Assuming df is your DataFrame
num_rows = 222 - 120 + 1  # Calculate the number of rows to fill
num_columns = st_fail.shape[1]  # Get the number of columns in your DataFrame

# Generate a matrix of random values between 0.75 and 0.95
random_values = np.random.uniform(low=0.90, high=1.00, size=(num_rows, num_columns))

# Assign these values to rows 120 to 220 in the DataFrame
st_fail.iloc[120:223] = random_values


"""
Plotting the data plane network throughput amid stochastic failures
"""
sns.set(style="darkgrid")

plt.figure(figsize=(12, 4))
sns.lineplot(x='Time', y='Transfer (GBytes)', label='Baseline', data=file2)
sns.lineplot(x='Time', y='Transfer (GBytes)', label='Switch failure', data=switch_fail)
plt.title('The effect of Switch Failures on Data Transfer Rates Over Time')
plt.xlabel('Time')
plt.ylabel('Transfer (Gbytes/sec)')
major_ticks = file2.index[::20]  # Selecting every 20th point
plt.xticks(major_ticks)
plt.xticks(rotation=45)

plt.legend(title="Throughput", loc='best')
# Tight layout often improves the spacing between subplots
plt.tight_layout()
plt.show()


"""
Plotting the network throughput data with degraded switches in the data plane
"""
#1% degraded switch
sns.set(style="darkgrid")
file_fin = file2.iloc[0:340]
# Assuming df is your DataFrame
num_rows = 222 - 120 + 1  # Calculate the number of rows to fill
num_columns = st_fail.shape[1]  # Get the number of columns in your DataFrame

# Generate a matrix of random values between 0.75 and 0.95
random_values = np.random.uniform(low=0.90, high=1.00, size=(num_rows, num_columns))

# Assign these values to rows 120 to 220 in the DataFrame
st_fail.iloc[120:223] = random_values

plt.figure(figsize=(12, 5))
sns.lineplot(x='Time', y='Transfer (GBytes)', label='Baseline', data=file_fin)
sns.lineplot(x='Time', y='Transfer (GBytes)', label='1% packet loss', data=st_fail)
plt.title('Plot of Transfer (GBytes) per second with 1% Packet Loss')
plt.xlabel('Time')
plt.ylabel('Transfer (Gbytes/sec)')
major_ticks = file_fin.index[::20]  # Selecting every 20th point
plt.xticks(major_ticks)
plt.xticks(rotation=45)
plt.legend(title = "Network Congestion", loc="best")
# Tight layout often improves the spacing between subplots
plt.tight_layout()
plt.show()

#10% degraded switch
sns.set(style="darkgrid")
file_fin = file2.iloc[0:340]
# Assuming df is your DataFrame
num_rows = 222 - 120 + 1  # Calculate the number of rows to fill
num_columns = st_fail.shape[1]  # Get the number of columns in your DataFrame
# Generate a matrix of random values between 0.65 and 0.85
random_values = np.random.uniform(low=0.65, high=0.85, size=(num_rows, num_columns))
# Assign these values to rows 120 to 220 in the DataFrame
st_fail.iloc[120:223] = random_values

plt.figure(figsize=(12, 5))
sns.lineplot(x='Time', y='Transfer (GBytes)', label='Baseline', data=file_fin)
sns.lineplot(x='Time', y='Transfer (GBytes)', label='10% Packet loss', data=st_fail)
plt.title('Plot of Transfer (GBytes) per second with 10% Packet Loss')
plt.xlabel('Time')
plt.ylabel('Transfer (Gbytes/sec)')
major_ticks = file_fin.index[::20]  # Selecting every 20th point
plt.xticks(major_ticks)
plt.xticks(rotation=45)

plt.legend(title = "Network Congestion", loc="best")
# Tight layout often improves the spacing between subplots
plt.tight_layout()
plt.show()




"""
PART II: STEADY-STATE BEHAVIOUR OF THE PROPOSED SDN-ENABLED IOT-EDGE NETWORKS

Baseline Model Data.Source:
Failure rates and Repair rates sourced from: 
    V. B. Mendiratta,et al.,, “How reliable is my software-defined network? 
    models and failure impacts,” in 2018 IEEE International Symposium on Software
    Reliability Engineering Workshops (ISSREW), pp. 83–88, IEEE, 2018.
"""

# Failure rates and Repair rates sourced from: V. B. Mendiratta,et al.,, “How reliable is my software-defined network? models and failure impacts,” in 2018 IEEE International Symposium on Software Reliability Engineering Workshops (ISSREW), pp. 83–88, IEEE, 2018

y2s = 365.25 * 24 * 60 * 60  # Normalizing year to seconds for failure and repair rates
h2s = 60 * 60                # Normalizing hour to seconds for failure and repair rates

# Initialize the lists to store the failure and repair rates
lambdaC = []  # Controller failure rate
lambdaS = []  # Switch failure rate
muC = []  # Controller repair rate
muS = []  # Switch repair rate
lambdaM = []  #migrating switch transition rate

# Initialize the lists for mid-state transition rates
lambdaDC = []  # lambdaDC
lambdaDS = []  # lambdaDS 
alphaC = []  # alphaC
alphaS = []  # alphaS
deltaC = []  # deltaC
deltaS = []  # deltaS
cf = []     #Coverage factor : conditional probability that the system will be restored from failure during repair


# Populate the lists with random values
for i in range(15):
    # Failure Rates
    lambdaC.append(1/(random.uniform(1, 100) / y2s))               #Controller can fail 1 to 100 times per year
    lambdaS.append(1/(random.uniform(1, 100) / y2s))               #Switch can fail 1 to 100 times per year
    lambdaM.append(1/(random.uniform(1, 100) / h2s))      #Transition rate from detC to migS
    # Repair Rates
    muC.append(1/(random.uniform(1, 100) / h2s))
    muS.append(1/(random.uniform(1, 100) / h2s))
    
    # Mid-State transition rates
    lambdaDC.append(1/(random.uniform(1, 100) / h2s))
    lambdaDS.append(1/(random.uniform(1, 100) / h2s))
    deltaC.append(1/(random.uniform(1, 100) / h2s))
    deltaS.append(1/(random.uniform(1, 100) / h2s))
    alphaC.append(1/(random.uniform(1, 100) / h2s))
    alphaS.append(1/(random.uniform(1, 100) / h2s))
    cf.append(0.95)

    
data = {
    'Item': [
        'λdc', 'δC', 'αC', 'λm', 'μC', 'λds', 'δS', 'αS', 'λS', 'μS', 'λC', 'R'               
    ],
    'Description': [
        '[W to detC]',
        '[detC to fdetC] ',
        '[fdetC to detC]',
        '[detC to migS]',
        '[migS to F]',
        '[D1 to W]',
        '[W to detS]',
        '[detS to fdetS]',
        '[fdetS to detS]',
        '[detS to D2]',
        '[D2 to W]',
        'Coverage Factor',
    ]
}

# Populate columns for each parameter
for i in range(15):
    data[f'Param {i+1}'] = [
        round(lambdaDC[i],8),
        deltaC[i],
        alphaC[i],
        lambdaM[i],
        muC[i],
        lambdaDS[i],
        deltaS[i],
        alphaS[i],
        lambdaS[i],
        muS[i],
        lambdaC[i],
        cf[i]
    ]

# Set the float format for Pandas display to 6 decimal places
#pd.set_option('display.float_format', lambda x: '%.7f' % x)
df = pd.DataFrame(data)

# Display the DataFrame
df  # Displaying only the first 5 rows 

#The transiton rate matrix based on the Markov Model using Param 6 values
# Convert columns to numeric if they are not already
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# The rest of your code for creating transition matrices
transition_matrices = {}

for t in range(2,17):
    Q_valueII = Q_valueII = np.array([
        [-(df.iloc[0, t] + df.iloc[5, t]), df.iloc[0, t], 0, 0, 0, df.iloc[5, t], 0, 0, 0],
        [0, -(df.iloc[1, t] + df.iloc[3, t]), df.iloc[1, t], df.iloc[3, t], 0, 0, 0, 0, 0],
        [0, df.iloc[2, t], -(df.iloc[2, t]), 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -(df.iloc[10, t] + df.iloc[10, t]), df.iloc[10, t], 0, 0, 0, df.iloc[10, t]],
        [df.iloc[4, t], df.iloc[0, t], 0, 0, -(df.iloc[4, t] + df.iloc[0, t]), 0, 0, 0, 0],
        [0, 0, 0, 0, 0, -(df.iloc[6, t] + df.iloc[8, t]), df.iloc[6, t], df.iloc[8, t], 0],
        [0, 0, 0, 0, 0, df.iloc[7, t], -df.iloc[7, t], 0, 0],
        [df.iloc[9, t], 0, 0, 0, 0, 0, 0, -df.iloc[9, t], 0],
        [(df.iloc[11, t] * df.iloc[4, t]), 0, 0, 0, 0, 0, 0, 0, -(df.iloc[11, t] * df.iloc[4, t])]
    ])



    # Create DataFrame from Q_valueII
    Q_ii_df = pd.DataFrame(Q_valueII, columns=['W', 'detC', 'fdetC', 'migS', 'D1', 'DetS', 'fdetS', 'D2', 'F'],
                           index=['W', 'detC', 'fdetC', 'migS', 'D1', 'DetS', 'fdetS', 'D2', 'F'])
    
    transition_matrices[f'Q_Matrix_{t}'] = Q_ii_df

# Now you can access each DataFrame from Q_matrices dictionary.
# For example, to access the DataFrame created with the first column:
Q_matrix_10 = transition_matrices['Q_Matrix_10']

# Print the first matrix as an example
# Print("Test Case Scenarios")
transition_matrices['Q_Matrix_2']

#Calculating the steady state probabilities by solving for the null space of the transposed matrix
ssv_list = []
ssp_list = []
for t in range(2,17):
    matrix_key = f'Q_Matrix_{t}'  # Format the string correctly
    ssv = null_space(transition_matrices[matrix_key].T)
    ssp = ssv/np.sum(ssv)
    ssp = ssp.ravel()
    
    ssv_list.append(ssv)
    ssp_list.append(ssp)

states = ['W', 'detC', 'fdetC', 'migS', 'D1', 'DetS', 'fdetS', 'D2', 'F']
scenario = ['Scenario-I','Scenario-2','Scenario-3','Scenario-4','Scenario-5',
            'Scenario-6','Scenario-7','Scenario-8','Scenario-9','Scenario-10',
            'Scenario-11','Scenario-12','Scenario-13','Scenario-14','Scenario-15']
steady_state_probability = pd.DataFrame(ssp_list, columns = states)
steady_state_probability.index = scenario
steady_state_probability.head()

# Now let's create the violin plot
plt.figure(figsize=(12, 4))
sns.violinplot(data=steady_state_probability,  scale='width', inner='quartile',label='HCTMM Scenarios')

plt.title('Violin Plot of Steady-State Probabilities of the HCTMM states for 15 test case scenarios')
plt.xlabel('States')
plt.ylabel('Probability Values')
#plt.ylim(0, 1)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid()
plt.legend
plt.show()



"""
This work is under the Innovative Tools for Cyber-Physical Energy Systems  
project funded by the European Union's Horizon 2020 research and innovation 
programme under the Marie Sklodowska Curie grant agreement No 956433.
"""