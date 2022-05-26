### To analyze the P1 vs J2 Bias data
### src: Z:\mcdermott-group\data\BlackBody\Circmon\LIU\CW20180514A_Ox2\JJRadiatorP1_2021Aug25_HighDensity\

from antennalib import P1_JSweep
import matplotlib.pyplot as plt
import numpy as np
import copy


J2_Bias_Q1 = np.array([
    0., 4., 8., 12., 15., 15.5, 16., 16.5, 17., 17.5, 18.,
    18.5, 19., 19.5, 20., 20.5, 21., 21.5, 22., 22.5, 23., 23.5,
    24., 24.5, 25., 25.5, 26., 26.5, 27., 27.5, 28., 28.5, 29.,
    29.5, 30., 30.5, 31., 31.5, 32., 32.5, 33., 33.5, 34., 34.5,
    35., 35.5, 36., 36.5, 37., 37.5, 38., 38.5, 39., 39.5, 40.,
    40.5, 41., 41.5, 42., 42.5, 43., 43.5, 44., 44.5, 45., 49.,
    53., 57., 61., 65., 69., 73., 77., 81., 85., 89., 93., 97.
])
J2_Bias_Q2 = np.array([
    0., 4., 8., 12., 16., 20., 24., 28., 32., 36., 40.,
    44., 48., 52., 56., 60., 64., 68., 70., 70.5, 71., 71.5,
    72., 72.5, 73., 73.5, 74., 74.5, 75., 75.5, 76., 76.5, 77.,
    77.5, 78., 78.5, 79., 79.5, 80., 80.5, 81., 81.5, 82., 82.5,
    83., 83.5, 84., 84.5, 85., 85.5, 86., 86.5, 87., 87.5, 88.,
    88.5, 89., 89.5, 90., 90.5, 91., 91.5, 92., 92.5, 93., 93.5,
    94., 94.5, 95., 95.5, 96., 96.5, 97., 97.5, 98., 98.5, 99., 99.5
])
J2_Bias_Q3 = np.array([
    0., 0.5, 1., 1.5, 2., 2.5, 3., 3.5, 4., 4.5, 5.,
    5.5, 6., 6.5, 7., 7.5, 8., 8.5, 9., 9.5, 10., 10.5,
    11., 11.5, 12., 12.5, 13., 13.5, 14., 14.5, 15., 15.5, 16.,
    16.5, 17., 17.5, 18., 18.5, 19., 19.5, 20., 20.5, 21., 21.5,
    22., 22.5, 23., 23.5, 24., 24.5, 25., 25.5, 26., 26.5, 27.,
    27.5, 28., 28.5, 29., 29.5, 30., 34., 38., 42., 46., 50.,
    54., 58., 62., 66., 70., 74., 78., 82., 86., 90., 94., 98.
])
J2_Bias_Q4 = np.array([
    0., 4., 8., 12., 16., 20., 24., 28., 32., 35., 35.5,
    36., 36.5, 37., 37.5, 38., 38.5, 39., 39.5, 40., 40.5, 41.,
    41.5, 42., 42.5, 43., 43.5, 44., 44.5, 45., 45.5, 46., 46.5,
    47., 47.5, 48., 48.5, 49., 49.5, 50., 50.5, 51., 51.5, 52.,
    52.5, 53., 53.5, 54., 54.5, 55., 55.5, 56., 56.5, 57., 57.5,
    58., 58.5, 59., 59.5, 60., 60.5, 61., 61.5, 62., 62.5, 63.,
    63.5, 64., 64.5, 65., 69., 73., 77., 81., 85., 89., 93., 97.
])

P1_J2_Q1 = np.array([
    0.09151478, 0.08703182, 0.0882618, 0.08794933, 0.08818165,
    0.0889833, 0.08665481, 0.08788676, 0.09349549, 0.09210614,
    0.09115154, 0.09756099, 0.0937575, 0.09053581, 0.09270245,
    0.09135221, 0.09693043, 0.09922347, 0.09521829, 0.09515874,
    0.09620075, 0.09641336, 0.0897389, 0.0831632, 0.08954523,
    0.09410053, 0.1063627, 0.13489624, 0.1714701, 0.18467862,
    0.17769778, 0.15978768, 0.14279426, 0.136362, 0.12170757,
    0.12026267, 0.1124961, 0.11121191, 0.10623433, 0.10359356,
    0.10361798, 0.10084759, 0.09779605, 0.10016808, 0.09887265,
    0.09722523, 0.1045435, 0.10062217, 0.10050382, 0.10062389,
    0.09647612, 0.09428073, 0.09678772, 0.09206999, 0.09520828,
    0.09783997, 0.09620696, 0.09292284, 0.09237972, 0.09231662,
    0.09246814, 0.09043257, 0.09673941, 0.09099237, 0.09039802,
    0.08834101, 0.09690655, 0.09679089, 0.09220214, 0.09922646,
    0.09915293, 0.09505855, 0.09302409, 0.09651796, 0.09162362,
    0.0954987, 0.09871815, 0.09382241])

P1_J2_Q2 = np.array([
    0.03221857, 0.03171556, 0.03314561, 0.03160513, 0.03256905,
    0.0334588, 0.03193355, 0.03310597, 0.03330728, 0.03287312,
    0.03435965, 0.03334423, 0.03221563, 0.03298754, 0.03251722,
    0.03347501, 0.03336158, 0.0323123, 0.03374858, 0.03361437,
    0.03339633, 0.03347469, 0.03250942, 0.03333688, 0.03329429,
    0.03458953, 0.0345589, 0.03405791, 0.0344945, 0.03401392,
    0.03417905, 0.03680676, 0.03519604, 0.03523518, 0.03515189,
    0.03498405, 0.0360857, 0.03462048, 0.0349227, 0.036426,
    0.03686152, 0.03609282, 0.03729288, 0.03625132, 0.03697142,
    0.03749846, 0.03622269, 0.03654815, 0.03662906, 0.03672985,
    0.03550154, 0.03657593, 0.03581621, 0.03706069, 0.03585106,
    0.03544399, 0.03496945, 0.03551317, 0.03404684, 0.03474205,
    0.03572859, 0.03525251, 0.03399945, 0.03548398, 0.0330383,
    0.03288229, 0.03442139, 0.03403903, 0.03412732, 0.03365845,
    0.03292763, 0.03420683, 0.03379292, 0.03339642, 0.03183218,
    0.03363377, 0.03462074, 0.0338995])

P1_J2_Q3 = np.array([
    0.35866972, 0.35993776, 0.35934135, 0.36007218, 0.35824569,
    0.35511218, 0.35877801, 0.35622436, 0.35882495, 0.35881574,
    0.35664185, 0.35847286, 0.36660959, 0.36271326, 0.36285709,
    0.37514232, 0.40016205, 0.42369837, 0.40673112, 0.39382693,
    0.3764224, 0.37314463, 0.36917056, 0.36920665, 0.37272307,
    0.35957246, 0.35683931, 0.37470522, 0.45932988, 0.60847636,
    0.70203152, 0.76432586, 0.77942278, 0.79431034, 0.78592739,
    0.77277292, 0.72812406, 0.68098695, 0.59170952, 0.50345913,
    0.44443252, 0.42040014, 0.40696555, 0.39151354, 0.38456568,
    0.37705724, 0.36862108, 0.38079186, 0.38498037, 0.39767371,
    0.40597892, 0.39638822, 0.39689778, 0.39088347, 0.38942494,
    0.37643967, 0.37927475, 0.38415159, 0.37650834, 0.37355905,
    0.37488226, 0.36635771, 0.37851994, 0.37119994, 0.3803977,
    0.42273087, 0.40457725, 0.40370722, 0.40011052, 0.39513678,
    0.39614748, 0.39793719, 0.49240824, 0.60858279, 0.63472405,
    0.63970019, 0.6475761, 0.65051623])

P1_J2_Q4 = np.array([
    0.02379928, 0.02462802, 0.02353492, 0.02403066, 0.02411472,
    0.02398406, 0.02387884, 0.02979766, 0.03140893, 0.032198,
    0.03374106, 0.03469236, 0.03260121, 0.03148727, 0.0305883,
    0.02950887, 0.03141353, 0.03429558, 0.03468443, 0.03938188,
    0.04359392, 0.04407681, 0.04567099, 0.04689744, 0.05095649,
    0.05582051, 0.05683922, 0.06269061, 0.06205835, 0.06280797,
    0.05756588, 0.05518739, 0.05395225, 0.05868567, 0.03942157,
    0.05527995, 0.05589302, 0.05530485, 0.05538489, 0.05641155,
    0.05855407, 0.06362561, 0.06962735, 0.07311105, 0.07165543,
    0.07411966, 0.07214671, 0.07155449, 0.07200671, 0.07270898,
    0.07012878, 0.0677421, 0.06433914, 0.05715432, 0.055365,
    0.05216418, 0.05126228, 0.04945946, 0.046659, 0.04610384,
    0.04521347, 0.04190738, 0.0410773, 0.03880886, 0.03899347,
    0.03697249, 0.03577604, 0.03639505, 0.03429648, 0.03633243,
    0.03253057, 0.03053162, 0.02954724, 0.0282534, 0.02852569,
    0.02966221, 0.02907174, 0.02941831])

# print('J2_Bias_Q1=', J2_Bias_Q1)
# print('J2_Bias_Q2=', J2_Bias_Q2)
# print('J2_Bias_Q3=', J2_Bias_Q3)
# print('J2_Bias_Q4=', J2_Bias_Q4)
# print('P1_J2_Q1=', P1_J2_Q1)
# print('P1_J2_Q2=', P1_J2_Q2)
# print('P1_J2_Q3=', P1_J2_Q3)
# print('P1_J2_Q4=', P1_J2_Q4)

# plt.plot(J2_Bias_Q1, P1_J2_Q1, label='Q1')
# plt.plot(J2_Bias_Q2, P1_J2_Q2, label='Q2')
# plt.plot(J2_Bias_Q3, P1_J2_Q3, label='Q3')
# plt.plot(J2_Bias_Q4, P1_J2_Q4, label='Q4')
# plt.xlabel('J2 Bias (mDAC)')
# plt.ylabel('P1')
# # plt.yscale('log')
# plt.grid()
# plt.legend()
# plt.show()

plt.plot(J2_Bias_Q1*4.8, P1_J2_Q1, 'b', label='Q1')
plt.plot(J2_Bias_Q2*4.8, P1_J2_Q2, 'r', label='Q2')
plt.plot(J2_Bias_Q3*4.8, P1_J2_Q3, 'k', label='Q3')
plt.plot(J2_Bias_Q4*4.8, P1_J2_Q4, 'y', label='Q4')
plt.xlabel('J2 Bias (GHz)')
plt.ylabel('P1')
# plt.yscale('log')
plt.grid()
plt.legend()
plt.show()