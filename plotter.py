import matplotlib.pyplot as plt

# just copied the results and pasted them here because im lazy
list1 = [9892, 24460, 19299, 8529, 18099, 18478, 1531, 21616, 3816, 28506, 20733, 42267, 90661, 34585, 129845, 10148, 3435, 48188, 13509, 2051, 63576, 72987, 6216, 32545, 28308, 6066, 43807, 6231, 8702, 5708, 32468, 40508, 32919, 1078, 38286, 28596, 60391, 6522, 78915, 31153, 53835, 11058, 145726, 10417, 74512, 11775, 61240, 17952, 51237, 35455, 38735, 64884, 55244, 82307, 93266, 13866, 56052, 39170, 14918, 49350, 40063, 14486, 2480, 2433, 39536, 69175, 5928, 58652, 2602, 13060, 23149, 14972, 5222, 45663, 16641, 9448, 49576, 25876, 27543, 33937, 10599, 37640, 90536, 20242, 68570, 15081, 57472, 33760, 58781, 37711, 23597, 15134, 102395, 30182, 100144, 66713, 7499, 86630, 26325, 26616]
list2 = [8219, 9314, 9115, 1931, 10641, 4861, 1538, 5190, 1089, 2313, 735, 11781, 800, 4605, 665, 7945, 431, 2908, 785, 882, 3399, 3129, 4980, 3050, 1164, 4459, 4861, 1599, 1900, 1605, 833, 1643, 728, 981, 565, 1542, 678, 670, 7024, 6508, 2818, 5468, 1252, 4932, 4272, 1457, 6696, 1243, 9841, 1686, 2059, 2146, 1608, 3894, 6027, 3031, 1451, 1784, 849, 3484, 1058, 1144, 719, 1038, 5121, 1374, 2094, 8214, 2892, 4934, 2958, 975, 2435, 1336, 2009, 2025, 726, 3073, 5205, 2500, 2498, 4324, 1729, 1351, 1553, 1122, 556, 2308, 2092, 1077, 1260, 2983, 3912, 1289, 1270, 940, 7835, 1154, 2336, 2879]
list3 = [18131, 120696, 68983, 50168, 33360, 53212, 32459, 96447, 125241, 60940, 245983, 186805, 68596, 55875, 19520, 86335, 41358, 118659, 82381, 215730, 240816, 7993, 45359, 76621, 162105, 31406, 95415, 11668, 9637, 107026, 102969, 30124, 104944, 8581, 32715, 20510, 122590, 194121, 15327, 40834, 21390, 106796, 35632, 20246, 8658, 143903, 40509, 142706, 149619, 17512, 225858, 14459, 230113, 212292, 22745, 114781, 190770, 41628, 58168, 69747, 40332, 40715, 84507, 19924, 52737, 12745, 88230, 16289, 5982, 138565, 15692, 24068, 82282, 46144, 30206, 22582, 28319, 15269, 190563, 15485, 16019, 348619, 30153, 118461, 102848, 87233, 75991, 8611, 42218, 150736, 47135, 75443, 132295, 10794, 85821, 242820, 9111, 23128, 36126, 40199]
list4 = [59337, 76226, 114117, 110438, 120023, 45199, 11838, 244236, 159470, 13714, 82073, 10606, 91389, 41165, 55826, 53486, 165483, 102284, 48328, 56162, 10047, 86169, 231163, 54542, 97771, 258305, 77616, 37094, 55151, 39709, 61642, 32886, 70451, 58860, 236307, 21267, 131983, 18750, 82573, 29812, 52525, 54317, 144295, 37366, 18575, 115615, 67201, 33949, 56540, 107572, 46398, 84578, 212391, 69329, 31853, 33981, 72685, 21672, 45309, 44790, 17856, 67149, 49645, 58417, 40447, 51192, 83513, 83071, 26965, 247256, 85403, 35023, 6724, 38555, 16453, 37151, 83547, 53062, 142320, 53466, 38253, 79567, 172819, 18420, 193667, 206823, 59023, 19768, 114817, 75104, 74140, 165528, 30829, 60772, 37065, 109198, 80623, 43311, 7963, 125806]
list5 = [89244, 118482, 222138, 35486, 66589, 161303, 308843, 119151, 621263, 210695, 718313, 134065, 16024, 149632, 122484, 298772, 42719, 91183, 31544, 462529, 153900, 294665, 187627, 64111, 139696, 448692, 179715, 342750, 146501, 228714, 227947, 256351, 152089, 40603, 241270, 56722, 50085, 94136, 30865, 212783, 186018, 342961, 88083, 92186, 167847, 55623, 45804, 217024, 136591, 360566, 223712, 22232, 19185, 148470, 161769, 23133, 120828, 6053, 137552, 189204, 352486, 93926, 207745, 99181, 110212, 192515, 99710, 27044, 301530, 110437, 316151, 95766, 167092, 342613, 697347, 66293, 32125, 154347, 214087, 30137, 71500, 583704, 621228, 229700, 199531, 117393, 226146, 218426, 57943, 66706, 89335, 25857, 49717, 39318, 37128, 47477, 448957, 21534, 105836, 457138]
list6 = [13670, 95572, 36703, 4908, 112629, 23111, 35359, 62531, 161222, 63415, 20416, 12809, 20398, 12346, 5005, 21006, 63185, 57779, 43292, 69259, 24009, 8258, 97456, 106775, 25257, 5896, 27247, 37581, 10150, 6615, 15096, 15373, 45551, 31400, 86026, 55715, 42732, 56584, 7300, 67355, 6672, 96550, 49733, 18959, 72450, 40309, 16180, 33008, 36085, 33483, 55104, 17980, 13037, 53804, 17186, 64494, 33554, 66776, 114530, 31747, 55435, 26645, 45825, 20529, 35623, 74384, 49196, 29689, 17411, 66341, 21618, 82788, 44146, 80035, 25295, 103767, 18252, 14844, 44557, 46959, 25864, 52887, 24703, 29520, 66547, 10006, 927, 44316, 94665, 26887, 71486, 8776, 25582, 174985, 41510, 59291, 37998, 12505, 93496, 73818]
list7 = [41966, 89230, 148057, 161520, 91318, 240522, 325175, 152047, 238641, 157203, 221364, 135935, 302533, 136598, 279297, 191490, 135039, 154730, 304280, 451799, 229515, 178824, 449274, 33667, 147597, 121273, 595498, 376720, 290903, 302051, 505351, 382046, 139900, 47019, 227655, 235003, 26651, 299752, 59046, 68245, 331604, 625800, 355677, 265773, 123771, 169850, 234984, 743373, 118984, 46178, 67078, 298806, 169778, 659486, 457402, 205217, 35616, 411670, 409690, 22912, 568241, 263924, 56347, 771226, 457240, 342038, 110246, 323523, 205488, 33825, 71233, 121580, 64741, 356616, 625999, 20151, 79636, 270996, 357628, 34267, 179304, 155851, 144704, 136417, 37515, 370252, 270459, 307637, 81491, 247192, 229911, 479638, 144173, 383296, 246943, 279724, 50615, 77086, 64308, 535934]

def plot_average_minimum(data_list):
    lowest = 999999999
    sum = 0
    for item in data_list:
        if item < lowest:
            lowest = item

    for item in data_list:
        sum += item
    average = sum/len(data_list)

    plt.plot(data_list, 'ro', label="all games")
    plt.hlines(average, xmin=0, xmax=len(data_list), label="average")
    plt.hlines(lowest, xmin=0, xmax=len(data_list), label="lowest")

    print(f"This list wins the game after an average of {average} turns, with {lowest} turns as the fastest game.")

    plt.xlabel("experiment number")
    plt.ylabel("turns until victory")
    plt.legend()
    plt.savefig("plotty.png")
    # plt.show()

plot_average_minimum(list1)

# 35716.98
# 2993.62
# 77635.69

# 76951.5
# 177398.4
# 44577.4

# 239857.78

