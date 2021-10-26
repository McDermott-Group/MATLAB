"""
P1 for Q1 at different J7 Bias
Data:
### Z:\mcdermott-group\data\Antenna\SUXmon\Liu\VitoChip1\P12021Oct22_Q1WithJ7


"""
import noiselib
import matplotlib.pyplot as plt
import numpy as np


Q1 = np.array([
 [0.0, 0.17473, 0.02012], [0.005, 0.1756, 0.01989], [0.01, 0.17443, 0.0193],
 [0.015, 0.17634, 0.01881], [0.02, 0.17455, 0.01903], [0.025, 0.17725, 0.02075],
 [0.0275, 0.17763, 0.02231], [0.03, 0.17673, 0.02156], [0.0325, 0.17817, 0.02076],
 [0.0349, 0.1784, 0.02072], [0.0374, 0.17758, 0.02143], [0.04, 0.17692, 0.02181],
 [0.041, 0.17765, 0.02168], [0.042, 0.17716, 0.0226], [0.043, 0.17605, 0.02031],
 [0.044, 0.17709, 0.0204], [0.045, 0.17887, 0.02135], [0.046, 0.1786, 0.01976],
 [0.047, 0.17823, 0.02231], [0.048, 0.17889, 0.02146], [0.049, 0.17852, 0.02023],
 [0.05, 0.18053, 0.02062], [0.051, 0.18112, 0.02116], [0.052, 0.1804, 0.02055],
 [0.053, 0.1823, 0.02067], [0.054, 0.18033, 0.02154], [0.055, 0.18146, 0.01974],
 [0.056, 0.18247, 0.02109], [0.057, 0.1811, 0.02092], [0.058, 0.18216, 0.02121],
 [0.059, 0.17943, 0.01918], [0.06, 0.17865, 0.01956], [0.061, 0.18003, 0.01994],
 [0.062, 0.1789, 0.01905], [0.063, 0.17866, 0.02128], [0.064, 0.17764, 0.02085],
 [0.065, 0.17792, 0.02242], [0.066, 0.17717, 0.02153], [0.067, 0.17718, 0.01991],
 [0.068, 0.17858, 0.02006], [0.069, 0.1782, 0.02141], [0.07, 0.17698, 0.02027],
 [0.07, 0.17607, 0.01895], [0.0725, 0.17725, 0.01991], [0.075, 0.17761, 0.0225],
 [0.0775, 0.17801, 0.02044], [0.08, 0.17873, 0.02039], [0.0825, 0.17653, 0.02068],
 [0.085, 0.17848, 0.02062], [0.0875, 0.1768, 0.02112], [0.09, 0.17631, 0.01959],
 [0.0925, 0.17637, 0.0204], [0.095, 0.17764, 0.02075], [0.0975, 0.17629, 0.02054],
 [0.1, 0.1779, 0.02207], [0.105, 0.17877, 0.02083], [0.11, 0.17844, 0.0223],
 [0.115, 0.17739, 0.02212], [0.12, 0.17737, 0.01988], [0.125, 0.17954, 0.02101],
 [0.13, 0.17814, 0.02086], [0.135, 0.17886, 0.02031], [0.14, 0.17937, 0.01999],
 [0.145, 0.18015, 0.01936]
])

### J7 Bias Conversion
Q1[:, 0] = (Q1[:, 0])*1000
# Q2[:, 0] = (Q2[:, 0])*1000
# Q4[:, 0] = (Q4[:, 0])*1000


f = 4.604
Al_gap = 380e-6
DAC_Al = 1e5*Al_gap/0.952
plt.errorbar(Q1[:, 0]*f, Q1[:, 1], yerr=Q1[:, 2]/np.sqrt(300), color='b', label='Q1')
# plt.errorbar(Q2[:, 0]*f, Q2[:, 1], yerr=Q2[:, 2]/np.sqrt(150), color='r', label='Q2')
# plt.errorbar(Q4[:, 0]*f, Q4[:, 1], yerr=Q4[:, 2]/np.sqrt(150), color='y', label='Q4')

plt.axvline(x=DAC_Al * f, color='k', linestyle='--', linewidth=4, label='JJ Al Gap')

plt.xlabel('Radiator Josephson Frequency (GHz)')
plt.ylabel('P1')
plt.yscale('log')
plt.grid()
plt.legend(loc=1)
# plt.xlim([0, 1500])
# plt.ylim([10, 100000])
plt.show()



