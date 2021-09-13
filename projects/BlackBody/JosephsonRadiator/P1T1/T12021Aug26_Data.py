### To analyze the P1 vs J2 Bias data
### src: Z:\mcdermott-group\data\BlackBody\Circmon\LIU\CW20180514A_Ox2\JJRadiatorT1_2021Aug26_HighDensity\

from antennalib import P1_JSweep
import matplotlib.pyplot as plt
import numpy as np
import copy


J2_Bias_Q1 = np.array([0, 10, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 50, 60, 70, 80, 90])
J2_Bias_Q2 = np.array([0, 10, 20, 30, 40, 50, 60, 70, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
J2_Bias_Q3 = np.array([0, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 35, 45, 55, 65, 75, 85, 95])
J2_Bias_Q4 = np.array([0, 10, 20, 30, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 70, 80, 90])

T1_J2_Q1 = np.array([20.831678115932576, 20.831152152129977, 22.648565161668444, 24.24226746372009, 23.51635610508561, 22.859458476588003, 11.947189748969604, 7.3921969965767964, 8.1583270042740601, 8.2945990038021833, 10.185989609935836, 12.723646399810224, 14.55338786693043, 13.86050536513088, 14.678702400801086, 16.035804152037805, 15.516198094851823, 9.841065999798019, 17.0538229630783, 17.578503880792312, 17.244175693147561, 9.8936344475622899, 7.5617823363183234, 15.883200770241919, 9.6125654651980259, 16.839421069639648, 16.533857387697648, 7.5071371766153749])
T1_J2_Q2 = np.array([10.230950182808948, 9.8494305195166056, 10.641139199763936, 10.172732856234818, 11.235318998019242, 11.151883621689869, 10.578941941351832, 10.354241775471609, 10.421352073135671, 9.5254212764896486, 10.296740741041305, 9.866965821453098, 10.649947744459693, 10.84045772256373, 10.678306540354301, 11.2860146062394, 9.9082005253054195, 10.436189193880367, 11.32824890479386, 10.144432964109875, 9.9733300869561372, 11.203218778653072, 11.338924416314359, 11.121118126568609, 10.5919924639197, 10.340413692969211, 9.9994621338869401, 10.735364349350441, 10.416108986472091, 10.358009827315046, 9.4953059996556863, 9.5276397226331007, 10.721954897265299])
T1_J2_Q3 = np.array([78.560401202877273, 64.598890712547359, 64.598890712547359, 65.374407794365823, 64.408862664057438, 95.779109931072824, 76.127800656441906, 59.062701726575042, 76.54461757207936, 69.792306114400802, 68.217926614770803, 81.721933272845774, 111.06122014736114, 273.10607372080472, 1898.2962176754183, 206.10430854707172, 129.62422619538265, 83.539503078737212, 79.87847866209701, 65.475713426353167, 65.383821972104798, 59.468411980315523, 64.916679438515516, 55.407808272185676, 55.609017084479206, 70.950852510724332, 66.412674641673107, 89.481390968580271, 144.87466671198422, 394.51810534381468])
T1_J2_Q4 = np.array([19.111808698967319, 15.773058618831827, 19.933397089893784, 15.95495797415297, 16.18903524110166, 22.116299895512036, 18.201922921793638, 17.847687755539827, 20.568712459255153, 17.482288558107307, 19.476738350010297, 16.678390202477498, 15.346711892518899, 18.661051010085046, 17.184775818080638, 17.095030614122589, 17.916100020928805, 16.909962242936718, 18.428055233613229, 16.119263159582758, 17.854631716105157, 18.219723888576841, 17.357015888411482, 18.026604945484173, 17.669564961307749, 19.320084445633675, 18.552422178444619, 18.412166721279657])


plt.plot(J2_Bias_Q1, T1_J2_Q1, label='Q1')
plt.plot(J2_Bias_Q2, T1_J2_Q2, label='Q2')
# plt.plot(J2_Bias_Q3, T1_J2_Q3, label='Q3')
plt.plot(J2_Bias_Q4, T1_J2_Q4, label='Q4')
plt.xlabel('J2 Bias (mDAC)')
plt.ylabel('T1 (us)')
# plt.yscale('log')
plt.grid()
plt.legend()
plt.show()