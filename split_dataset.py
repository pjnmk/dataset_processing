import pandas as pd
import numpy as np
data = pd.read_csv("E:\dataset\\anime Recommendationd database\citeulike_svd_host_1000_train.csv",error_bad_lines=False)#读数据

data["uid"] = pd.factorize(data["uid"])[0].astype(np.uint64)#将特定列的字符串特征改为无符号整数形式

data = data.drop(["id"],axis=1)#删除特定列

data = data.sample( frac=0.6, replace=False, axis=0)#抽样
# n是选取的行或列个数，frac是选取的比例，replace可不可以重复选同一行，weights是权重-会选取对应列值较大的n行，random_state是随机种子，axis为0是选取行，为1是选取列。

data = data.sample(frac=1.0)#打乱数据顺序

data=data.sort_values(by="id", ascending=True)#按列排序

data_1 = data.iloc[:1067258]#取前n行数据
data.to_csv("E:\dataset\\anime Recommendationd database\citeulike_svd_host_1000_train.csv",index=None)
data_2 = data.iloc[1067258:2051488]
data.to_csv("E:\dataset\\anime Recommendationd database\citeulike_svd_guest_1000_train.csv",index=None) #写数据
