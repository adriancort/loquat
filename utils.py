import matplotlib.pyplot as plt
from pandas_datareader import data, wb
from datetime import datetime
import pandas as pd
import numpy as np
import datetime
from datetime import date


def oneDayDelay(stock, minTranche=-0.2, maxTranche=0.2, numTranche=20):
    q = np.linspace(minTranche, maxTranche, numTranche)
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
    return prb_dict
