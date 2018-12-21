#!/usr/bin/python

import numpy
from statistics import mean
import pandas as pd

data=pd.open_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data")

x=np.array([1,2,3,4,5])
y=np.array([5,6,7,8,9])

#calculate slope that is m

#m=(mean(x)* mean(y) - mean(x*y))/ (mean(x))^2 - mean(x^2))

def slope(x,y):
	m=(((mean(x)* mean(y)) - mean(x*y))/ ((mean(x) * (mean(x)) - mean(x*x)))
	return (m)

#intercept

def inter():
	intc=(mean(y) - slope(m)* mean(x))
	return intc
