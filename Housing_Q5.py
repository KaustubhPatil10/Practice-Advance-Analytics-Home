import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\PG_DBDA\Advanced Analytics\Dec_07")


housing = pd.read_csv("Housing.csv")


#Facet Grid by bathrooms
g=sns.FacetGrid(data=housing,col="bathrms")
g=g.map(plt.scatter,"price","lotsize",color="orange")
plt.show()



g=sns.FacetGrid(data=housing,row="bathrms")
g=g.map(plt.scatter,"lotsize","price",color="blue")
plt.show()