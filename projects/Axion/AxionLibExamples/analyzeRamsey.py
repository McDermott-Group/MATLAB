from axionlib import *
from dataChest import *
import os


base_path = ['Axion', '2023-04-05 - DR2']
user = 'DCH'
device_name = 'Axion4A JJ Radiator'
dates = ['04-06-23']
experiment_base_name ='Ramsey_XY_Freq_Idle'

expt_paths =  [base_path + [user] + [device_name] + [d] + [experiment_base_name.replace(" ", "_")] for d in dates]
paths = [os.path.join(*([r'Z:\mcdermott-group\data'] + expt_path)) for expt_path in expt_paths]

qb_data = {i:[] for i in range(4,6)}
for path,expt_path in zip(paths,expt_paths):
    for dataSet in os.listdir(path):
        d = dataChest(expt_path)
        d.openDataset(dataSet, modify=True)
        qb_data[d.getParameter('Qubit ID')].append(dataSet)

for qb_id in range(4,6):
    if qb_data[qb_id] == []:
        continue
    else:
        for expt_path in expt_paths:
            for dataSet in qb_data[qb_id]:
                try:
                    TwoDimensionalRamsey(expt_path,dataSet,sequence_name='X/2-Idle-X/2').plot()
                except Exception as e:
                    print(e)
