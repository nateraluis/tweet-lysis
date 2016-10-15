from collections import Counter
import numpy as np
import matplotlib.pyplot as plt



def plotTupleCount(HTList):
    index, counts = zip(*HTList)

    indexes = np.arange(len(index))
    width = 0.7
    plt.bar(indexes, counts, width)
    plt.xticks(indexes + width * 0.5, index)
    plt.show()
