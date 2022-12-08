import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\PG_DBDA\Advanced Analytics\Dec_07")


cars93 = pd.read_csv("Cars93.csv")

#joint plot
sns.jointplot(data=cars93,x= "EngineSize",y ="MPG.highway")
plt.show()