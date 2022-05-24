"""
PSD for Q1, Q2, Q4 at different J6 Bias
Data:
Z:\mcdermott-group\data\Antenna\Circmon\Liu\CW20180514A_Ox2\2021Oct16_QB124_PSD_J6Radiator
Fitting method Chris' no white noise verison

"""
import noiselib
import matplotlib.pyplot as plt
import numpy as np


Q1 = np.array([
    [0, 1078.68], [2500, 999.82], [5000, 1016.91], [7500, 1034.04],
    [10000, 1015.61], [12500, 1085.17], [15000, 1018.18], [15000, 1018.18],
    [16000, 967.86], [17000, 1103.88], [18000, 1119.76], [19000, 978.59],
    [20000, 1078.55], [21000, 1004.54], [22000, 1161.92], [23000, 1150.86],
    [24000, 3135.68], [25000, 5569.89], [26000, 6598.09], [27000, 5670.77],
    [28000, 4281.14], [29000, 5000.0], [30000, 3293.89], [31000, 3982.48],
    [32000, 3104.04], [33000, 2834.33], [34000, 4581.58], [35000, 3190.31],
    [36000, 3472.43], [37000, 2238.87], [38000, 3568.64], [39000, 2091.32],
    [40000, 5519.56], [41000, 3188.28], [42000, 2752.9], [43000, 3645.67],
    [44000, 2851.07], [45000, 3528.77], [46000, 3584.03], [47000, 3240.24],
    [48000, 2713.08], [49000, 2704.8], [50000, 2821.12], [51000, 2087.32],
    [52000, 2302.36], [53000, 2615.76], [54000, 2563.2], [55000, 2604.92],
    [56000, 2149.33], [57000, 2082.0], [58000, 2092.85], [59000, 1947.21],
    [60000, 2143.52], [61000, 1988.77], [62000, 1712.5], [63000, 1786.17],
    [64000, 1965.38], [65000, 1852.61], [66000, 1825.28], [67000, 1778.41],
    [68000, 2083.52], [69000, 2023.11], [70000, 1867.65], [71000, 1938.54],
    [72000, 1865.53], [73000, 1877.29], [74000, 1817.14], [75000, 1865.92],
    [76000, 1656.63], [77000, 1616.98], [78000, 1806.2], [79000, 1566.45],
    [80000, 1886.48], [81000, 1692.77], [82000, 1714.68], [83000, 1856.38],
    [84000, 1795.64], [85000, 1644.99], [86000, 1522.69], [87000, 1804.43],
    [88000, 1895.92], [89000, 1783.54], [90000, 1535.05], [91000, 1570.01],
    [92000, 1989.82], [93000, 2555.79], [94000, 4342.84], [95000, 4228.76],
])

"""
Q1
    [96000, 6398.53], [97000, 7129.2], [98000, 7923.7], [99000, 5927.27], 
    [100000, 6334.19], [102500, 8597.25], [105000, 8614.1], [107500, 9039.52], 
    [110000, 9725.3], [112500, 7590.93], [115000,10387.06], [117500, 12640.94], 
    [120000, 16001.85], [122500, 31858.94], [125000, 24285.42], [127500, 42047.57],
    [130000, 60945.26], [132500, 52349.47], [135000, 70188.28], [137500, 74441.65], 
    [140000, 82574.44], [142500,75912.6], [145000, 80358.6], [147500, 81136.89]
"""

Q2 = np.array([
    [0, 13.11], [2500, 13.82], [5000, 13.29], [7500, 13.0], [10000, 12.97],
    [12500, 12.86], [15000, 13.04], [15000, 13.04], [16000, 11.86],
    [17000, 12.54], [18000, 13.28], [19000, 11.56], [20000, 12.21],
    [21000, 13.53], [22000, 12.61], [23000, 13.42], [24000, 13.25],
    [25000, 16.42], [26000, 18.29], [27000, 57.52], [28000, 107.3],
    [29000, 47.13], [30000, 141.52], [31000, 45.15], [32000, 40.28],
    [33000, 28.67], [34000, 41.69], [35000, 42.63], [36000, 44.92],
    [37000, 31.6], [38000, 63.43], [39000, 63.12], [40000, 102.41],
    [41000,115.34], [42000, 157.29], [43000, 286.77], [44000, 181.98],
    [45000, 125.4], [46000, 99.33], [47000, 282.97], [48000, 199.84],
    [49000, 79.21], [50000, 103.4], [51000, 59.02], [52000, 85.29],
    [53000, 86.8], [54000, 62.83], [55000, 163.1], [56000, 122.14],
    [57000, 65.59], [58000, 75.34], [59000, 73.72], [60000, 77.05],
    [61000, 95.16], [62000, 97.09], [63000, 173.19], [64000, 248.98],
    [65000, 278.68], [66000, 261.08], [67000, 323.54], [68000, 259.22],
    [69000, 214.96], [70000, 356.92], [71000, 330.22], [72000, 424.59],
    [73000, 549.75], [74000, 325.67], [75000, 645.99], [76000, 621.75],
    [77000, 554.82], [78000, 365.73], [79000, 717.97], [80000, 486.47],
    [81000, 443.92], [82000, 867.01], [83000, 730.85], [84000, 727.64],
    [85000, 857.31], [86000, 1044.49], [87000, 800.21], [88000, 541.31],
    [89000, 590.86], [90000, 487.61], [91000, 438.85], [92000, 419.95],
    [93000, 331.37], [94000, 369.93], [95000, 463.28], [96000, 350.78],
    [97000, 295.48], [98000, 321.93], [99000, 309.06], [100000, 269.1],
    [102500, 258.54], [105000, 256.93], [107500, 263.24], [110000, 208.82],
    [112500, 218.23], [115000, 214.81], [117500, 240.48], [120000, 249.95],
    [122500, 282.65], [125000, 317.03], [127500, 325.68], [130000, 365.28],
    [132500, 413.1], [135000, 424.04], [137500, 488.02], [140000, 522.45],
    [142500, 546.14], [145000, 585.84], [147500, 625.11], [150000, 823.5],
    [169999, 1362.54], [189999, 2630.75], [209999, 4622.72], [229999, 7763.39],
    [249999, 12262.96]
])

Q2_10usRep = np.array([
    [230000, 12745.99], [250000, 17279.2], [270000, 20590.5]
])
"""
Q2
[269999, 37972.61], [289999, 52435.53], [309999, 75313.89], [329999, 77594.13]

Q2_10us
"""

Q4 = np.array([
    [0, 189.81], [2500, 188.55], [5000, 188.79], [7500, 178.3],
    [10000, 190.36], [12500, 195.36], [15000, 196.13], [15000, 196.13],
    [16000, 184.83], [17000, 192.35], [18000, 191.29], [19000, 195.76],
    [20000, 192.9], [21000, 200.35], [22000, 193.76], [23000, 183.55],
    [24000, 200.41], [25000, 229.36], [26000, 276.71], [27000, 400.1],
    [28000, 310.77], [29000, 654.45], [30000, 566.61], [31000, 399.7],
    [32000, 427.41], [33000, 360.49], [34000, 906.81], [35000, 876.47],
    [36000, 616.05], [37000, 524.09], [38000, 784.77], [39000, 1297.89],
    [40000, 1539.44], [41000, 3271.88], [42000, 5007.14], [43000, 3911.55],
    [44000, 2889.74], [45000, 3225.15], [46000, 2755.31], [47000, 4100.1],
    [48000, 4164.48], [49000, 3581.28], [50000, 3719.63], [51000, 1980.9],
    [52000,3796.64], [53000, 3040.43], [54000, 2541.78], [55000, 2937.74],
    [56000, 2874.69], [57000, 3050.76], [58000, 3502.16], [59000, 2285.78],
    [60000, 1777.45], [61000, 1130.26], [62000, 1705.04], [63000, 1648.01],
    [64000, 2530.56], [65000, 2006.44], [66000, 1509.57], [67000, 1400.99],
    [68000, 2211.09], [69000, 1373.31], [70000, 1356.12], [71000, 1464.85],
    [72000, 1302.45], [73000, 1324.56], [74000, 941.91], [75000, 1087.28],
    [76000, 977.72],[77000, 734.15], [78000, 738.11], [79000, 821.37],
    [80000, 788.4], [81000, 1038.99], [82000, 718.47], [83000, 800.25],
    [84000, 855.59], [85000, 748.27], [86000, 755.35], [87000, 765.22],
    [88000, 823.14], [89000, 1152.36], [90000, 897.02], [91000, 1303.88],
    [92000, 1425.32], [93000, 1391.09], [94000, 1435.63], [95000, 1049.49],
    [96000, 1340.38], [97000, 1360.39], [98000, 1512.52], [99000, 1200.62],
    [100000, 1125.4], [102500, 1526.92], [105000, 1697.92], [107500, 1598.49],
    [110000, 1580.31], [112500, 1669.07], [115000, 1873.96], [117500, 2112.48],
    [120000, 2127.0], [122500, 2613.05], [125000, 2819.47], [127500, 3274.55],
    [130000, 3619.08], [132500, 4057.44], [135000, 4506.21], [137500, 4845.46],
    [140000, 5260.9], [142500, 5377.98], [145000, 5708.79], [147500, 6346.98]
])

"""
Q4
[[150000, 6428.34], [169999, 8292.25], [189999, 15749.21], [209999, 17783.17], [229999, 23978.96
], [249999, 28859.36], [269999, 21958.85], [289999, 9001.36], [309999, 43342.6], [329999, 46772.41]
"""

### J6 Bias Conversion
Q1[:, 0] = (Q1[:, 0])/1000
Q2[:, 0] = (Q2[:, 0])/1000
Q2_10usRep[:, 0] = (Q2_10usRep[:, 0])/1000
Q4[:, 0] = (Q4[:, 0])/1000


# plt.plot(Q1[:, 0], Q1[:, 1], color='b', label='Q1')
# plt.plot(Q2[:, 0], Q2[:, 1], color='r', label='Q2')
# plt.plot(Q4[:, 0], Q4[:, 1], color='y', label='Q4')
# plt.xlabel('Radiator Josephson Frequency (mDAC)')
# plt.ylabel('PSD (Hz)')
# plt.yscale('log')
# plt.grid()
# plt.legend(loc=1)
# plt.show()

np.savetxt('2021OctSFQStrongRadiator_Q1_PSD_Data.txt', Q1)
np.savetxt('2021OctSFQStrongRadiator_Q2_PSD_Data.txt', Q2)
np.savetxt('2021OctSFQStrongRadiator_Q4_PSD_Data.txt', Q4)

f = 4.604
# f = 1
Al_gap = 380e-6
DAC_Al = 1e5*Al_gap/0.952
# plt.plot(Q1[::2, 0]*f, Q1[::2, 1], color='b', label='Q1')
# plt.plot(Q2[::2, 0]*f, Q2[::2, 1], color='r', label='Q2')
# plt.plot(Q4[::2, 0]*f, Q4[::2, 1], color='y', label='Q4')
plt.plot(Q1[:, 0]*f, Q1[:, 1], color='b', label='Q1')
plt.plot(Q2[:, 0]*f, Q2[:, 1], color='r', label='Q2')
plt.plot(Q2_10usRep[:, 0]*f, Q2_10usRep[:, 1], color='r', label='Q2')
plt.plot(Q4[:, 0]*f, Q4[:, 1], color='y', label='Q4')

plt.axvline(x=DAC_Al * f, color='k', linestyle='--', linewidth=4, label='JJ Al Gap')

plt.xlabel('J8 Strong Radiator Josephson Frequency (GHz)')
plt.ylabel('PSD (Hz)')
# plt.xscale('log')
plt.yscale('log')
plt.grid(True, which="both")
plt.legend(loc=2)
plt.xlim([0, 600])
plt.ylim([10, 10000])
plt.show()



