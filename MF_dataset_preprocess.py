data = pd.read_csv("E:\资料\研究生\大创\dataset\\anime-1\\rating.csv",error_bad_lines=False)#读数据
# data[['uid', 'iid']] = data[['iid', 'uid']] #两列交换
data = data[~data['rate'].isin([-1])]
for index, row in data.iteritems():
    if index!="uid" and index!="iid" and index!="rate":
        data = data.drop([index], axis=1)#删除特定列

# data = data.sample(frac=1.0)#打乱数据顺序
# data["uid"] = pd.factorize(data["uid"])[0].astype(np.uint64)#将特定列的字符串特征改为无符号整数形式
# data = data.sample(frac=1.0)#打乱数据顺序
# data["iid"] = pd.factorize(data["iid"])[0].astype(np.uint64)#将特定列的字符串特征改为无符号整数形式
# data = data.sample(frac=1.0)#打乱数据顺序

data = data.groupby("iid").filter(lambda x: x.iloc[0]['iid']<10000)   #删除数据少的行
data = data.groupby("uid").filter(lambda x: x.iloc[0]['uid']<10000)   #删除数据少的行

# max_min_scaler = lambda x: (x - np.min(x)) / (np.max(x) - np.min(x))
# data['rate']=data[['rate']].apply(max_min_scaler)#rate列归一化

guest = data.groupby("iid").filter(lambda x: x.iloc[0]['iid']<5000)
host = data.groupby("iid").filter(lambda x: x.iloc[0]['iid']>=5000 )
guest = guest.groupby("uid").filter(lambda x: len(x) > 9)
host = host.groupby("uid").filter(lambda x: len(x) > 9)

guest = guest.sample(frac=1.0)#打乱数据顺序
host = host.sample(frac=1.0)#打乱数据顺序
guest.insert(0, 'id', range(len(guest)))
host.insert(0, 'id', range(len(host)))
guest_test = guest.groupby(guest['uid']).apply(lambda x:x.sample(frac=0.2))
d = guest_test['id'].tolist()
guest_train= guest[~guest['id'].isin(d)]
host_test = host.groupby(host['uid']).apply(lambda x:x.sample(frac=0.2))
e = host_test['id'].tolist()
host_train= host[~host['id'].isin(e)]

f=guest_train['iid'].tolist()
guest_test= guest_test[guest_test['iid'].isin(f)]
g=host_train['iid'].tolist()
host_test= host_test[host_test['iid'].isin(g)]

guest_train=guest_train.sort_values(by="id", ascending=True)#按列排序
guest_test=guest_test.sort_values(by="id", ascending=True)#按列排序
host_train=host_train.sort_values(by="id", ascending=True)#按列排序
host_test=host_test.sort_values(by="id", ascending=True)#按列排序
guest_train.to_csv("E:\迅雷下载\\citeulike_svd_guest_1000_train.csv",index=None)
guest_test.to_csv("E:\迅雷下载\\citeulike_svd_guest_1000_test.csv",index=None)
host_train.to_csv("E:\迅雷下载\\citeulike_svd_host_1000_train.csv",index=None)
host_test.to_csv("E:\迅雷下载\\citeulike_svd_host_1000_test.csv",index=None)
