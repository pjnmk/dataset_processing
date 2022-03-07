import pandas as pd
import numpy as np

data = pd.read_csv("E:\资料\研究生\大创\dataset\\anime Recommendationd database\\rating.csv")
data = data[~data['rate'].isin([-1])]
data.to_csv("E:\资料\研究生\大创\dataset\\anime Recommendationd database\\rating.csv",index=None)
