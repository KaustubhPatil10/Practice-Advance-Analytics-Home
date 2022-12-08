import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\PG_DBDA\Advanced Analytics\Dec_07")


cars93 = pd.read_csv("Cars93.csv")

# Box Plot
cars93['Price'].plot(kind='box')
plt.title("Box Plot")
plt.show()

#Matplotlib
plt.boxplot(cars93["Price"])
plt.title("Box Plot")
plt.show()

#Seaborn
sns.boxplot(data=cars93, y="Price")
plt.show()

sns.boxplot(data=cars93,x = "AirBags", y= "Price")
plt.show()

#Facet Grid
g = sns.FacetGrid(cars93,row="AirBags")
g=g.map(plt.scatter,"EngineSize", "MPG.highway",color="violet")
plt.show()

g = sns.FacetGrid(cars93,col="AirBags")
g=g.map(plt.scatter,"EngineSize", "MPG.highway",color="Red")
plt.show()

#Sub Plot
plt.subplot(1,2,1)             #1,2 ka 1st plot
sns.boxplot(y='Price', data= cars93)
plt.title("Box Plot")

plt.subplot(1,2,2)             #1,2 ka 2nd plot
sns.histplot(data=cars93, x='Price', bins=8)
plt.title("Histogram")

plt.tight_layout()
plt.show()