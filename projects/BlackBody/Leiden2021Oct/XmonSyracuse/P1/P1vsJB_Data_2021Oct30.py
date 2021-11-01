"""
P1 for Q123 at different J7 Bias
Data:
Z:\mcdermott-group\data\Antenna_Temporary\SUXmon\Liu\VitoChip1\P12021Oct30_Q123WithJ7\P1_J7_Q1_Chunk0\MATLABData
Z:\mcdermott-group\data\Antenna_Temporary\SUXmon2\Liu\VitoChip2\P12021Oct31_Q2WithJ7OnChip_TimeDomain\P1_J7_Q2_Chunk0\MATLABData


"""
import noiselib
import matplotlib.pyplot as plt
import numpy as np

Q1 = np.array([
 [0.0, 0.03296, 0.03653], [0.005, 0.03417, 0.03857], [0.01, 0.03145, 0.03359],
 [0.015, 0.03268, 0.03902], [0.02, 0.02601, 0.02207], [0.025, 0.03519, 0.03883],
 [0.0275, 0.03349, 0.04031], [0.03, 0.03665, 0.04155], [0.0325, 0.03752, 0.04382],
 [0.0349, 0.03621, 0.04404], [0.0374, 0.0385, 0.04965], [0.04, 0.03578, 0.04663],
 [0.041, 0.03648, 0.04741], [0.042, 0.03691, 0.03972], [0.043, 0.03962, 0.04572],
 [0.044, 0.03688, 0.04542], [0.045, 0.03845, 0.04402], [0.046, 0.03746, 0.04399],
 [0.047, 0.04157, 0.04695], [0.048, 0.04062, 0.04638], [0.049, 0.04157, 0.04509],
 [0.05, 0.0434, 0.04627], [0.051, 0.04403, 0.04945], [0.052, 0.0438, 0.04876],
 [0.053, 0.04113, 0.0472], [0.054, 0.0424, 0.04725], [0.055, 0.0416, 0.04491],
 [0.056, 0.048, 0.0499], [0.057, 0.04244, 0.04857], [0.058, 0.0441, 0.04691],
 [0.059, 0.04469, 0.04914], [0.06, 0.03996, 0.04291], [0.061, 0.04102, 0.04606],
 [0.062, 0.04064, 0.04254], [0.063, 0.03807, 0.04247], [0.064, 0.03612, 0.04111],
 [0.065, 0.03399, 0.03769], [0.066, 0.03451, 0.0415], [0.067, 0.03534, 0.04025],
 [0.068, 0.03674, 0.04271], [0.069, 0.03682, 0.03805], [0.07, 0.03309, 0.03869],
 [0.07, 0.03608, 0.04099], [0.0725, 0.03311, 0.03889], [0.075, 0.03323, 0.04211],
 [0.0775, 0.03643, 0.03882], [0.08, 0.0364, 0.0393], [0.0825, 0.03214, 0.03758],
 [0.085, 0.03649, 0.03573], [0.0875, 0.03365, 0.03979], [0.09, 0.03851, 0.04388],
 [0.0925, 0.03892, 0.04336], [0.095, 0.03747, 0.04245], [0.0975, 0.04169, 0.04078],
 [0.1, 0.04264, 0.04303], [0.105, 0.03915, 0.03847], [0.11, 0.0417, 0.04462],
 [0.115, 0.04273, 0.04618], [0.12, 0.04415, 0.04905], [0.125, 0.04491, 0.04583],
 [0.13, 0.04185, 0.04657], [0.135, 0.04245, 0.04605], [0.14, 0.04432, 0.04797],
 [0.145, 0.04727, 0.05072], [0.15, 0.04584, 0.04541], [0.155, 0.04691, 0.04815],
 [0.16, 0.05009, 0.04591], [0.165, 0.04915, 0.04728], [0.17, 0.051, 0.05072],
 [0.175, 0.05163, 0.05037], [0.18, 0.05159, 0.04983], [0.185, 0.05367, 0.05179],
 [0.19, 0.05506, 0.0511], [0.195, 0.05426, 0.05038], [0.2, 0.05634, 0.05144],
 [0.205, 0.05618, 0.04866], [0.21, 0.05506, 0.0489], [0.215, 0.05751, 0.05035],
 [0.22,0.0553, 0.04791], [0.225, 0.05939, 0.0531], [0.23, 0.05863, 0.04937],
 [0.235, 0.05656, 0.05211], [0.24, 0.05925, 0.05108], [0.245, 0.05952, 0.05339]
])


Q2 = np.array([
 [0.0, 0.02125, 0.02365], [0.005, 0.0213, 0.02239], [0.01, 0.02175, 0.02226],
 [0.015, 0.02221, 0.02478], [0.02, 0.02248, 0.0191], [0.025, 0.02384, 0.02375],
 [0.0275, 0.02165, 0.02594], [0.03, 0.0225, 0.02217], [0.0325, 0.0285, 0.02379],
 [0.0349, 0.02634, 0.02444], [0.0374, 0.03124, 0.02973], [0.04, 0.02589,0.02736],
 [0.041, 0.02811, 0.0286], [0.042, 0.02801, 0.02753], [0.043, 0.02834, 0.02889],
 [0.044, 0.02851, 0.02859], [0.045, 0.03064, 0.02764], [0.046, 0.02486,0.0304],
 [0.047, 0.03177, 0.02987], [0.048, 0.03367, 0.02954], [0.049, 0.03227, 0.02847],
 [0.05, 0.03899, 0.03076], [0.051, 0.0347, 0.02851], [0.052, 0.04071, 0.02721],
 [0.053, 0.03472, 0.02946], [0.054, 0.03767, 0.03058], [0.055, 0.04054, 0.03181],
 [0.056, 0.03892, 0.02971], [0.057, 0.036, 0.03096], [0.058, 0.03607, 0.03005],
 [0.059, 0.03552, 0.02628], [0.06, 0.03329, 0.03125], [0.061, 0.0314, 0.02676],
 [0.062, 0.02399, 0.02676], [0.063, 0.02901, 0.02492], [0.064, 0.02538, 0.02743],
 [0.065, 0.02739, 0.02845], [0.066, 0.02856, 0.02605], [0.067, 0.02374, 0.02566],
 [0.068, 0.02747, 0.02536], [0.069, 0.02825, 0.02531], [0.07, 0.02428, 0.02698],
 [0.07, 0.02587, 0.02628], [0.0725, 0.02627, 0.02745], [0.075, 0.0234, 0.02526],
 [0.0775, 0.02351, 0.02462], [0.08, 0.02351, 0.0264], [0.0825, 0.02471, 0.02617],
 [0.085, 0.02494, 0.0253], [0.0875, 0.02627, 0.02144], [0.09, 0.0234, 0.02319],
 [0.0925, 0.02784, 0.02535], [0.095, 0.02719, 0.02603], [0.0975, 0.02464, 0.02725],
 [0.1, 0.02669, 0.02435], [0.105, 0.02495, 0.02599], [0.11, 0.02379, 0.02724],
 [0.115, 0.02726, 0.03004], [0.12, 0.02515, 0.02709], [0.125, 0.0261, 0.02595],
 [0.13, 0.02687, 0.02675], [0.135, 0.02984, 0.02989], [0.14, 0.03, 0.02845],
 [0.145, 0.03483, 0.02821], [0.15, 0.0315, 0.02912], [0.155, 0.03397, 0.02765],
 [0.16, 0.03957, 0.03101], [0.165, 0.03538, 0.02917], [0.17, 0.04065, 0.02988],
 [0.175, 0.04042, 0.03257], [0.18, 0.0409, 0.02825], [0.185, 0.04018, 0.03138],
 [0.19, 0.04567, 0.02907], [0.195, 0.043, 0.02884], [0.2, 0.04457, 0.02895],
 [0.205, 0.04263, 0.02933], [0.21, 0.04644, 0.03002], [0.215, 0.04742, 0.02839],
 [0.22, 0.04301, 0.02741], [0.225, 0.0496, 0.0299], [0.23, 0.04821, 0.03156],
 [0.235, 0.04851, 0.03085], [0.24, 0.05147, 0.03087], [0.245, 0.05051, 0.03112]
])

Q3 = np.array([
 [0.0, 0.06321, 0.01429], [0.005, 0.06347, 0.0123], [0.01, 0.06639, 0.0122],
 [0.015, 0.06366, 0.01527], [0.02, 0.06174, 0.01432], [0.025, 0.06406, 0.01229],
 [0.0275, 0.0632, 0.01344], [0.03, 0.06385, 0.01405], [0.0325, 0.06747, 0.01266],
 [0.0349, 0.0641, 0.01295], [0.0374, 0.06561, 0.01346], [0.04, 0.06786,0.01321],
 [0.041, 0.06476, 0.01443], [0.042, 0.0648, 0.01322], [0.043, 0.06553, 0.01392],
 [0.044, 0.06579, 0.01432], [0.045, 0.06592, 0.01583], [0.046, 0.06467,0.01271],
 [0.047, 0.06498, 0.01384], [0.048, 0.06566, 0.01364], [0.049, 0.06566, 0.01294],
 [0.05, 0.06415, 0.01237], [0.051, 0.06606, 0.01362], [0.052, 0.06699,0.013],
 [0.053, 0.06477, 0.01284], [0.054, 0.06324, 0.01371], [0.055, 0.06244, 0.01351],
 [0.056, 0.06452, 0.01421], [0.057, 0.06402, 0.01395], [0.058, 0.06408, 0.01207],
 [0.059, 0.06301, 0.01217], [0.06, 0.06219, 0.01237], [0.061, 0.06252, 0.01321],
 [0.062, 0.06349, 0.01241], [0.063, 0.0649, 0.01407], [0.064, 0.06343, 0.01292],
 [0.065, 0.06383, 0.0134], [0.066, 0.06271, 0.01363], [0.067, 0.06419, 0.01373],
 [0.068, 0.06551, 0.01354], [0.069, 0.0625, 0.01509], [0.07, 0.06416, 0.01307],
 [0.07, 0.06437, 0.01287], [0.0725, 0.06271, 0.01286], [0.075, 0.06451, 0.01426],
 [0.0775, 0.06353, 0.01386], [0.08, 0.06599, 0.01505], [0.0825, 0.0664, 0.01324],
 [0.085, 0.06399, 0.01436], [0.0875, 0.06501, 0.01314], [0.09, 0.06385, 0.01469],
 [0.0925, 0.06529, 0.0138], [0.095, 0.06512, 0.01229], [0.0975, 0.0633, 0.01324],
 [0.1, 0.06321, 0.01532], [0.105, 0.06405, 0.014], [0.11, 0.06589, 0.01409],
 [0.115, 0.06385, 0.01253], [0.12, 0.06562, 0.01355], [0.125, 0.06744, 0.01337],
 [0.13, 0.06634, 0.01301], [0.135, 0.06623, 0.01497], [0.14, 0.06543, 0.01459],
 [0.145, 0.06694, 0.01331], [0.15, 0.06707, 0.01354], [0.155, 0.06782, 0.01376],
 [0.16, 0.06794, 0.01459], [0.165, 0.06998, 0.01394], [0.17, 0.06726, 0.01402],
 [0.175, 0.06879, 0.01429], [0.18, 0.06926, 0.01311], [0.185, 0.06864, 0.01409],
 [0.19, 0.0696, 0.013], [0.195, 0.06912, 0.01296], [0.2, 0.06913, 0.01396],
 [0.205, 0.07002, 0.01234], [0.21, 0.07105, 0.01396], [0.215, 0.07198, 0.01394],
 [0.22,0.07124, 0.0137], [0.225, 0.07404, 0.01314], [0.23, 0.07169, 0.01234],
 [0.235, 0.07373, 0.01288], [0.24, 0.07183, 0.01184], [0.245, 0.07353, 0.01184]
])

Q2_Chip2 = np.array([
 [0.0, 0.01258, 0.00543], [0.005, 0.01258, 0.00431], [0.01, 0.01306, 0.00468],
 [0.015, 0.01312, 0.00575], [0.02, 0.01265, 0.00446], [0.025, 0.01222, 0.00462],
 [0.0275, 0.0139, 0.00698], [0.03, 0.01253, 0.00343], [0.0325, 0.01405, 0.00441],
 [0.0349, 0.01277, 0.00395], [0.0374, 0.0127, 0.0044], [0.04, 0.01276, 0.0041],
 [0.041, 0.01286, 0.00438], [0.042, 0.01386, 0.0057], [0.043, 0.01468, 0.0055],
 [0.044, 0.01267, 0.00501], [0.045, 0.01279, 0.00465], [0.046, 0.0151, 0.00635],
 [0.047, 0.01375, 0.00621], [0.048, 0.01381, 0.00516], [0.049, 0.01361, 0.00391],
 [0.05, 0.01454, 0.00568], [0.051, 0.01274, 0.00393], [0.052, 0.01294, 0.00387],
 [0.053, 0.0143, 0.0054], [0.054, 0.01449, 0.00469], [0.055, 0.01406, 0.00508],
 [0.056, 0.013, 0.0039], [0.057, 0.0127, 0.00363], [0.058, 0.0145, 0.00428],
 [0.059, 0.01507, 0.00646], [0.06, 0.01579, 0.00645], [0.061, 0.01358, 0.00504],
 [0.062, 0.01295, 0.00324], [0.063, 0.01341, 0.00378], [0.064, 0.0145, 0.00569],
 [0.065, 0.01386, 0.00416], [0.066, 0.01442, 0.00418], [0.067, 0.01436, 0.00516],
 [0.068, 0.01379, 0.00401], [0.069, 0.01312, 0.00379], [0.07, 0.01279, 0.00402],
 [0.07, 0.01415, 0.00449], [0.0725, 0.01438, 0.00545], [0.075, 0.0154, 0.00442],
 [0.0775, 0.0147, 0.00436], [0.08, 0.01379, 0.00432], [0.0825, 0.01392, 0.00377],
 [0.085, 0.01466, 0.00502], [0.0875, 0.01394, 0.00304], [0.09, 0.01478, 0.00439],
 [0.0925, 0.01532, 0.00429], [0.095, 0.01599, 0.00679], [0.0975, 0.0146, 0.00426],
 [0.1, 0.01639, 0.00489], [0.105, 0.0158, 0.00496], [0.11, 0.01593, 0.00488],
 [0.115, 0.01692, 0.00874], [0.12, 0.0165, 0.00435], [0.125, 0.01775, 0.00688],
 [0.13, 0.01742, 0.00391], [0.135, 0.01841, 0.00482], [0.14, 0.01786, 0.00405],
 [0.145, 0.0204, 0.00465], [0.15, 0.01913, 0.00601], [0.155, 0.02037, 0.00551],
 [0.16, 0.02061, 0.00717], [0.165, 0.02055, 0.00431], [0.17, 0.02068, 0.00536],
 [0.175, 0.0203, 0.00472], [0.18, 0.02163, 0.00425], [0.185, 0.02244, 0.00496],
 [0.19, 0.02372, 0.00433], [0.195, 0.02457, 0.00712], [0.2, 0.0231, 0.00436],
 [0.205, 0.02489, 0.00501], [0.21, 0.02522, 0.00623], [0.215, 0.02603, 0.00533],
 [0.22, 0.0264, 0.00566], [0.225, 0.02638, 0.00511], [0.23, 0.02803, 0.00472],
 [0.235, 0.02781, 0.00486], [0.24, 0.02795, 0.00433], [0.245, 0.02812, 0.00468]
])
### J7 Bias Conversion
Q1[:, 0] = (Q1[:, 0])*1000
Q2[:, 0] = (Q2[:, 0])*1000
Q3[:, 0] = (Q3[:, 0])*1000
Q2_Chip2[:, 0] = (Q2_Chip2[:, 0])*1000


f = 4.604
# f = 1
Al_gap = 380e-6
DAC_Al = 1e5*Al_gap/0.952
plt.errorbar(Q1[:, 0]*f, Q1[:, 1], yerr=Q1[:, 2]/np.sqrt(100), color='b', label='Q1_SteadyState_OffChip')
plt.errorbar(Q2[:, 0]*f, Q2[:, 1], yerr=Q2[:, 2]/np.sqrt(100), color='r', label='Q2_SteadyState_OffChip')
# plt.errorbar(Q3[:, 0]*f, Q3[:, 1], yerr=Q3[:, 2]/np.sqrt(100), color='y', label='Q3')
plt.errorbar(Q2_Chip2[:, 0]*f, Q2_Chip2[:, 1], yerr=Q2_Chip2[:, 2]/np.sqrt(50), color='g', label='Q2_AfterPoison_OnChip')

plt.axvline(x=DAC_Al * f, color='k', linestyle='--', linewidth=4, label='JJ Al Gap')

plt.xlabel('Radiator Josephson Frequency (GHz)')
# plt.xlabel('Radiator Josephson Bias (mDAC)')
plt.ylabel('P1')
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which="both")
plt.legend(loc=2)
# plt.xlim([0, 1500])
# plt.ylim([10, 100000])
plt.show()



