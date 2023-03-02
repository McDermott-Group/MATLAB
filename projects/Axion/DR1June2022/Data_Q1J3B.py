from datetime import datetime
from scipy import signal
from dataChest import *
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

biases_data=[-0.06, -0.057999999999999996, -0.055999999999999994, -0.05399999999999999, -0.05199999999999999, -0.04999999999999999, -0.04799999999999999, -0.045999999999999985, -0.043999999999999984, -0.04199999999999998, -0.03999999999999998, -0.03799999999999998, -0.035999999999999976, -0.033999999999999975, -0.03199999999999997, -0.02999999999999997, -0.02799999999999997, -0.025999999999999968, -0.023999999999999966, -0.021999999999999964, -0.019999999999999962, -0.01799999999999996, -0.01599999999999996, -0.013999999999999957, -0.011999999999999955, -0.009999999999999953, -0.007999999999999952, -0.00599999999999995, -0.003999999999999948, -0.0019999999999999463, 5.551115123125783e-17, 0.0020000000000000573, 0.004000000000000059, 0.006000000000000061, 0.008000000000000063, 0.010000000000000064, 0.012000000000000066, 0.014000000000000068, 0.01600000000000007, 0.01800000000000007, 0.020000000000000073, 0.022000000000000075, 0.024000000000000077, 0.02600000000000008, 0.028, 0.03, 0.032, 0.033999999999999996, 0.03599999999999999, 0.03799999999999999, 0.039999999999999994, 0.04199999999999999, 0.043999999999999984, 0.045999999999999985, 0.04799999999999999, 0.04999999999999998, 0.05199999999999998, 0.05399999999999998, 0.05599999999999998, 0.057999999999999975, 0.05999999999999997, 0.06199999999999997, 0.06399999999999997, 0.06599999999999996, 0.06799999999999996, 0.06999999999999997, 0.07199999999999997, 0.07399999999999995, 0.07599999999999996, 0.07799999999999996, 0.07999999999999996, 0.08199999999999995, 0.08399999999999995, 0.08599999999999995, 0.08799999999999995, 0.08999999999999994, 0.09199999999999994, 0.09399999999999994, 0.09599999999999995, 0.09799999999999993, 0.09999999999999994, 0.10199999999999994, 0.10399999999999993, 0.10599999999999993, 0.10799999999999993, 0.10999999999999993, 0.11199999999999993, 0.11399999999999992, 0.11599999999999992, 0.11799999999999992, 0.11999999999999991, 0.12199999999999991, 0.12399999999999992, 0.12599999999999992, 0.12799999999999992, 0.12999999999999992, 0.13199999999999992, 0.13399999999999992, 0.1359999999999999, 0.1379999999999999, 0.1399999999999999, 0.1419999999999999, 0.1439999999999999, 0.1459999999999999, 0.1479999999999999, 0.1499999999999999, 0.15199999999999989, 0.1539999999999999, 0.1559999999999999, 0.1579999999999999, 0.1599999999999999, 0.1619999999999999, 0.1639999999999999, 0.16599999999999987, 0.16799999999999987, 0.16999999999999987, 0.17199999999999988, 0.17399999999999988, 0.17599999999999988, 0.17799999999999988, 0.17999999999999985, -0.2, -0.19, -0.18, -0.16999999999999998, -0.15999999999999998, -0.14999999999999997, -0.13999999999999996, -0.12999999999999995, -0.11999999999999994, -0.10999999999999993, -0.09999999999999992, -0.08999999999999991, -0.0799999999999999, -0.0699999999999999, -0.05999999999999989, -0.04999999999999988, -0.03999999999999987, -0.02999999999999986, -0.01999999999999985, -0.009999999999999842, 1.6653345369377348e-16, 0.010000000000000175, 0.020000000000000184, 0.030000000000000193, 0.0400000000000002, 0.05000000000000021, 0.06000000000000022, 0.07000000000000023, 0.08000000000000024, 0.09000000000000025, 0.10000000000000026, 0.11000000000000026, 0.12000000000000027, 0.13000000000000028, 0.1400000000000003, 0.1500000000000003, 0.1600000000000003, 0.17000000000000032, 0.18000000000000033, 0.19000000000000034, 0.20000000000000034, 0.21000000000000035, 0.22000000000000036, 0.23000000000000037, 0.24000000000000038, 0.2500000000000004, 0.2600000000000004, 0.2700000000000004, 0.2800000000000004, 0.2900000000000004]
parity_rate_data =[1227.2817111582783, 1179.0204699884919, 1163.1595361119878, 1064.2636874240966, 1035.645609456408, 989.7361747514433, 960.7081876389725, 924.7096521779291, 951.6958762187055, 925.969644690773, 945.71153989383, 875.2014247041136, 814.5182668297491, 789.2953023592408, 740.9033887977679, 766.148153475272, 730.6913048620165, 780.1667207329637, 798.7429034578901, 797.7623684252247, 780.9492957881698, 775.2870561097677, 15.352335985712196, 747.9039862271895, 709.5090029242978, 681.6429086134543, 672.8233488435627, 652.0448325459104, 633.5493453361997, 634.0537038717471, 635.8533454721656, 672.5549759058426, 726.0788372386105, 766.3345540525829, 783.3153022931089, 799.4956736707741, 733.0994377569797, 689.0220584763407, 693.7032769436682, 686.3254267444585, 662.2290099141366, 670.2840762634017, 646.9830511487439, 681.8237970787718, 731.8038343226036, 864.6313523168043, 1094.15894174538, 1296.2988629946294, 1295.419317852485, 1215.366113150535, 1033.2864830136305, 1052.524498698836, 837.8316240584861, 557.8504108390683, 460.8262379359794, 456.1007700999713, 408.7810977711913, 386.15439174223775, 404.1521853770063, 405.6337408090537, 409.75259988423096, 401.5855436418431, 393.98144630084784, 413.4749456574204, 413.35312917125276, 424.50378383581557, 419.4430316968097, 431.059289536684, 451.09162910626935, 505.7520947895016, 704.7515927198142, 948.2293205346335, 1034.8675394596378, 1134.9977514367126, 1221.8920234467837, 1233.0443562659789, 1081.78138227941, 856.544253765209, 715.3045347315108, 685.0169828611764, 677.5896864722457, 643.1658429689772, 647.0950868248767, 678.4630177726424, 669.3278428428696, 687.845848022077, 716.3262686022621, 798.6637957804118, 866.2999139781502, 793.9826086585488, 739.0778867443307, 638.8847379460299, 621.2689770352408, 590.6679850527503, 605.8245075962492, 620.0074239402038, 683.6464722129688, 641.9373814386452, 709.1119641260276, 712.6263710342839, 724.851191260557, 788.3098934511094, 839.1950915348405, 848.8840115885691, 879.1089501931856, 860.1090290793688, 816.937432576567, 797.9688172292064, 822.8323221668808, 865.1795010191745, 905.9769738327248, 897.7372955523083, 955.7088060905622, 967.7143765931992, 1015.0313628219765, 1068.9445363493219, 1063.9349689545877, 1128.5644468263192, 1165.2484345732237, 1163.3763651453523, 1225.3077446736963, 3883.630965467972, 3843.064993858691, 3720.11044343621, 3633.219024348494, 3508.1654583614154, 3243.708111823343, 3124.7196697109157, 2823.834592219409, 2630.1299744765174, 2324.7364485098187, 2057.674644483671, 1790.9441351670189, 1518.870288553492, 1355.0681026284628, 1141.5728497229961, 990.781245443102, 827.445811712229, 720.3392852606526, 761.8447635914468, 627.4002345663653, 631.566329120061, 851.7470721712435, 695.7310734806417, 857.7750200930576, 1009.4314924012266, 411.73366635935656, 387.3691998213455, 395.9285466554588, 703.7059921809937, 1467.0710832875307, 590.9893224937017, 74.04661928926859, 75.32140740487742, 197.32640035943723, 27.213576981837846, 123.76563421763721, 70.61443957019937, 48.654892671578644, 52.04173180760676, 76.77650942525872, 34.51731766508547, 37.38536708391117, 1922.0135427209698, 2219.375545627313, 2555.080303203582, 2830.745707233626, 3054.5255099895844, 3306.9650258927354, 3443.9226854606795, 3594.916261298625]


biases=[]
parity_rate=[]
for i in range(len(parity_rate_data)):
    if parity_rate_data[i] < 5000 and parity_rate_data[i] > 0:
        biases.append(biases_data[i])
        parity_rate.append(parity_rate_data[i])

plt.title('Parity Rate vs Radiator Bias')
# plt.plot(4*times, np.abs(I + Q * 1j))
plt.semilogy([np.abs(b-0.062)*(490)*(0.02)*484 for b in biases], parity_rate,marker='.',linestyle='None')
plt.grid(which='both')
plt.ylim(4e2,2e3)
plt.xlim(0,500)
# plt.xlabel('Radiator Bias (mV)')
plt.xlabel('Radiator Frequency (GHz)')
plt.ylabel('Parity Rate (Hz)')
plt.pause(0.1)


