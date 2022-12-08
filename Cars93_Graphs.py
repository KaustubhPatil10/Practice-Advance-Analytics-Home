import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\PG_DBDA\Advanced Analytics\Dec_07")


cars93 = pd.read_csv("Cars93.csv")


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

#Density plot / Distribution plot
cars93['Price'].plot(kind='kde')
plt.show()

#seaborn
sns.kdeplot(data = cars93, x= 'Price')
plt.show()

#scatter plot
cars93.plot(kind= 'scatter', x= 'EngineSize', y= 'MPG.highway')
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("MPG.highway")
plt.show()

#Matplotlib
plt.scatter(cars93['EngineSize'],cars93['MPG.highway'])
plt.title("Scatter Plot")
plt.xlabel("EngineSize")
plt.ylabel("MPG.highway")
plt.show()

#seaborn
sns.scatterplot(data= cars93,x= "EngineSize", y="MPG.highway")
plt.title("Scatter Plot")
plt.xlabel("EngineSize")
plt.ylabel("MPG.highway")
plt.show()

#Matplotlib
no_bags= cars93[cars93["AirBags"] == "None"]
plt.scatter(no_bags['EngineSize'],no_bags['MPG.highway'])
plt.title("Scatter Plot")
plt.xlabel("EngineSize")
plt.ylabel("MPG.highway")
plt.show()



#Matplotlip
no_bags= cars93[cars93["AirBags"] == "None"]
plt.scatter(no_bags['EngineSize'],no_bags['MPG.highway'],
             label="No AirBags")
driver= cars93[cars93["AirBags"] == "Driver only"]
plt.scatter(driver['EngineSize'],driver['MPG.highway'],
            label="Driver only")
d_p= cars93[cars93["AirBags"] == "Driver & Passenger"]
plt.scatter(d_p['EngineSize'],d_p['MPG.highway'],
            label="Driver & Passenger")
plt.legend(loc="best")     #those colour point are called legends
plt.title("Scatter Plot")
plt.xlabel("EngineSize")
plt.ylabel("MPG.highway")
plt.show()


#seaborn
sns.scatterplot(data= cars93,x= "EngineSize", y="MPG.highway",hue = "AirBags")
plt.title("Scatter Plot")
plt.xlabel("EngineSize")
plt.ylabel("MPG.highway")
plt.show()






