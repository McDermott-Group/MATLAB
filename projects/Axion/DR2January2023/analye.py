from datetime import datetime
from scipy import signal
from dataChest import *
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from axionlib import Parity
import matplotlib
matplotlib.use('TkAgg')

qb_id = 4
rad_id = 1

base_path = ['Axion', '2023-01-23 - DR2']
user = 'DCH'
device_name = 'Axion4A'
dates = ['01-30-23','01-31-23']
experiment_base_name ='PSD_Q{:d}_J{:d}B'.format(qb_id,rad_id)

expt_paths =  [base_path + [user] + [device_name] + [d] + [experiment_base_name.replace(" ", "_")] for d in dates]
paths = [os.path.join(*([r'Z:\mcdermott-group\data'] + expt_path)) for expt_path in expt_paths]


parity_rates=[]
fidelities=[]
biases=[]
for i in range(len(paths)):
    path = paths[i]
    expt_path = expt_paths[i]
    for dataSet in os.listdir(path):
        try:
            d = dataChest(os.path.join(path), dataSet)
            d.cd(expt_path)
            d.openDataset(dataSet,modify=True)
        except:
            continue
        try:
            biases.append(d.getParameter('JB{:1d} Voltage Bias'.format(rad_id))[0])
            try:
                parity_rates.append(d.getParameter('Fit Parity Rate')[0])
                fidelities.append(d.getParameter('Fit Fidelity'))
            except:
                print('Error--Should Not Be Here')
                p=Parity(expt_path, dataSet, rad_id)
                parity_rate,fidelity = p.fit()
                parity_rates.append(parity_rate)
                fidelities.append(fidelity)
                p.plot(fit=True,save=True)
        except:
            continue

plt.figure()
plt.semilogy([np.abs(b+0.01)*484*2*10 for b in biases],parity_rates,marker='.',linestyle='None',color='b')
plt.gca().xaxis.set_tick_params(direction = 'in')
plt.gca().yaxis.set_tick_params(direction = 'in')
plt.xlabel('Radiator Frequency (GHz)')
plt.ylabel('Parity Switching Rate (GHz)')
plt.show()


