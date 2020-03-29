import csv
import pandas as pd
import numpy as np

data = np.array(pd.read_csv('data/region_data.csv'))
ln = len(data[0])
popul = np.array(pd.read_csv('data/population.csv'))
length = len(popul[0])

gend = {}
gend['male'] = 107/101
gend['female'] = 93/99

a = {} #num of infected
for x in data:
    a[x[1]] = 0
for x in data:
    a[x[1]] += x[ln-1]

b = {} #population
for x in popul:
    b[x[1]] = x[length - 3]

flu_rate = {} #source: https://academic.oup.com/cid/article/66/10/1511/4682599
for x in range(0,18):
    flu_rate[x] = 0.093
for x in range(18,65):
    flu_rate[x] = 0.088
for x in range(65,120):
    flu_rate[x] = 0.039

def detect(country, gender, age):
    p = gend[gender]
    # p = gend[gender] / flu_rate[age]
    if country in a.keys() and country in b.keys():
        p *= a[country] / b[country]
    else:
        p *= 718187/7775000000
    return p
    