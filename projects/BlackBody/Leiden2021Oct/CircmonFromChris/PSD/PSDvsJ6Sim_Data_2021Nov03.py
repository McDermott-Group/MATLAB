"""
PSD for Q1, Q2, Q4 at different J6 Bias with Sim slow bias
Data:
Z:\mcdermott-group\data\Antenna\Circmon\Liu\CW20180514A_Ox2\2021Nov02_QB124_PSD_J6Radiator_Sim
Fitting method Chris' no white noise verison

"""
# import noiselib
import matplotlib.pyplot as plt
import numpy as np
import copy


Q1 = np.array([
    [0, 1009.34], [10, 958.58], [20, 1145.83], [30, 1046.75], [40, 1160.41],
    [50, 944.89], [60, 1210.19], [65, 1009.63], [70, 962.35], [75, 1140.02],
    [80, 1023.09], [85, 950.27], [90, 1115.45], [95, 1010.86], [100, 1010.15],
    [105, 941.78], [110, 1220.46], [115, 3437.57], [120, 4664.58], [125, 5172.3],
    [130, 4358.9], [135, 4078.99], [140, 3504.63], [145, 2565.52], [150, 2402.98],
    [155, 2252.7], [160, 2143.96], [165, 2867.33], [170, 2797.36], [175, 2298.0],
    [180, 2121.93], [185, 1866.51], [190, 2393.17], [195, 3000.95], [200, 3228.92],
    [205, 2731.99], [210, 4102.09], [215, 2740.09], [220, 2366.99], [225, 2074.19],
    [230, 2532.39], [235, 2125.4], [240, 1961.89], [245, 1994.41], [250, 1631.03],
    [255, 1733.2], [260, 1552.79], [265, 1505.57], [270, 1453.08], [275, 1596.24],
    [280, 1432.32], [285, 1493.91], [290,1538.86], [295, 1804.63], [300, 1614.51],
    [305, 1580.93], [310, 1528.13], [315, 1682.05], [320, 1507.64], [325, 1496.16],
    [330, 1612.51], [335, 1797.43], [340, 1642.42], [345, 1414.63], [350, 1333.24],
    [355, 1471.76], [360, 1455.64], [365, 1274.01], [370, 1213.63], [375, 1250.93],
    [380, 1262.28], [385, 1188.31], [390, 1350.99], [395, 1381.67], [400, 1434.28],
    [405, 1381.46], [410, 1514.37], [415, 1276.58], [420, 1198.76], [425, 1342.48],
    [430, 1600.78], [435, 1932.09], [440, 3354.68], [445, 2190.77], [450, 4330.97],
    [455, 4096.65], [455, 4096.65], [460, 4260.12], [465, 4579.53], [470, 5555.07],
    [475, 6303.84], [480, 5552.77], [485, 4612.55], [490, 5192.22], [495, 6452.49],
    [500, 6584.32], [505, 5684.13], [510, 5332.56], [515, 5229.72], [520, 5744.56],
    [525, 5112.43], [530, 6392.96], [535, 6664.02], [540, 5807.01], [545, 8712.34],
    [550, 5562.97], [555, 6059.17], [560, 5850.5], [565, 6664.39], [570, 7159.78],
    [575, 7547.52], [580, 7821.21]
])


Q2 = np.array([
    [0, 12.86], [10, 11.36], [20, 13.26], [30, 12.21], [40, 12.7], [50, 12.83],
    [60, 12.84], [65, 11.72], [70, 12.77], [75, 13.46], [80,14.29], [85, 11.23],
    [90, 12.81], [95, 12.3], [100, 12.55], [105, 14.13], [110, 13.12], [115, 13.11],
    [120, 13.91], [125, 46.08], [130, 70.16], [135, 59.33], [140, 49.56], [145, 45.13],
    [150, 33.69], [155, 32.47], [160, 29.91], [165, 40.26], [170, 49.44], [175, 74.12],
    [180, 69.88], [185, 53.25], [190, 76.92], [195, 87.42], [200, 104.56], [205, 138.78],
    [210, 135.9], [215, 103.5], [220, 133.22], [225, 111.34], [230, 101.3], [235, 114.74],
    [240, 98.55], [245, 92.63], [250, 79.81], [255, 79.2], [260, 93.96], [265, 72.88],
    [270, 76.79], [275, 89.38], [280, 84.88], [285, 89.87], [290, 80.34], [295, 113.91],
    [300, 91.7], [305, 103.52], [310, 137.55], [315, 242.21], [320, 289.37], [325, 309.71],
    [330, 394.06], [335, 445.71], [340, 398.16], [345, 328.41], [350, 332.01], [355, 378.13],
    [360, 397.16], [365, 407.39], [370, 417.23], [375, 501.99], [380, 589.45], [385, 539.99],
    [390, 591.56], [395, 581.89], [400, 598.1], [405, 587.99], [410, 548.04], [415, 464.87],
    [420, 344.23], [425, 326.42], [430, 332.82], [435, 317.92], [440, 269.24],
    [445, 235.44], [450, 277.23], [455, 229.28], [455, 229.28], [460, 189.52],
    [465, 180.09], [470, 176.76], [475, 144.67], [480, 142.35], [485, 141.16],
    [490, 139.55], [495, 154.04], [500, 166.06], [505, 161.47], [510, 156.82],
    [515, 140.3], [520, 123.91], [525, 125.29], [530, 127.77], [535, 122.87],
    [540, 128.8], [545, 118.93], [550, 126.27], [555, 128.9], [560, 135.61],
    [565, 144.21], [570, 151.43], [575, 153.62], [580, 156.3]
])



Q4 = np.array([
    [0, 201.33], [10, 191.95], [20, 185.84], [30, 184.72], [40, 190.91], [50, 192.32],
    [60, 191.89], [65, 199.26], [70, 185.41], [75, 186.42], [80, 191.55], [85, 187.11],
    [90, 196.13], [95, 192.59], [100, 183.86], [105, 195.27], [110, 173.7], [115, 197.69],
    [120, 230.62], [125, 303.48], [130, 325.11], [135, 437.51], [140, 443.43], [145, 591.88],
    [150, 542.91], [155, 349.66], [160, 333.63], [165, 492.91], [170, 650.01], [175, 874.25],
    [180, 789.24], [185, 743.13], [190, 1292.96], [195, 2104.6], [200, 2590.91],
    [205, 2378.21], [210, 3400.27], [215, 2979.89], [220, 2583.41], [225, 3639.7],
    [230, 2984.22], [235, 3062.72], [240, 2624.84], [245, 2456.55], [250, 2150.58],
    [255, 2201.17], [260, 2371.47], [265, 2309.56], [270, 2076.11], [275, 2427.54],
    [280, 2452.78], [285, 1863.37], [290, 1673.27], [295, 1555.0], [300, 1159.26],
    [305, 1230.32], [310, 1226.15], [315, 1300.76], [320, 1719.83], [325, 1759.15],
    [330, 1350.34], [335, 1180.01], [340, 1433.55], [345, 1233.66], [350, 1099.69],
    [355, 826.48], [360, 706.27], [365, 750.64], [370, 655.02], [375, 760.93],
    [380, 798.0], [385, 684.65], [390, 619.28], [395, 672.03], [400, 646.95],
    [405, 650.66], [410, 591.86], [415, 603.73], [420, 661.36], [425, 708.76],
    [430, 675.09], [435, 863.73], [440, 834.24], [445, 846.6], [450, 891.59],
    [455, 900.44], [455, 900.44], [460, 936.8], [465, 840.21], [470, 927.87],
    [475, 862.11], [480, 860.69], [485, 919.19], [490, 918.64], [495, 929.98],
    [500, 944.81], [505, 994.55], [510, 984.28], [515, 974.87], [520, 1126.25],
    [525, 1080.68], [530, 1000.69], [535, 1014.04], [540, 1088.76], [545, 1032.05],
    [550, 1028.85], [555, 1111.87], [560, 1200.51], [565, 1246.12], [570, 1264.38],
    [575, 1305.01], [580, 1357.58]
])


### J6 Bias Conversion

Q1_pure = copy.deepcopy(Q1)
Q2_pure = copy.deepcopy(Q2)
Q4_pure = copy.deepcopy(Q4)
e_Q41 = 0.0
e_Q21 = 0.01
e_Q24 = 0.035
Q4_pure[:, 1] = Q4_pure[:, 1] - e_Q41*Q1_pure[:, 1]
Q2_pure[:, 1] = Q2_pure[:, 1] - e_Q21*Q1_pure[:, 1]-e_Q24*Q4_pure[:, 1]


# plt.plot(Q1[:, 0], Q1[:, 1], color='b', label='Q1')
# plt.plot(Q2[:, 0], Q2[:, 1], color='r', label='Q2')
# plt.plot(Q4[:, 0], Q4[:, 1], color='y', label='Q4')
# plt.xlabel('Radiator Josephson Frequency (mDAC)')
# plt.ylabel('PSD (Hz)')
# plt.yscale('log')
# plt.grid()
# plt.legend(loc=1)
# plt.show()

f = 0.968
# f = 1
Al_gap = 380e-6
DAC_Al = 1e5*Al_gap/0.200
# plt.plot(Q1[::2, 0]*f, Q1[::2, 1], color='b', label='Q1')
# plt.plot(Q2[::2, 0]*f, Q2[::2, 1], color='r', label='Q2')
# plt.plot(Q4[::2, 0]*f, Q4[::2, 1], color='y', label='Q4')
plt.plot(Q1[:, 0]*f, Q1[:, 1], color='b', label='Q1')
plt.plot(Q2[:, 0]*f, Q2[:, 1], color='r', label='Q2')
plt.plot(Q4[:, 0]*f, Q4[:, 1], color='y', label='Q4')

plt.plot(Q1[:, 0]*f, Q1[:, 1]*0.01, '-', label='Q2FromQ1')
plt.plot(Q4[:, 0]*f, Q4[:, 1]*0.04, '-', label='Q2FromQ4')
plt.plot(Q2[:, 0]*f, Q4[:, 1]*0.04+Q1[:, 1]*0.008, '--', label='Q2FromQ14')

plt.plot(Q1_pure[:, 0]*f, Q1_pure[:, 1]*e_Q21, 'b--', label='Q1_pure')
plt.plot(Q2_pure[:, 0]*f, Q2_pure[:, 1], 'r--', label='Q2_pure')
plt.plot(Q4_pure[:, 0]*f, Q4_pure[:, 1]*e_Q24, 'y--', label='Q4_pure')

plt.axvline(x=DAC_Al * f, color='k', linestyle='--', linewidth=4, label='JJ Al Gap')

plt.xlabel('J6 Weak Radiator Josephson Frequency (GHz)')
plt.ylabel('PSD (Hz)')
plt.yscale('log')
# plt.xscale('log')
plt.grid(True, which="both")
plt.legend(loc=2)
# plt.xlim([0, 1500])
# plt.ylim([10, 100000])
plt.show()



