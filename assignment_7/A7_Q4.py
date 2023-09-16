# 4)Write a Pandas program to change the order of index of a given series. Go to
# the editor
# Sample Output:
# Original Data Series:
# A1
# B2
# C3
# D4
# E5
# dtype: int64
# Data Series after changing the order of index:
# B2
# A1
# C3
# D4
# E5
# dtype: int64

import pandas as pd


def function(s1):
    l1 = list(s1)
    a = l1[0]
    l1[0] = l1[1]
    l1[1] = a
    print(l1)


s1 = pd.Series(['A1', 'B2', 'C3', 'D4', 'E5'])

function(s1)
