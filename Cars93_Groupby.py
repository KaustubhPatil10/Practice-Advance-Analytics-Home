import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\PG_DBDA\Advanced Analytics\Dec_07")


cars93 = pd.read_csv("Cars93.csv")


########## Group by Aggregate ###################

cars93["Price"].mean()

no_bags= cars93[cars93["AirBags"] == "None"]
driver= cars93[cars93["AirBags"] == "Driver only"]
d_p= cars93[cars93["AirBags"] == "Driver & Passenger"]

cars93.groupby('AirBags')['Price'].mean()


cts=cars93.groupby('AirBags')['Price'].mean()
#seaborn
cts1= cts.reset_index()
cts1.columns = ['Type', 'Count']
sns.barplot(data=cts1, x= 'Type', y='Count')
plt.show()

#basic
cts=cars93.groupby('AirBags')['Price'].mean()
cts1= cts.reset_index()
sns.barplot(data=cts1, x='AirBags', y='Price')
plt.ylabel("mean price")
plt.show()


#Matplotlib
plt.bar(cts.index, cts)
plt.show()
















