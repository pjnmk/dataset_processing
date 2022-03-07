# import pandas as pd

# data_train = pd.read_csv("E:\dataset\\anime Recommendationd database\citeulike_svd_host_1000_train.csv", usecols=["uid"])
# data_train = data_train.drop_duplicates()
# data_train["exsit"] = True
# data_dict = data_train.set_index(['uid'])['exsit'].to_dict()

# data_test = pd.read_csv("E:\dataset\\anime Recommendationd database\citeulike_svd_host_1000_test2.csv")

# for i in range(1, len(data_test)):
#     if data_test.loc[i, 'uid'] in data_dict:
#         continue
#     else:
#         data_test = data_test.drop(index=i, axis=0)
        
# data_test.to_csv("E:\dataset\\anime Recommendationd database\citeulike_svd_host_1000_test.csv",index=None)


# 样本对齐
import pandas as pd
data_1 = pd.read_csv("*.csv")
data_2 = pd.read_csv("*.csv")
#构建共同用户列表
a=data_1['uid'].tolist()
b=data_2['uid'].tolist()
c=list(set(a).intersection(set(b)))
#保留共同用户对应行数据
data_1= data_1[data_1['uid'].isin(c)]
data_2= data_2[data_2['uid'].isin(c)]
data_1.to_csv("*.csv",index=None)
data_2.to_csv("*.csv",index=None)
