import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\PG_DBDA\Advanced Analytics\Dec_07")


cars93 = pd.read_csv("Cars93.csv")
print(cars93.shape)
print(cars93.columns)
print(cars93.dtypes)
print(cars93.info())


print(cars93['Price'].mean())
print(cars93['Price'].median())
print(cars93['Price'].quantile())
print(cars93['Price'].quantile(q=0.25))
print(cars93['Price'].quantile(q=0.75))

print(cars93['Price'].quantile(q=np.array([0.25,0.5,0.75])))

cars93['Price'].plot(kind='box')
plt.show()

#variance
cars93['Price'].var()

#coefficient of variation
cv=cars93['Price'].std()/cars93['Price'].mean()
cv

#skewness
from scipy.stats import skew
skew(cars93['Price'])
cars93['Price'].skew()

#kurtosis
from scipy.stats import kurtosis
kurtosis(cars93['Price'], fisher=True)
cars93['Price'].kurtosis()

cts=cars93['Type'].value_counts()
cts.plot(kind='bar')
plt.show()

#matplotlib
plt.bar(cts.index,cts)
plt.show()


#Seaborn
cts1= cts.reset_index()
cts1.columns = ['Type', 'Count']
sns.barplot(data= cts1, x='Type', y= 'Count')
plt.show()

#Histogram
cars93['Price'].plot(kind= 'hist', bins = 15 )
plt.show()

#Matplotlib
plt.hist(cars93['Price'],bins = 15 )
plt.show()

#seaborn
sns.histplot(data= cars93, x='Price', bins = 15 )
plt.show()












