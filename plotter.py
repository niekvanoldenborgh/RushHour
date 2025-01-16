import matplotlib.pyplot as plt

# just copied the results and pasted them here
list1 = [18959, 2908, 53742, 10794, 18257, 3458, 60696, 33632, 4472, 15250, 1002, 9960, 45663, 88120, 36126, 99964, 37825, 72885, 5181, 5853]
list2 = [17144, 736, 1805, 1250, 1117, 858, 1669, 396, 3200, 1915, 1490, 5893, 1129, 3352, 2165, 1355, 3436, 12548, 4523, 10334]
list3 = [2017, 2956, 2331, 3039, 986, 2069, 3454, 2460, 3271, 1686, 24234, 19250, 183271, 14500, 10278, 13792, 175822, 32532, 42598, 79321]

plt.plot(list1, 'ro', label="6x6_1")
plt.plot(list2, 'bo', label="6x6_2")
plt.plot(list3, 'go', label="6x6_3")

plt.xlabel("experiment number")
plt.ylabel("turns until victory")
plt.legend()
plt.savefig("plotty.png")
plt.show()