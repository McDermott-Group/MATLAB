import matplotlib.pyplot as plt

bias22=[-298, -278, -258, -238, -218, -198, -178, -158, -138, -118, -98, -88, -78, -68, -58, -48, -38, -28, -18, -8, 2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 142, 152, 162, 172, 182, 192, 202, 212, 222, 232, 242, 252, 272, 292, 312, 332, 352, 372, 392, 412, 432, 452, 472, 492, 512, 532, 552, 572, 592, 612, 632, 652, 672, 692]
freq22=[-713.7280000000001, -683.008, -652.288, -621.568, -590.848, -560.128, -529.408, -498.68800000000005, -467.9680000000001, -437.248, -406.528, -391.168, -375.808, -360.44800000000004, -345.088, -329.728, -314.36800000000005, -299.008, -283.648, -268.288, -252.92800000000003, -237.56799999999998, -222.208, -206.848, -191.48800000000003, -176.12800000000001, -160.76800000000003, -145.40800000000002, -130.048, -114.68800000000002, -99.32800000000003, -83.96799999999999, -68.60799999999999, -53.248000000000005, -37.88800000000001, -22.527999999999977, -7.167999999999984, 8.192000000000007, 23.552, 38.91199999999999, 54.271999999999984, 69.63199999999998, 84.99199999999996, 100.35199999999996, 115.71199999999999, 131.07199999999997, 161.79200000000003, 192.512, 223.23199999999997, 253.95199999999997, 284.67199999999997, 315.39200000000005, 346.112, 376.832, 407.55199999999996, 438.27199999999993, 468.992, 499.712, 530.432, 561.1519999999999, 591.872, 622.5920000000001, 653.3119999999999, 684.032, 714.7520000000001, 745.472, 776.192, 806.9119999999999]
p122=[0.6903900163269342, 0.6981817623538229, 0.7034140724971097, 0.7070009422776125, 0.7037255949938519, 0.7069849809200951, 0.7076965521826278, 0.7025079339857737, 0.71303000633767, 0.7137049840335944, 0.7212537338513971, 0.6902860008843024, 0.7174738893425132, 0.7005450487772225, 0.7010548783258691, 0.6918710339021603, 0.7232682679123611, 0.68221094869804, 0.7063554348427533, 0.6972788486685808, 0.7127604651571932, 0.7181809012459375, 0.7323712975367501, 0.6932585578036331, 0.7373669486843845, 0.7114605338713659, 0.7308549875057059, 0.7059086473053333, 0.7336636835354639, 0.7066085764029901, 0.68932823250822, 0.7102439965453231, 0.7298117390266463, 0.7428395996262694, 0.7205500354728692, 0.7333912081837631, 0.7235212091499034, 0.7226246221713037, 0.7110585817697629, 0.7164466895226812, 0.7119500393169709, 0.6738377327082473, 0.6950569288473784, 0.7130492063399995, 0.7247172977037987, 0.7280713055378264, 0.7343915774016765, 0.7271466909501569, 0.6998806910748772, 0.7216335326010711, 0.7022725220631538, 0.707055935734898, 0.7089877268151377, 0.7139926331599501, 0.7098539682100724, 0.7096284773189332, 0.7138266061179325, 0.7008959216857231, 0.7070664690734413, 0.709279956416249, 0.7117407365369576, 0.7097324947739477, 0.7076928244653831, 0.703827540099496, 0.7052094819991247, 0.7107496146107491, 0.6902247429688629, 0.685224246029751]

bias23=[-308, -298, -288, -278, -268, -258, -248, -238, -228, -218, -208, -198, -188, -178, -168, -158, -148, -138, -128, -118, -108, -98, -88, -78, -68, -58, -48, -38, -28, -18, -8, 2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 142, 152, 162, 172, 182, 192, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 302, 312, 322, 342, 352, 362, 372, 382, 392, 402, 412, 422, 432, 442, 452, 462, 472, 482, 492, 502, 512, 532, 552, 572, 592, 612, 632, 652, 672, 692]
freq23=[-729.088, -713.7280000000001, -698.3679999999999, -683.008, -667.648, -652.288, -636.928, -621.568, -606.208, -590.848, -575.488, -560.128, -544.768, -529.408, -514.048, -498.68800000000005, -483.328, -467.9680000000001, -452.608, -437.248, -421.88800000000003, -406.528, -391.168, -375.808, -360.44800000000004, -345.088, -329.728, -314.36800000000005, -299.008, -283.648, -268.288, -252.92800000000003, -237.56799999999998, -222.208, -206.848, -191.48800000000003, -176.12800000000001, -160.76800000000003, -145.40800000000002, -130.048, -114.68800000000002, -99.32800000000003, -83.96799999999999, -68.60799999999999, -53.248000000000005, -37.88800000000001, -22.527999999999977, -7.167999999999984, 8.192000000000007, 23.552, 38.91199999999999, 54.271999999999984, 69.63199999999998, 84.99199999999996, 100.35199999999996, 115.71199999999999, 131.07199999999997, 146.432, 161.79200000000003, 177.15199999999996, 192.512, 207.87199999999996, 223.23199999999997, 238.592, 269.312, 284.67199999999997, 300.032, 315.39200000000005, 330.75199999999995, 346.112, 361.472, 376.832, 392.192, 407.55199999999996, 422.91200000000003, 438.27199999999993, 453.632, 468.992, 484.352, 499.712, 515.072, 530.432, 561.1519999999999, 591.872, 622.5920000000001, 653.3119999999999, 684.032, 714.7520000000001, 745.472, 776.192, 806.9119999999999]
p123=[0.6270459111424934, 0.5426055421551735, 0.6025649542429258, 0.5813095562464916, 0.6001097216472276, 0.5677261817898581, 0.5895801744970227, 0.5798032476379879, 0.6127692869684723, 0.5910778057403977, 0.592386202344596, 0.5873047402743544, 0.6085978722878133, 0.5596565584570221, 0.6030448694809074, 0.5661491446916739, 0.6162286666155762, 0.6116633544934406, 0.6085060266312254, 0.6049097792185795, 0.6042712274901432, 0.5920605880592756, 0.6072483029941984, 0.591425604505414, 0.6212089538165189, 0.5502491865574, 0.6272181315915515, 0.553003670453277, 0.613274409514241, 0.6005853923908793, 0.5912204827689983, 0.5747092590509265, 0.5630568364793322, 0.5955723852579886, 0.5773831445732077, 0.6044996799458603, 0.5885171934205278, 0.5874500367314324, 0.6066576144815575, 0.5588966797114597, 0.5866667208253914, 0.5678590305674691, 0.6006044459830143, 0.5706583668891597, 0.6133365013227833, 0.5857503571862785, 0.587567415202134, 0.6126505283807581, 0.5672541870090411, 0.5925588278208285, 0.5679185539849565, 0.591359967330067, 0.5578862638867351, 0.5576076614557395, 0.6031100024114212, 0.6007264604422836, 0.6192756632154119, 0.6171456622265743, 0.601865964584367, 0.5965591062008726, 0.6162251448651939, 0.5699748510217642, 0.6255161081952135, 0.5876854246138254, 0.6234592841515618, 0.6121927693408865, 0.6008353503394851, 0.5978706614621974, 0.6014402993521478, 0.5843021988724172, 0.592973509964722, 0.6016472232524986, 0.5829219067505563, 0.6103396147250154, 0.5854654116453434, 0.6230601050809433, 0.5257993231743426, 0.6240079860186227, 0.5766446274805185, 0.5940220294221336, 0.5836734352147247, 0.6080443622737257, 0.5704203587883154, 0.5724752607389323, 0.5787666034413643, 0.5615488099303838, 0.5784031364548713, 0.5877159994743941, 0.577665528294711, 0.5684080643569707, 0.5704931047738344]


plt.plot(freq22, p122,'o-',markersize=3, label='Q3 5us', color='b')
plt.plot(freq23, [p+0.11 for p in p123],'o-',markersize=3, label='Q3 10us', color='r')
plt.xlabel('J3 Frequency (GHz)')
plt.ylabel('P1')
plt.grid()
plt.legend()
plt.draw()
plt.show()