import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\PG_DBDA\Advanced Analytics\Dec_07")


housing = pd.read_csv("Housing.csv")

#skewness
from scipy.stats import skew
skew(housing['price'])
housing['price'].skew()

#kurtosis
from scipy.stats import kurtosis
kurtosis(housing['price'], fisher=True)
housing['price'].kurtosis()

#histogram
housing['price'].plot(kind='hist', bins=7)
plt.show()

#seaborn
sns.histplot(data= housing, x='price', bins = 9 )
plt.show()
