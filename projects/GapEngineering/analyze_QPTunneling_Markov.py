"""
This is to extract QP tunneling rate from limited data points without high readout fidelities.
Date: 2020A April
Author: Chuanhong Liu
"""

import numpy as np
import matplotlib.pyplot as plt


def meas_trace_recover(meas_trace, readout_fidelity, t_QP):
    return None

n_1000 = 4
t = np.arange(0, 1000 * n_1000, 1)
qb_state = np.zeros(len(t))
qb_meas = np.zeros(len(t))
qb_recover = np.zeros(len(t))

t_QP_ = 20000
t_meas_ = 100
p_QP_ = 1 - np.exp(-t_meas_ / t_QP_)
# Transition matrix
p_ee_ = 1 - p_QP_
p_eg_ = p_QP_
p_ge_ = p_QP_
p_gg_ = 1 - p_QP_

# Initial Probabilities, also known as the prior probability, calculated from Transition matrix
p_e_ = 1 / 2
p_g_ = 1 / 2

# Emission Probabilities, or measurement fidelities
p_e1_ = 0.75
p_e0_ = 1 - p_e1_
p_g0_ = 0.95
p_g1_ = 1 - p_g0_
qb_state[0] = 1
for i in range(1, len(qb_state)):
    qb_state[i] = np.random.choice([qb_state[i - 1], 1 - qb_state[i - 1]], p=[1 - p_QP_, p_QP_])
for i in range(len(qb_meas)):
    if qb_state[i] == 0:
        qb_meas[i] = np.random.choice([0, 1], p=[p_g0_, p_g1_])
    if qb_state[i] == 1:
        qb_meas[i] = np.random.choice([0, 1], p=[p_e0_, p_e1_])


t_QP = 10000
t_meas = 100
p_QP = 1 - np.exp(-t_meas / (t_QP))
# Transition matrix
p_ee = 1 - p_QP
p_eg = p_QP
p_ge = p_QP
p_gg = 1 - p_QP

# Initial Probabilities, also known as the prior probability, calculated from Transition matrix
p_e = 1 / 2
p_g = 1 / 2

# Emission Probabilities, or measurement fidelities
p_e1 = 0.75
p_e0 = 1 - p_e1
p_g0 = 0.6
p_g1 = 1 - p_g0


qb_recover = np.zeros(len(t))
for chunck in range(n_1000):
    probabilities = []
    if qb_meas[1000 * chunck] == 0:
        probabilities.append((p_e * p_e1, p_g * p_g1))
    else:
        probabilities.append((p_e * p_e0, p_g * p_g0))

    for i in range(1000 * chunck + 1, 1000 * chunck + 1000):
        prev_e, prev_g = probabilities[-1]
        if qb_meas[i] == 0:
            curr_e = max(prev_e * p_ee * p_e1, prev_g * p_ge * p_e1)
            curr_g = max(prev_e * p_eg * p_g1, prev_g * p_gg * p_g1)
            probabilities.append((curr_e, curr_g))
        else:
            curr_e = max(prev_e * p_ee * p_e0, prev_g * p_ge * p_e0)
            curr_g = max(prev_e * p_eg * p_g0, prev_g * p_gg * p_g0)
            probabilities.append((curr_e, curr_g))

    for p_index in range(len(probabilities)):
        p = probabilities[p_index]
        if p[0] > p[1]:
            qb_recover[1000 * chunck + p_index] = 0
        else:
            qb_recover[1000 * chunck + p_index] = 1

fig = plt.figure(figsize=(20, 10))
font = {'family': 'normal',
        'weight': 'bold',
        'size': 30}
ax = fig.add_subplot(1, 1, 1)
plt.rc('font', **font)
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
plt.plot(t, qb_state + 1.5, 'o-', label=r"Hidden State")
plt.plot(t, qb_meas, 'o-', label=r"Meas")
plt.plot(t, qb_recover - 1.5, 'o-', label=r"Recover")
# plt.plot(t, qb_recover-qb_state-3.5, 'o-', label=r"Recover-state")
plt.legend(prop={'size': 20})

# %%


