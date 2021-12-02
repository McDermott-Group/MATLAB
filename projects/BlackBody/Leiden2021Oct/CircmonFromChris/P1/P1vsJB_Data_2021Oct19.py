"""
P1 for Q1, Q2, Q4 at different J6 Bias
Data:
Z:\mcdermott-group\data\Antenna\Circmon\Liu\CW20180514A_Ox2\
2021Oct16_QB124_P1_J6Radiator

"""
import noiselib
import matplotlib.pyplot as plt
import numpy as np


Q1 = np.array([
    [0.0, 0.0464, 0.02661], [0.0025, 0.0481, 0.03192], [0.005, 0.0486, 0.02833],
    [0.0075, 0.0486, 0.0281], [0.01, 0.04648, 0.02639], [0.0125, 0.04835, 0.02936],
    [0.015, 0.05067, 0.03294], [0.016, 0.05005, 0.0308], [0.017, 0.04808, 0.0275],
    [0.018, 0.04911, 0.03145], [0.019, 0.04897, 0.03146], [0.02, 0.05182, 0.03383],
    [0.021, 0.04964, 0.02958], [0.022, 0.05055, 0.03092], [0.023, 0.0514, 0.03007],
    [0.024, 0.04087, 0.01972], [0.025, 0.04663, 0.02123], [0.026, 0.11685, 0.03693],
    [0.027, 0.117, 0.04283], [0.028, 0.08619, 0.04513], [0.029, 0.07591, 0.04411],
    [0.03, 0.06416, 0.0395], [0.031, 0.06595, 0.04091], [0.032, 0.06228, 0.04272],
    [0.033, 0.05839, 0.0409], [0.034, 0.06642, 0.04247], [0.035, 0.06166, 0.04122],
    [0.036, 0.05922, 0.03746], [0.037, 0.05526, 0.03714], [0.038, 0.05923, 0.03971],
    [0.039, 0.05366, 0.03789], [0.04, 0.06097, 0.03939], [0.041, 0.05832, 0.04043],
    [0.042, 0.05682, 0.03852], [0.043, 0.05783, 0.03581], [0.044, 0.05684, 0.03692],
    [0.045, 0.05781, 0.03605], [0.046, 0.0567, 0.03558], [0.047, 0.05482, 0.03464],
    [0.048, 0.05369, 0.03222], [0.049, 0.05132, 0.03075], [0.05, 0.05431, 0.03479],
    [0.051, 0.05314, 0.03205], [0.052, 0.05922, 0.03869], [0.053, 0.05578, 0.0343],
    [0.054, 0.05912, 0.03924], [0.055, 0.0558, 0.03552], [0.056, 0.05734, 0.04035],
    [0.057, 0.05665, 0.03726], [0.058, 0.05369, 0.03519], [0.059, 0.05322, 0.0348],
    [0.06, 0.05406, 0.03797], [0.061, 0.05353, 0.03487], [0.062, 0.05353, 0.03629],
    [0.063, 0.05432, 0.03517], [0.064, 0.05468, 0.03716], [0.065, 0.05446, 0.03813],
    [0.066, 0.05399, 0.03447], [0.067, 0.05395, 0.03564], [0.068, 0.05262, 0.03209],
    [0.069, 0.05403, 0.03536], [0.07, 0.05407, 0.03456], [0.071, 0.05509, 0.03811],
    [0.072, 0.05438, 0.03629], [0.073, 0.0546, 0.0355], [0.074, 0.0525, 0.03417],
    [0.075, 0.05601, 0.03858], [0.076, 0.05387, 0.03519], [0.077, 0.05389, 0.03449],
    [0.078, 0.05344, 0.03346], [0.079, 0.05455, 0.03563], [0.08, 0.05482, 0.03384],
    [0.081, 0.05325, 0.03191], [0.082, 0.05337, 0.0337], [0.083, 0.05232, 0.03339],
    [0.084, 0.05312, 0.03311], [0.085, 0.05406, 0.03293], [0.086, 0.05458, 0.03456],
    [0.087, 0.05517, 0.03721], [0.088, 0.05263, 0.03235], [0.089, 0.0541, 0.03487],
    [0.09, 0.05544, 0.03624], [0.091, 0.05607, 0.03605], [0.092, 0.05336, 0.03362],
    [0.093, 0.04984, 0.02565], [0.094, 0.05014, 0.02648], [0.095, 0.05254, 0.03014],
    [0.096, 0.06745, 0.03268], [0.097, 0.0887, 0.03758], [0.098, 0.09349, 0.03379],
    [0.099, 0.09534, 0.0317], [0.1, 0.09717, 0.03359], [0.1025, 0.10213, 0.03383],
    [0.105, 0.10355, 0.03466], [0.1075, 0.10371, 0.03264], [0.11, 0.10425, 0.03373],
    [0.1125, 0.10565, 0.035], [0.115, 0.10626, 0.03297], [0.1175, 0.10572, 0.03527],
    [0.12, 0.10184, 0.0269], [0.1225, 0.10376, 0.03078], [0.125, 0.10254, 0.03099],
    [0.1275, 0.10482, 0.03387], [0.13, 0.10584, 0.03059], [0.1325, 0.10498, 0.03303],
    [0.135, 0.10443, 0.03007], [0.1375, 0.10546, 0.03076], [0.14, 0.10382, 0.03029],
    [0.1425, 0.10198, 0.02997], [0.145, 0.10248, 0.02762], [0.1475, 0.10197, 0.02755]
])


Q2 = np.array([
    [0.0, 0.11848, 0.01197], [0.0025, 0.11858, 0.01135], [0.005, 0.11805, 0.01025],
    [0.0075, 0.11681, 0.01151], [0.01, 0.11879, 0.01113], [0.0125, 0.11814, 0.01063],
    [0.015, 0.11877, 0.01055], [0.016, 0.11645,0.01262], [0.017, 0.11788, 0.01119],
    [0.018, 0.11791, 0.01079], [0.019, 0.1191, 0.01099], [0.02, 0.11886, 0.01117],
    [0.021, 0.11792, 0.0111], [0.022, 0.11837, 0.01105], [0.023, 0.11866, 0.01168],
    [0.024, 0.11747, 0.01226], [0.025, 0.11818, 0.0117], [0.026, 0.11805, 0.00998],
    [0.027, 0.12044, 0.01111], [0.028, 0.11942, 0.01172],[0.029, 0.11735, 0.01205],
    [0.03, 0.11868, 0.01074], [0.031, 0.11922, 0.01236], [0.032, 0.11797, 0.01086],
    [0.033, 0.11941, 0.01045], [0.034, 0.11842, 0.01098], [0.035, 0.11741, 0.01173],
    [0.036, 0.12015, 0.0117], [0.037, 0.11784, 0.01158], [0.038, 0.11656, 0.01224],
    [0.039, 0.11767, 0.01081], [0.04, 0.11899, 0.01187], [0.041, 0.11831, 0.01115],
    [0.042, 0.11869, 0.01154], [0.043, 0.11874, 0.01076], [0.044, 0.11871, 0.01172],
    [0.045, 0.11884, 0.01081], [0.046, 0.11869, 0.01181], [0.047, 0.11785, 0.01212],
    [0.048, 0.12008, 0.01223], [0.049, 0.11968, 0.01139], [0.05, 0.11817, 0.01172],
    [0.051, 0.1188, 0.01149], [0.052, 0.11735, 0.01121], [0.053, 0.1187, 0.01004],
    [0.054, 0.11829, 0.01178], [0.055, 0.11791, 0.01063], [0.056, 0.1187, 0.0118],
    [0.057, 0.11888, 0.01179], [0.058, 0.1182, 0.01105], [0.059, 0.11836, 0.01158],
    [0.06, 0.11875, 0.01153], [0.061, 0.11672, 0.01268], [0.062, 0.11901, 0.01191],
    [0.063, 0.1193, 0.01115], [0.064, 0.11771, 0.01186], [0.065, 0.11936, 0.0123],
    [0.066, 0.11958, 0.01116], [0.067, 0.11953, 0.01096], [0.068, 0.11916, 0.01117],
    [0.069, 0.11788, 0.01175], [0.07, 0.12016, 0.01122], [0.071, 0.121, 0.01225],
    [0.072, 0.11938, 0.01168], [0.073, 0.11893, 0.01132], [0.074, 0.11755, 0.0103],
    [0.075, 0.12136, 0.01166], [0.076, 0.11986, 0.01051], [0.077, 0.11914, 0.01156],
    [0.078, 0.11962, 0.00981], [0.079, 0.1218, 0.01171], [0.08, 0.11919, 0.01139],
    [0.081, 0.12006, 0.01176], [0.082, 0.12451,0.01102], [0.083, 0.12188, 0.01087],
    [0.084, 0.12155, 0.01156], [0.085, 0.12132, 0.01053], [0.086, 0.12351, 0.01199],
    [0.087, 0.12088, 0.01259], [0.088, 0.1213, 0.01053], [0.089, 0.12059, 0.01129],
    [0.09, 0.12038, 0.01184], [0.091, 0.11986, 0.01171], [0.092, 0.12048, 0.01119],
    [0.093, 0.11952, 0.01126], [0.094, 0.11876, 0.01151], [0.095, 0.11949, 0.01033],
    [0.096, 0.12002, 0.01093], [0.097, 0.12035, 0.01113], [0.098, 0.12065, 0.01117],
    [0.099, 0.11892, 0.01082], [0.1, 0.11966, 0.01247], [0.1025, 0.11903, 0.01125],
    [0.105, 0.1192, 0.01183], [0.1075, 0.12011, 0.01087], [0.11, 0.11808, 0.01082],
    [0.1125, 0.11907, 0.01168], [0.115, 0.11894, 0.0106], [0.1175, 0.1195, 0.01152],
    [0.12, 0.11927, 0.01112], [0.1225, 0.11871, 0.01069], [0.125, 0.11826, 0.01135],
    [0.1275, 0.11872, 0.01054], [0.13, 0.11885, 0.0106], [0.1325, 0.11927, 0.01102],
    [0.135, 0.11861, 0.01109], [0.1375, 0.12027, 0.01152], [0.14, 0.12069, 0.00986],
    [0.1425, 0.12038, 0.01087], [0.145, 0.11967, 0.0104], [0.1475, 0.12006, 0.01135]
])

Q4 = np.array([
    [0.0, 0.05567, 0.01234], [0.0025, 0.05431, 0.01272], [0.005, 0.05451, 0.01062],
    [0.0075, 0.05453, 0.01225], [0.01, 0.05518, 0.01205], [0.0125, 0.05387, 0.01173],
    [0.015, 0.05418, 0.0128], [0.016, 0.0548, 0.01175], [0.017, 0.05481, 0.01178],
    [0.018, 0.05425, 0.01164], [0.019, 0.05402, 0.01127], [0.02, 0.05491, 0.01156],
    [0.021, 0.05539, 0.01167], [0.022, 0.05555, 0.01095], [0.023, 0.05515, 0.01081],
    [0.024, 0.05482, 0.0126], [0.025, 0.05459, 0.0133], [0.026, 0.05571, 0.01323],
    [0.027, 0.05619, 0.01091], [0.028, 0.05605, 0.01194], [0.029, 0.05746, 0.01178],
    [0.03, 0.05677, 0.01166], [0.031, 0.05612, 0.01164], [0.032, 0.05564, 0.0132],
    [0.033, 0.05459, 0.01185], [0.034, 0.0565, 0.01098], [0.035, 0.05646, 0.01154],
    [0.036, 0.05644, 0.01114], [0.037,0.05509, 0.01176], [0.038, 0.05717, 0.01014],
    [0.039, 0.05928, 0.01187], [0.04, 0.05898, 0.01234], [0.041, 0.06708, 0.01123],
    [0.042, 0.07983, 0.01267], [0.043, 0.07223, 0.01174], [0.044, 0.06373, 0.01209],
    [0.045, 0.06685, 0.01212], [0.046, 0.06377, 0.012], [0.047, 0.06994, 0.01094],
    [0.048, 0.07165, 0.0121], [0.049, 0.06851, 0.01288], [0.05, 0.0676, 0.01201],
    [0.051, 0.06128, 0.0123], [0.052, 0.06918, 0.01229], [0.053, 0.06467, 0.01351],
    [0.054, 0.06194, 0.01141], [0.055, 0.06405, 0.01144], [0.056, 0.06542, 0.01186],
    [0.057, 0.06546, 0.0118], [0.058, 0.06601, 0.01114], [0.059, 0.06168, 0.013],
    [0.06, 0.06045, 0.01216], [0.061, 0.05717, 0.01239], [0.062, 0.06049, 0.01221],
    [0.063, 0.06047, 0.01184], [0.064, 0.06188, 0.01036], [0.065, 0.06067, 0.01099],
    [0.066, 0.0599, 0.01228], [0.067, 0.05873, 0.01224], [0.068, 0.06213, 0.0117],
    [0.069, 0.06001, 0.01215], [0.07, 0.05832, 0.01171], [0.071, 0.05776, 0.01186],
    [0.072, 0.05911, 0.01221], [0.073, 0.0591, 0.01247], [0.074, 0.0573, 0.01144],
    [0.075, 0.05744, 0.01196], [0.076, 0.05704, 0.01208], [0.077, 0.05605, 0.01264],
    [0.078, 0.05693,0.01107], [0.079, 0.05707, 0.01186], [0.08, 0.05634, 0.0115],
    [0.081, 0.05671, 0.0112], [0.082, 0.05561, 0.01177], [0.083, 0.0564, 0.01122],
    [0.084, 0.05684, 0.01224], [0.085, 0.0567, 0.01222], [0.086, 0.05682, 0.01195],
    [0.087, 0.0569, 0.01201], [0.088, 0.05624, 0.01143], [0.089, 0.05782, 0.01206],
    [0.09, 0.05677, 0.01169], [0.091, 0.06054, 0.01101], [0.092, 0.05942, 0.0117],
    [0.093, 0.05885, 0.01068], [0.094, 0.0604, 0.01235], [0.095, 0.05684, 0.01156],
    [0.096, 0.05791, 0.01178], [0.097, 0.05937, 0.01228], [0.098, 0.06034, 0.01328],
    [0.099, 0.05852, 0.01109], [0.1, 0.05911, 0.01206], [0.1025, 0.05839, 0.01092],
    [0.105, 0.06028, 0.01212], [0.1075, 0.06115, 0.01188], [0.11, 0.06045, 0.01076],
    [0.1125, 0.06164, 0.01067], [0.115, 0.06058, 0.01073], [0.1175, 0.06252, 0.01154],
    [0.12, 0.06195, 0.01175], [0.1225, 0.06582, 0.01176], [0.125, 0.06679, 0.01153],
    [0.1275, 0.06752, 0.01146], [0.13, 0.06966, 0.0124], [0.1325, 0.07271, 0.0119],
    [0.135, 0.07651, 0.01273], [0.1375, 0.07928, 0.01295], [0.14, 0.08183, 0.01288],
    [0.1425, 0.08635, 0.01159], [0.145, 0.08775, 0.01357], [0.1475, 0.09069,0.01309]
])
### J6 Bias Conversion
Q1[:, 0] = (Q1[:, 0])*1000
Q2[:, 0] = (Q2[:, 0])*1000
Q4[:, 0] = (Q4[:, 0])*1000


f = 4.604
# f = 1
Al_gap = 380e-6
DAC_Al = 1e5*Al_gap/0.952
plt.errorbar(Q1[:, 0]*f, Q1[:, 1], yerr=Q1[:, 2]/np.sqrt(150), color='b', label='Q1')
plt.errorbar(Q2[:, 0]*f, Q2[:, 1], yerr=Q2[:, 2]/np.sqrt(150), color='r', label='Q2')
plt.errorbar(Q4[:, 0]*f, Q4[:, 1], yerr=Q4[:, 2]/np.sqrt(150), color='y', label='Q4')

plt.axvline(x=DAC_Al * f, color='k', linestyle='--', linewidth=4, label='JJ Al Gap')

plt.xlabel('Radiator Josephson Frequency (GHz)')
plt.ylabel('P1')
plt.yscale('log')
plt.grid()
plt.legend(loc=1)
# plt.xlim([0, 1500])
# plt.ylim([10, 100000])
plt.show()


