import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\PG_DBDA\Advanced Analytics\Dec_07")


housing = pd.read_csv("Housing.csv")

#boxplot
plt.subplot(2,2,1)
sns.boxplot(data=housing['price'])
#plt.show()


#histogram
plt.subplot(2,2,2)
sns.histplot(data=housing, x="price", bins =6)
#plt.show()


#scatter plot
plt.subplot(2,2,3)
sns.scatterplot(data=housing, x="lotsize", y="price", hue="bedrooms")
#plt.show()


#bar plot using count
plt.subplot(2,2,4)
cts=housing['bathrms'].value_counts()
cts.plot(kind='bar')
plt.tight_layout()
plt.show()
