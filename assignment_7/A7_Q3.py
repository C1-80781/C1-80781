#
# 3)Write a Pandas program to convert a dictionary to a Pandas series.
# Sample dictionary: d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}

import pandas as pd

def converter(d1):
    s1 = pd.Series(d1)
    print(s1)

d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
converter(d1)
