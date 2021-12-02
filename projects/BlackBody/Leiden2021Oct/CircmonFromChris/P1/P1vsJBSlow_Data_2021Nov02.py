"""
P1 for Q1, Q2, Q4 at different J6 Bias with Sim
Data:
Z:\mcdermott-group\data\Antenna_Temporary\Circmon\Liu\CW20180514A_Ox2\2021Nov02_QB124_P1_J6Radiator_Sim
"""
import noiselib
import matplotlib.pyplot as plt
import numpy as np


Q1 = np.array([
    [0.0, 0.0512, 0.0453], [0.01, 0.04579, 0.03925], [0.02, 0.04951, 0.03798],
    [0.03, 0.0453, 0.03717], [0.04, 0.04614, 0.037], [0.05, 0.04907, 0.0367],
    [0.06, 0.05046, 0.03851], [0.065, 0.04832, 0.03687], [0.07, 0.046, 0.03569],
    [0.075, 0.04907, 0.03904], [0.08, 0.04824, 0.03981], [0.085, 0.04747, 0.03556],
    [0.09, 0.04501, 0.03664], [0.095,0.04318, 0.03681], [0.1, 0.04835, 0.03912],
    [0.105, 0.04765, 0.03564], [0.11, 0.04581, 0.032], [0.115, 0.03486, 0.02466],
    [0.12, 0.06003, 0.04422], [0.125, 0.11833, 0.06081], [0.13, 0.09608, 0.06108],
    [0.135, 0.08388, 0.05895], [0.14, 0.07552, 0.05353], [0.145, 0.06188, 0.05147],
    [0.15, 0.06496, 0.04713], [0.155, 0.0633, 0.05232], [0.16, 0.05763, 0.0465],
    [0.165, 0.06486, 0.05488], [0.17, 0.05986, 0.05046], [0.175, 0.06852, 0.05555],
    [0.18, 0.06201, 0.04722], [0.185,0.06208, 0.04507], [0.19, 0.06276, 0.0505],
    [0.195, 0.06286, 0.04737], [0.2, 0.06777, 0.05582], [0.205, 0.0671, 0.05032],
    [0.21, 0.06446, 0.0502], [0.215, 0.06868, 0.06355], [0.22, 0.06742, 0.06123],
    [0.225, 0.06291, 0.05628], [0.23, 0.06444, 0.05671], [0.235, 0.06559, 0.05822],
    [0.24, 0.06241, 0.05176], [0.245, 0.06224, 0.05372], [0.25, 0.05749, 0.05423],
    [0.255, 0.06103, 0.04797], [0.26, 0.05806, 0.04942], [0.265, 0.06123, 0.05387],
    [0.27, 0.0598, 0.05103], [0.275,0.05846, 0.05307], [0.28, 0.05364, 0.04969],
    [0.285, 0.05732, 0.05108], [0.29, 0.05817, 0.04947], [0.295, 0.05714, 0.0467],
    [0.3, 0.0585, 0.04868], [0.305, 0.05593, 0.05258], [0.31, 0.05884, 0.04943],
    [0.315, 0.05166, 0.04768], [0.32, 0.05448, 0.0463], [0.325, 0.05711, 0.05164],
    [0.33, 0.05781, 0.05263], [0.335, 0.05918, 0.04651], [0.34, 0.05447, 0.04523],
    [0.345, 0.05414, 0.04871], [0.35, 0.05798, 0.05065], [0.355, 0.05898, 0.04817],
    [0.36, 0.05662, 0.04696], [0.365, 0.05342, 0.0488], [0.37, 0.05621, 0.04741],
    [0.375, 0.05809, 0.04866], [0.38, 0.05179, 0.04576], [0.385, 0.05412, 0.04749],
    [0.39, 0.05459, 0.0427], [0.395, 0.05601, 0.04543], [0.4, 0.06094, 0.04831],
    [0.405, 0.06163, 0.04872], [0.41,0.06036, 0.04982], [0.415, 0.05841, 0.05042],
    [0.42, 0.05767, 0.04507], [0.425, 0.05777, 0.0499], [0.43, 0.05859, 0.04636],
    [0.435, 0.05319, 0.04624], [0.44, 0.04664, 0.03775], [0.445, 0.04938, 0.0417],
    [0.45, 0.05282, 0.04282], [0.455, 0.06554, 0.04861], [0.46, 0.07698, 0.05542],
    [0.465, 0.07487, 0.05643], [0.47, 0.07937, 0.05868], [0.475, 0.08434, 0.06137],
    [0.48, 0.0893, 0.06316], [0.485, 0.08061, 0.05759], [0.49, 0.08597, 0.05972],
    [0.495, 0.08978, 0.06234], [0.5, 0.09305, 0.06459], [0.505, 0.0899, 0.06269],
    [0.51, 0.08536, 0.05882], [0.515, 0.09501, 0.0638], [0.52, 0.09028, 0.0635],
    [0.525, 0.09617, 0.06446], [0.53, 0.09426, 0.06333], [0.535, 0.09628, 0.06492],
    [0.54, 0.0915, 0.06003], [0.545,0.09039, 0.06288], [0.55, 0.09334, 0.06218],
    [0.555, 0.09545, 0.06541], [0.56, 0.09648, 0.06307], [0.565, 0.09477, 0.06464],
    [0.57, 0.09567, 0.06252], [0.575, 0.09503, 0.06083], [0.58, 0.09278, 0.05822],
    [0.585, 0.09799, 0.06709], [0.59, 0.09718, 0.06387], [0.595, 0.09036, 0.05935],
    [0.6, 0.10621, 0.06754], [0.605, 0.10221, 0.06918], [0.61, 0.09191, 0.06501],
    [0.615, 0.09742, 0.06675], [0.62, 0.09407, 0.06639], [0.625, 0.09874, 0.06746],
    [0.63, 0.0996, 0.06713], [0.635, 0.09462, 0.05507], [0.64, 0.1018, 0.06398],
    [0.645, 0.10386, 0.065], [0.65, 0.11072, 0.06641], [0.655, 0.09719, 0.06469],
    [0.66, 0.09917, 0.06202], [0.665, 0.10534, 0.07327], [0.67, 0.10173, 0.07111],
    [0.675, 0.10383, 0.07128], [0.68, 0.1017, 0.06795], [0.685, 0.10114, 0.07072],
    [0.69, 0.10736, 0.06785], [0.695, 0.10759, 0.06738], [0.7, 0.10895, 0.06724],
    [0.71, 0.10756, 0.06942], [0.72, 0.10519, 0.06408], [0.73, 0.10942, 0.06743],
    [0.74, 0.116, 0.07055], [0.75, 0.10987, 0.06974], [0.76, 0.10883, 0.07065],
    [0.77, 0.11241, 0.06754], [0.78, 0.11049, 0.06863], [0.79, 0.1064, 0.06167],
    [0.8, 0.10586, 0.06731], [0.81, 0.10819, 0.06316], [0.82, 0.11088, 0.06998],
    [0.83, 0.11457, 0.06828], [0.84, 0.10336, 0.06607], [0.85, 0.10883, 0.06905],
    [0.86, 0.10474, 0.06756], [0.87, 0.10554, 0.06752], [0.88, 0.09773, 0.05754],
    [0.89, 0.10121, 0.06326], [0.9, 0.10198, 0.05817], [0.91, 0.10261, 0.06347],
    [0.92, 0.1025, 0.06583], [0.93, 0.09506, 0.05734], [0.94, 0.10133, 0.06517],
    [0.95, 0.09394, 0.05808], [0.96, 0.09464, 0.0558], [0.97, 0.10692, 0.06727],
    [0.98, 0.09688, 0.06097], [0.99, 0.09545, 0.06026], [1.0, 0.09984, 0.06145],
    [1.01, 0.09605, 0.0624], [1.02, 0.09926, 0.06632], [1.03, 0.09841, 0.06335],
    [1.04, 0.0967, 0.06327], [1.05, 0.09308, 0.06595], [1.06, 0.09365, 0.06227],
    [1.07, 0.10317, 0.06423], [1.08, 0.1002, 0.06245], [1.09, 0.1048, 0.06221],
    [1.1, 0.09808, 0.06609], [1.11, 0.10449, 0.0705], [1.12, 0.09851, 0.06357],
    [1.13, 0.09681, 0.06063], [1.14, 0.09604, 0.06353], [1.15, 0.10461, 0.06506],
    [1.16, 0.10008, 0.06297], [1.17, 0.10307, 0.06821], [1.18, 0.10318, 0.07077],
    [1.19, 0.10237, 0.06945]
])


Q2 = np.array([
    [0.0, 0.06674, 0.03713], [0.01, 0.06916, 0.04445], [0.02, 0.0655, 0.03656],
    [0.03, 0.06801, 0.03627], [0.04, 0.06115, 0.03578], [0.05, 0.07327, 0.04108],
    [0.06, 0.06881, 0.03707], [0.065, 0.06278, 0.03435], [0.07, 0.06857, 0.04012],
    [0.075, 0.06386, 0.03633], [0.08, 0.06504, 0.03534], [0.085, 0.06619, 0.03377],
    [0.09, 0.05631, 0.02811], [0.095, 0.05997, 0.03084], [0.1, 0.05995, 0.03371],
    [0.105, 0.07537, 0.03553], [0.11, 0.06238, 0.03859], [0.115, 0.05824, 0.0292],
    [0.12, 0.06084, 0.02957], [0.125, 0.05888, 0.02341], [0.13, 0.06181, 0.02722],
    [0.135, 0.06023, 0.0257], [0.14, 0.06474, 0.02543], [0.145, 0.06001, 0.02421],
    [0.15, 0.0656, 0.02677], [0.155, 0.05666, 0.02494], [0.16, 0.05905, 0.02718],
    [0.165, 0.06139, 0.02635], [0.17, 0.05729, 0.02292], [0.175, 0.06306, 0.02295],
    [0.18, 0.06005, 0.02581], [0.185, 0.05827, 0.02578], [0.19, 0.05882, 0.02539],
    [0.195, 0.06039, 0.02449], [0.2, 0.06471, 0.02442], [0.205, 0.06215, 0.02527],
    [0.21, 0.06102, 0.02334], [0.215, 0.06071, 0.02584], [0.22, 0.06384, 0.0269],
    [0.225, 0.06181, 0.02461], [0.23, 0.06237, 0.02709], [0.235, 0.06377, 0.02365],
    [0.24, 0.06345, 0.02656], [0.245, 0.06896, 0.03048], [0.25, 0.06333, 0.02848],
    [0.255, 0.06184, 0.02401], [0.26, 0.06586, 0.03111], [0.265, 0.06423, 0.02957],
    [0.27, 0.07119, 0.03014], [0.275, 0.06244, 0.02923], [0.28, 0.06326, 0.02982],
    [0.285, 0.06666, 0.0267], [0.29, 0.06639, 0.03246], [0.295, 0.06558, 0.03105],
    [0.3, 0.06391, 0.03065], [0.305, 0.06148, 0.02886], [0.31, 0.06281, 0.02947],
    [0.315, 0.06278, 0.03168], [0.32, 0.06295, 0.02757], [0.325, 0.0672, 0.03112],
    [0.33, 0.0665, 0.03012], [0.335, 0.06249, 0.02771], [0.34, 0.06277, 0.02845],
    [0.345, 0.06548, 0.03144], [0.35, 0.06387, 0.02968], [0.355, 0.06687, 0.03111],
    [0.36, 0.0645, 0.03086], [0.365, 0.0675, 0.03024], [0.37, 0.06442, 0.02728],
    [0.375, 0.06711, 0.02945], [0.38, 0.06617, 0.02379], [0.385, 0.06387, 0.02472],
    [0.39, 0.06474, 0.02711], [0.395, 0.06557, 0.02608], [0.4, 0.06705, 0.02742],
    [0.405, 0.06377, 0.02722], [0.41, 0.06317, 0.028], [0.415, 0.06414, 0.02543],
    [0.42, 0.06414, 0.02843], [0.425, 0.06582, 0.03037], [0.43, 0.06225, 0.02817],
    [0.435, 0.06552, 0.02893], [0.44, 0.06542, 0.03097], [0.445, 0.06501, 0.03079],
    [0.45, 0.06573, 0.03097], [0.455, 0.06648, 0.03259], [0.46, 0.06296, 0.03139],
    [0.465, 0.06156, 0.02884], [0.47, 0.06155, 0.02578], [0.475, 0.06102, 0.02874],
    [0.48, 0.06316, 0.03326], [0.485, 0.06562, 0.03166], [0.49, 0.06528, 0.0287],
    [0.495, 0.06378, 0.02888], [0.5, 0.05823, 0.02938], [0.505, 0.06659, 0.02997],
    [0.51, 0.06793, 0.03029], [0.515, 0.06601, 0.03373], [0.52, 0.06544, 0.03418],
    [0.525, 0.06877, 0.0287], [0.53, 0.06646, 0.03071], [0.535, 0.06836, 0.03045],
    [0.54, 0.06676, 0.03226], [0.545, 0.06512, 0.03394], [0.55, 0.06103, 0.03105],
    [0.555, 0.06498, 0.03184], [0.56, 0.06606, 0.02824], [0.565, 0.06776, 0.02925],
    [0.57, 0.06256, 0.02912], [0.575, 0.06415, 0.02823], [0.58, 0.06516, 0.02858],
    [0.585, 0.06517, 0.02893], [0.59, 0.06681, 0.03533], [0.595, 0.06624, 0.03122],
    [0.6, 0.06418, 0.03137], [0.605, 0.06589, 0.02959], [0.61, 0.06265, 0.02994],
    [0.615, 0.06458, 0.02737], [0.62, 0.06449, 0.02731], [0.625, 0.06536, 0.0267],
    [0.63, 0.06706, 0.0272], [0.635, 0.06786, 0.02919], [0.64, 0.06349, 0.03097],
    [0.645, 0.06357, 0.02812], [0.65, 0.06613, 0.03135], [0.655, 0.06491, 0.02904],
    [0.66, 0.06579, 0.02997], [0.665, 0.06317, 0.0296], [0.67, 0.06461, 0.02883],
    [0.675, 0.0642, 0.02813], [0.68, 0.06221, 0.02614], [0.685, 0.0614, 0.02925],
    [0.69, 0.06029, 0.02743], [0.695, 0.06119, 0.02452], [0.7, 0.06285, 0.02881],
    [0.71, 0.06264, 0.02692], [0.72, 0.06686, 0.02689], [0.73, 0.06479, 0.02586],
    [0.74, 0.06221, 0.02582], [0.75, 0.06477, 0.02878], [0.76, 0.0651, 0.02499],
    [0.77, 0.06077, 0.02491], [0.78, 0.06173, 0.02739], [0.79, 0.06212, 0.02307],
    [0.8, 0.06257, 0.02362], [0.81, 0.06564, 0.02671], [0.82, 0.06426, 0.02395],
    [0.83, 0.06232, 0.02467], [0.84, 0.06954, 0.02563], [0.85, 0.0633, 0.02481],
    [0.86, 0.06434, 0.02836], [0.87, 0.06394, 0.02715], [0.88, 0.06214, 0.02553],
    [0.89, 0.06267, 0.03012], [0.9, 0.06882, 0.02918], [0.91, 0.0668, 0.02704],
    [0.92, 0.06542, 0.02596], [0.93, 0.06365,0.02632], [0.94, 0.06436, 0.02403],
    [0.95, 0.0676, 0.02629], [0.96, 0.06918, 0.02521], [0.97, 0.06662, 0.0278],
    [0.98, 0.06576, 0.02359], [0.99, 0.06875, 0.02771], [1.0, 0.06644, 0.02628],
    [1.01, 0.0628, 0.02348], [1.02, 0.06485, 0.02695], [1.03, 0.06642, 0.02843],
    [1.04, 0.06583, 0.02708], [1.05, 0.06989, 0.0296], [1.06, 0.06423, 0.02503],
    [1.07, 0.06711, 0.03001], [1.08, 0.06714, 0.03258], [1.09, 0.06351, 0.02557],
    [1.1, 0.06364, 0.02595], [1.11, 0.06421, 0.02509], [1.12, 0.0625, 0.0287],
    [1.13, 0.06445, 0.02622], [1.14, 0.06622, 0.02658], [1.15, 0.06774, 0.0274],
    [1.16, 0.0672, 0.02413], [1.17, 0.0675, 0.02795], [1.18, 0.06273, 0.02653],
    [1.19, 0.06426, 0.02847]
])
Q2_More = np.array([
    [0.3, 0.0834, 0.03409], [0.302, 0.08035, 0.02272], [0.304, 0.07932, 0.02613],
    [0.306, 0.08611, 0.02617], [0.308, 0.07833, 0.02102], [0.31, 0.08597, 0.02318],
    [0.312, 0.08761, 0.02081], [0.314, 0.07423, 0.01781], [0.316, 0.07256, 0.02403],
    [0.318, 0.08189, 0.02474], [0.32, 0.0741, 0.01695], [0.322, 0.07715, 0.01817],
    [0.324, 0.08021, 0.02111], [0.326, 0.07723, 0.02256], [0.328, 0.08193, 0.02406],
    [0.33, 0.07861, 0.01447], [0.332, 0.07946, 0.02115], [0.334, 0.08402, 0.01976],
    [0.336, 0.08549, 0.01946], [0.338, 0.07796, 0.01139], [0.34, 0.08134, 0.019],
    [0.342, 0.07747, 0.02286], [0.344, 0.07316, 0.01441], [0.346, 0.08257, 0.01864],
    [0.348, 0.08069, 0.01807], [0.35, 0.07901, 0.01979], [0.352, 0.08346, 0.01782],
    [0.354, 0.07876, 0.01882], [0.356, 0.08608, 0.01274], [0.358, 0.07739, 0.01508],
    [0.36, 0.08242, 0.01979], [0.362, 0.07824, 0.01043], [0.364, 0.07719, 0.01938],
    [0.366, 0.08171, 0.01745], [0.368, 0.07782, 0.01099], [0.37, 0.07603, 0.01383],
    [0.372, 0.08159, 0.01482], [0.374, 0.07927, 0.01609], [0.376, 0.07722, 0.01384],
    [0.378, 0.07434, 0.01852], [0.38, 0.07149, 0.01258], [0.382, 0.07555, 0.01497],
    [0.384, 0.07218, 0.01124], [0.386, 0.07576, 0.01268], [0.388, 0.07104, 0.015],
    [0.39, 0.0736, 0.0173], [0.392, 0.07063, 0.01457], [0.394, 0.06762, 0.01347],
    [0.396, 0.07309, 0.01313], [0.398, 0.07266, 0.01003], [0.4, 0.07535, 0.01204],
    [0.402, 0.0715, 0.01321], [0.404, 0.07621, 0.01504], [0.406, 0.07616, 0.01408],
    [0.408, 0.07807, 0.01449], [0.41, 0.077, 0.01412], [0.412, 0.07204, 0.01639],
    [0.414, 0.07263, 0.01536], [0.416, 0.07362, 0.01788], [0.418, 0.0712, 0.01543],
    [0.42, 0.07211, 0.01416], [0.422, 0.07314, 0.01607], [0.424, 0.07405, 0.01349],
    [0.426, 0.07126, 0.01465], [0.428, 0.07031, 0.01286], [0.43, 0.07778, 0.01807],
    [0.432,0.07333, 0.01558], [0.434, 0.07221, 0.01142], [0.436, 0.07584, 0.01692],
    [0.438, 0.07539, 0.01182], [0.44, 0.07106, 0.01892], [0.442, 0.07709, 0.01682],
    [0.444, 0.08118, 0.01714], [0.446, 0.07227, 0.01638], [0.448, 0.07313, 0.01797],
    [0.45, 0.07622, 0.01585], [0.452, 0.07632, 0.0168], [0.454, 0.07654, 0.01554],
    [0.456, 0.07557, 0.02134], [0.458, 0.07327, 0.01577], [0.46, 0.06868, 0.01724],
    [0.462, 0.07374, 0.01914], [0.464, 0.08621, 0.02998], [0.466, 0.07836, 0.0172],
    [0.468, 0.07623, 0.02244], [0.47, 0.07477, 0.02219], [0.472, 0.07583, 0.02339],
    [0.474, 0.07839, 0.0201], [0.476, 0.06912, 0.01778], [0.478, 0.07322, 0.0152],
    [0.48, 0.08007, 0.0232], [0.482, 0.07717, 0.01804], [0.484, 0.085, 0.01778],
    [0.486, 0.07968, 0.02128], [0.488, 0.08461, 0.02071], [0.49, 0.0853, 0.00937],
    [0.492, 0.07628, 0.02119], [0.494, 0.07572, 0.02067], [0.496, 0.07635, 0.01991],
    [0.498, 0.0756, 0.02239]
])

Q4 = np.array([
    [0.0, 0.01893, 0.0122], [0.01, 0.01999, 0.01242], [0.02, 0.0176, 0.01021],
    [0.03, 0.01752, 0.01212], [0.04, 0.01769, 0.0138], [0.05, 0.0184, 0.01179],
    [0.06, 0.02062, 0.01201], [0.065, 0.01718, 0.01008], [0.07, 0.01958, 0.01104],
    [0.075, 0.01665, 0.01193], [0.08, 0.01737, 0.01111], [0.085, 0.01841, 0.01291],
    [0.09, 0.01831, 0.01148], [0.095, 0.01776, 0.01089], [0.1, 0.01966, 0.01566],
    [0.105, 0.01661, 0.01231], [0.11, 0.01595, 0.01122], [0.115, 0.01682,0.0107],
    [0.12, 0.0189, 0.0115], [0.125, 0.01691, 0.01162], [0.13, 0.02199, 0.01267],
    [0.135, 0.02043, 0.01035], [0.14, 0.02209, 0.01301], [0.145, 0.02045, 0.01355],
    [0.15, 0.02083, 0.01273], [0.155, 0.02034, 0.01274], [0.16, 0.02287, 0.01323],
    [0.165, 0.01937, 0.01359], [0.17, 0.02005, 0.01223], [0.175, 0.02303, 0.01218],
    [0.18, 0.02231, 0.01306], [0.185, 0.02538, 0.0153], [0.19, 0.02358, 0.01611],
    [0.195, 0.02857, 0.01332], [0.2, 0.03186, 0.0135], [0.205, 0.02391, 0.01226],
    [0.21, 0.03128, 0.0098], [0.215, 0.031, 0.01497], [0.22, 0.02913, 0.01217],
    [0.225, 0.03572, 0.01203], [0.23, 0.02876, 0.01158], [0.235, 0.03147, 0.01388],
    [0.24, 0.02888, 0.01182], [0.245, 0.0273, 0.01218], [0.25, 0.02491, 0.01366],
    [0.255, 0.02488, 0.01035], [0.26, 0.02481, 0.01149], [0.265, 0.02721, 0.01184],
    [0.27, 0.02492, 0.01307], [0.275, 0.02764, 0.01251], [0.28, 0.02522, 0.01147],
    [0.285, 0.02321, 0.0106], [0.29, 0.023, 0.01451], [0.295, 0.02418, 0.01183],
    [0.3, 0.02376, 0.01239], [0.305, 0.02353, 0.0114], [0.31, 0.02074, 0.01285],
    [0.315, 0.02288, 0.0125], [0.32, 0.02253, 0.00988], [0.325, 0.02219, 0.013],
    [0.33, 0.02259, 0.01265], [0.335, 0.02308, 0.01205], [0.34, 0.02286, 0.01162],
    [0.345, 0.02141, 0.01067], [0.35, 0.02414, 0.01312], [0.355, 0.0216, 0.01069],
    [0.36, 0.01755, 0.01214], [0.365, 0.02268, 0.01301], [0.37, 0.02131, 0.01082],
    [0.375, 0.01987, 0.01201], [0.38, 0.01976, 0.01066], [0.385, 0.02295, 0.01556],
    [0.39, 0.0194, 0.01221], [0.395, 0.02155, 0.01062], [0.4, 0.02064, 0.01221],
    [0.405, 0.02136, 0.01255], [0.41, 0.02163, 0.01382], [0.415, 0.022, 0.01147],
    [0.42, 0.0233, 0.01455], [0.425, 0.01903, 0.01338], [0.43, 0.01974, 0.0136],
    [0.435, 0.01897, 0.01045], [0.44, 0.02454, 0.0109], [0.445, 0.02271, 0.01353],
    [0.45, 0.01795, 0.01106], [0.455, 0.02189, 0.0124], [0.46, 0.02379, 0.0128],
    [0.465, 0.02383, 0.0114], [0.47, 0.02251, 0.01292], [0.475, 0.01984, 0.01028],
    [0.48, 0.02408, 0.0142], [0.485, 0.01988, 0.01016], [0.49, 0.02081, 0.01203],
    [0.495, 0.0231, 0.01211], [0.5, 0.02293, 0.01135], [0.505, 0.02267, 0.01469],
    [0.51, 0.0216, 0.01194], [0.515, 0.0249, 0.01123], [0.52, 0.02249, 0.01225],
    [0.525, 0.02075, 0.01065], [0.53, 0.02126, 0.0107], [0.535, 0.02121, 0.01171],
    [0.54, 0.02301, 0.01164], [0.545, 0.02169, 0.0101], [0.55, 0.02177, 0.01185],
    [0.555, 0.02196, 0.00992], [0.56, 0.02504, 0.01392], [0.565, 0.02519, 0.01114],
    [0.57, 0.02418, 0.01285], [0.575, 0.02398, 0.01308], [0.58, 0.02717, 0.01677],
    [0.585, 0.02421, 0.01036], [0.59, 0.02441, 0.01219], [0.595, 0.02222, 0.01236],
    [0.6, 0.02378, 0.01327], [0.605, 0.02433, 0.01149], [0.61, 0.02443, 0.01165],
    [0.615, 0.02794, 0.01329], [0.62, 0.02643, 0.01198], [0.625, 0.0258, 0.01036],
    [0.63, 0.02778, 0.01039], [0.635, 0.03015, 0.01256], [0.64, 0.03332, 0.01319],
    [0.645, 0.02879, 0.01079], [0.65, 0.03347, 0.01686], [0.655, 0.03421, 0.01268],
    [0.66, 0.03379, 0.01132], [0.665, 0.03464, 0.00987], [0.67, 0.03527, 0.01283],
    [0.675, 0.03934, 0.01349], [0.68, 0.03919, 0.01344], [0.685, 0.03919, 0.01157],
    [0.69, 0.03929, 0.01334], [0.695, 0.04264, 0.01113], [0.7, 0.04246, 0.01191],
    [0.71, 0.03947, 0.01262], [0.72, 0.04721, 0.01395], [0.73, 0.04556, 0.01235],
    [0.74, 0.05283, 0.01183], [0.75, 0.05238, 0.01615], [0.76, 0.05514, 0.01594],
    [0.77, 0.05594, 0.01155], [0.78, 0.05822, 0.01226], [0.79, 0.06343, 0.0115],
    [0.8, 0.06554, 0.01331], [0.81, 0.06551, 0.01216], [0.82, 0.06667, 0.01345],
    [0.83, 0.06873, 0.01479], [0.84, 0.07254, 0.01373], [0.85, 0.07548, 0.01516],
    [0.86, 0.07656, 0.01512], [0.87, 0.0768, 0.01269], [0.88, 0.0746, 0.01359],
    [0.89, 0.07639, 0.01239], [0.9, 0.07452, 0.01378], [0.91, 0.07535, 0.01444],
    [0.92, 0.07736, 0.01487], [0.93, 0.07721, 0.01288], [0.94, 0.07809, 0.01185],
    [0.95, 0.0771, 0.01306], [0.96, 0.07519, 0.01724], [0.97, 0.07536, 0.01524],
    [0.98, 0.07386, 0.01375], [0.99, 0.07455, 0.01511], [1.0, 0.07554, 0.01363],
    [1.01, 0.07384, 0.01249], [1.02, 0.07576, 0.0142], [1.03, 0.07491, 0.01281],
    [1.04, 0.07531, 0.01212], [1.05, 0.0756, 0.01427], [1.06, 0.07757, 0.01372],
    [1.07, 0.07425, 0.01245], [1.08, 0.07501, 0.01196], [1.09, 0.0748, 0.01478],
    [1.1, 0.07255, 0.01114], [1.11, 0.07292, 0.01141], [1.12, 0.07602, 0.01352],
    [1.13, 0.075, 0.01444], [1.14, 0.07739, 0.01426], [1.15, 0.07461, 0.01271],
    [1.16, 0.07613, 0.01124], [1.17, 0.0759, 0.01242], [1.18, 0.0738, 0.0132],
    [1.19, 0.07361, 0.01296]
])
### J6 Bias Conversion
Q1[:, 0] = (Q1[:, 0])*1000
Q2[:, 0] = (Q2[:, 0])*1000
Q2_More[:, 0] = (Q2_More[:, 0])*1000
Q4[:, 0] = (Q4[:, 0])*1000


# f = 4.604
f = 0.968
# f = 1
Al_gap = 380e-6
DAC_Al = 1e5*Al_gap/0.200
plt.errorbar(Q1[:, 0]*f, Q1[:, 1], yerr=Q1[:, 2]/np.sqrt(50), color='b', label='Q1')
plt.errorbar(Q2[:, 0]*f, Q2[:, 1], yerr=Q2[:, 2]/np.sqrt(50), color='r', label='Q2')
# plt.errorbar(Q2_More[:, 0]*f, Q2_More[:, 1], yerr=Q2_More[:, 2]/np.sqrt(50), color='k', label='Q2_More')
plt.errorbar(Q4[:, 0]*f, Q4[:, 1], yerr=Q4[:, 2]/np.sqrt(50), color='y', label='Q4')

plt.axvline(x=DAC_Al * f, color='k', linestyle='--', linewidth=4, label='JJ Al Gap')

plt.xlabel('J6 Weak Radiator Josephson Frequency (GHz)')
plt.ylabel('P1')
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which="both")
plt.legend(loc=2)
# plt.xlim([0, 1500])
# plt.ylim([10, 100000])
plt.show()


