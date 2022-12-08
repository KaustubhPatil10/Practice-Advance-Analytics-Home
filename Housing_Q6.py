import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\PG_DBDA\Advanced Analytics\Dec_07")


housing = pd.read_csv("Housing.csv")


#joint plot
sns.jointplot(data=housing,x="lotsize", y="price", color="red")
plt.title("Joint Plot")
plt.xlabel("Lot Size")
plt.ylabel("Price")
plt.show()