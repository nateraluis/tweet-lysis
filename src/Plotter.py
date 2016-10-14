from collections import Counter
import numpy as np
import matplotlib.pyplot as plt


# def plotRelatedHT(HTList):
#     counter = Counter(HTList)
#     hts, counts = zip(*Counter(HTList).items())
#
#     indexes = np.arange(len(hts))
#     width = 0.7
#     plt.bar(indexes, counts, width)
#     plt.xticks(indexes + width * 0.5, hts)
#     plt.show()


def plotRelatedHT(HTList):
    hts, counts = zip(*HTList)

    indexes = np.arange(len(hts))
    width = 0.7
    plt.bar(indexes, counts, width)
    plt.xticks(indexes + width * 0.5, hts)
    plt.show()
