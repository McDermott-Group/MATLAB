"""
PSD for Q14 at different J1 Bias with Sim slow bias with flux tunning
Data:
Z:\mcdermott-group\data\Antenna\Circmon\Liu\CW20180514A_Ox2\2021Nov12_QB14_PSD_Flux_J6Radiator_SimFitting method Chris' no white noise verison

"""
import noiselib
import matplotlib.pyplot as plt
import numpy as np


Q1 = np.array([
 [0, 5511.54], [10, 4449.64], [20, 3880.1], [30, 3786.62], [40, 6070.22],
 [50, 8560.8], [60, 4777.68], [70, 5251.92], [80, 5307.98], [90, 4334.33],
 [100, 4479.08], [110, 4130.02], [120, 10125.03], [130, 8886.92], [140, 8047.96],
 [150, 5617.27], [160, 4827.7], [170,5852.15], [180, 7882.99], [190, 4618.55],
 [200, 6333.57], [210, 6322.79], [220, 6931.6], [230, 6310.47], [240, 5156.37],
 [250, 7649.17], [260, 5473.48], [270, 5541.13], [280, 5237.88], [290, 5263.06],
 [300, 4345.86], [310, 4537.37], [320, 4927.98], [330, 4900.92], [340, 4118.82],
 [350, 4973.7], [360, 6924.67], [370, 6044.81], [380, 4540.36], [390, 3632.64],
 [400, 5678.31], [410, 4448.81], [420, 3301.32], [430, 4524.28], [440, 6333.65],
 [450, 7566.99], [460, 6810.99], [470, 8778.02], [480, 8650.98], [490, 8360.19]
])

Q4 = np.array([
 [0, 4048.72], [10, 3855.03], [20, 7696.62], [30, 6302.45], [40, 9003.79],
 [50, 8679.29], [60, 10467.95], [70, 9270.75], [80,9804.83], [90, 9286.4],
 [100, 9864.6], [110, 9653.21], [120, 9816.94], [130, 10108.69], [140, 9580.28],
 [150, 10939.96], [160, 10621.05], [170, 11153.77], [180, 10937.4], [190, 10839.3],
 [200, 11715.77], [210, 11268.93], [220, 10823.44], [230, 10057.31], [240, 10769.68],
 [250, 12251.07], [260, 9238.32], [270, 10446.99], [280, 11068.57], [290, 6324.22],
 [300, 7459.8], [310, 9317.64], [320, 11122.85], [330, 10603.39], [340, 9603.21],
 [350, 10455.32], [360, 10574.85], [370, 4506.97], [380, 5450.66], [390, 11150.58],
 [400, 4714.29], [410, 4830.01], [420, 9137.08], [430, 9793.2], [440, 8337.99],
 [450, 6369.47], [460, 10579.95], [470, 10457.63], [480, 9297.54],
 [490, 10225.29]
])
### J1 Bias Conversion
# Q3[:, 0] = (Q3[:, 0])

# plt.plot(Q3[:, 0], Q3[:, 1], color='y', label='Q3')
# plt.xlabel('Radiator Josephson Frequency (mDAC)')
# plt.ylabel('PSD (Hz)')
# plt.yscale('log')
# plt.grid()
# plt.legend(loc=1)
# plt.show()

# f = 1
f = 0.9676
Al_gap = 380e-6
DAC_Al = 1e5*Al_gap/0.200
d = 2 # for plotting purpose only
# plt.plot(Q1[:, 0]*f, Q1[:, 1]/d, color='b', label='Q1')
plt.plot(Q1[:, 0]*f, Q1[:, 1], color='b', label='Q1')
# plt.plot(Q2[:, 0]*f, Q2[:, 1], color='r', label='Q2')
plt.plot(Q4[:, 0]*f, Q4[:, 1], color='k', label='Q4')

plt.axvline(x=DAC_Al * f, color='k', linestyle='--', linewidth=4, label='JJ Al Gap')

plt.xlabel('Radiator Josephson Frequency (GHz)')
plt.ylabel('PSD (Hz)')
plt.yscale('log')
plt.grid(True, which="both")
plt.legend(loc=1)
# plt.xlim([0, 1500])
# plt.ylim([10, 100000])
plt.show()


