#留一法拆分数据集
import pandas as pd
import numpy as np
data = pd.read_csv("E:\资料\研究生\大创\dataset\\anime Recommendationd database\citeulike_svd_guest_1000.csv",error_bad_lines=False)#读数据
test = data.groupby(data['uid']).apply(lambda x:x.sample(frac=0.2))
test.to_csv("E:\资料\研究生\大创\dataset\\anime Recommendationd database\citeulike_svd_guest_1000_test.csv",index=None)
a = test['id'].tolist()
train= data[~data['id'].isin(a)]
train.to_csv("E:\资料\研究生\大创\dataset\\anime Recommendationd database\citeulike_svd_guest_1000_train.csv",index=None)
