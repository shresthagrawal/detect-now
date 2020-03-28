import csv
import pandas as pd
import numpy as np

data = np.array(pd.read_csv('data/region_data.csv'))
ln = len(data[0])
popul = np.array(pd.read_csv('data/population.csv'))
length = len(popul[0])

a = {} #num of infected
for x in data:
    a[x[1]] = 0
for x in data:
    a[x[1]] += x[ln-1]

b = {} #population
for x in popul:
    b[x[0]] = x[length-3]

def detect(country): # in %
    return (100*a[country]/b[country])
