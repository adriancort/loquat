import matplotlib.pyplot as plt
from pandas_datareader import data, wb
from datetime import datetime
import pandas as pd
import numpy as np
import datetime
import statistics as st
from datetime import date


# Selects number of singificant digits
def signif(x, p):
    x = np.asarray(x)
    x_positive = np.where(np.isfinite(x) & (x != 0), np.abs(x), 10**(p - 1))
    mags = 10 ** (p - 1 - np.floor(np.log10(x_positive)))
    return np.round(x * mags) / mags


# Evaluates "given yesterday's fall, whats the expected probability of a rise?"
def oneDayDelay(stock, minTranche=-0.2, maxTranche=0.2, numTranche=10):
    q = np.linspace(minTranche, maxTranche, numTranche)
    q = signif(q, 3)
    prb_dict = {}
    for i in range(len(q)):
        empty_List = {q[i]: ([])}
        prb_dict.update(empty_List)
    for i in range(1, len(stock) - 2):
        ii = 0
        tranchefound = False
        while tranchefound == False and ii - 1 < len(q):  # check = or ==
            if q[ii] < stock[i] and q[ii + 1] >= stock[i]:
                tranchefound = True
                prb_dict[q[ii]].append(stock[i + 1])
            ii += 1
    rev_list = list(reversed(range(len(prb_dict.keys()))))
    for i in rev_list:  # eliminates keys with less than 1 datapoints
        if len(prb_dict[q[i]]) <= 1:
            del prb_dict[q[i]]  # eleminates key
            q = np.delete(q, i, 0)  # eliminates array element

    return prb_dict, q


def oneDayDelay_plt(stock_dict, q):
    index = []
    mean_return = []
    for i in q:
        index.append(i)
        mean_return.append(st.mean(stock_dict[i]))
    df3 = pd.DataFrame({'Mean Return': mean_return}, index=index)
    df3.plot.bar(rot=0, grid=True).legend(
        loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.show()


def pos(lst):
    return [x for x in lst if x >= 0] or None


def neg(lst):
    return [x for x in lst if x < 0] or None
