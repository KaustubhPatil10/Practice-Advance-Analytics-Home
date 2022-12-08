import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\PG_DBDA\Advanced Analytics\Dec_07")


housing = pd.read_csv("Housing.csv")


#scatter  plot
sns.scatterplot(data=housing, x= 'lotsize', y= 'price', hue= 'airco')
plt.show()