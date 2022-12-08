import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\PG_DBDA\Advanced Analytics\Dec_07")


cars93 = pd.read_csv("Cars93.csv")

plt.subplot(2,2,1)
sns.boxplot(data=cars93["Price"])
plt.title("Box Plot")
#plt.show()

plt.subplot(2,2,2)
sns.histplot(data=cars93, x="Price", bins =8)
plt.title("Histogram")
#plt.show()

plt.subplot(2,2,3)
sns.scatterplot(data=cars93, x="EngineSize", y="MPG.highway")
plt.title("Scatter Plot")
#plt.show()

plt.subplot(2,2,4)
sns.barplot(data=cars93, x="AirBags",y ="Price")
plt.title("Bar Plot")
plt.tight_layout()
plt.show()
