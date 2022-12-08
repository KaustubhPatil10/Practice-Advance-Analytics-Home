import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\PG_DBDA\Advanced Analytics\Dec_07")


housing = pd.read_csv("Housing.csv")

#boxplot
#lotsize by bedrooms
sns.boxplot(x='bedrooms',y='lotsize',data= housing)
plt.show()

#boxplot
#price by bathrooms
sns.boxplot(x='bathrms', y='price', data= housing)
plt.show()