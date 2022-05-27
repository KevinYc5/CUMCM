# region 问题3 求分级 和 优先级 a>b>c的条件下的优先顺序以满足产能需要 
# 通过聚类将供应商分级
# 
# %%
df3_X = df1_X.sort_values("企业生产重要性", ascending= False)
# %% 
df3_X = df3_X.dropna(axis=0, how='any')
# %%
alist = []
blist = []
clist = []
for n in range(15, 300, 5):
    print(n)
    df3_selected = df3_X.head(n)
    alist.append(df3_selected['材料分类'].value_counts()['A'])
    blist.append(df3_selected['材料分类'].value_counts()['B'])
clist = [ 15 + 5*i - alist[i] - blist[i] for i in range(57)]
# %% 计算比率
for i in range(len(alist)):
    sum = alist[i] + blist[i] + clist[i]
    alist[i] = alist[i]/sum
    blist[i] = blist[i]/sum
    clist[i] = clist[i]/sum

# %%
tmp = []
for i in range(len(alist)):
    tmp.append((15 + 5*i, alist[i], "A"))
    tmp.append((15 + 5*i, blist[i], "B"))
    tmp.append((15 + 5*i, clist[i], "C"))

# %%
zhu = pd.DataFrame(tmp)
zhu.columns = ["n", "mix", "材料分类"]
# %% 
(
ggplot(zhu,aes(x='n',y='mix', fill = '材料分类'))#传入数据来源和映射
+ geom_bar(stat='identity', width=4)#统计方式为原数据
+ theme(text=element_text(family="SimHei"))
+ xlab("选择供应商数量/(个)")
+ ylab("不同原材料供应商占比")
+ scale_x_continuous(breaks=range(0,300,50))

)
# %%
df3_X['材料分类'].value_counts()
# A    126
# B    118
# C    104
# %% 聚类 
from sklearn.cluster import KMeans
SSE = []
x = np.array(df3_X['企业生产重要性'])
y = x.reshape(-1,1)

for k in range(1,11):
    estimator = KMeans(n_clusters=k)  # 构造聚类器
    estimator.fit(y)
    SSE.append(estimator.inertia_)
X = range(1,11)
plt.xlabel('k')
plt.ylabel('SSE')
plt.plot(X,SSE,'o-')
#%%
from plotnine import *
df_plt = pd.DataFrame({"k":X, "均方差":SSE})
(
    ggplot(df_plt, aes("k", "均方差"))
    + geom_line(size=1)
    + geom_point( size=3)
    + scale_x_continuous(breaks = range(0, 11,1))
    + theme(text=element_text(family="SimHei"))
)

# %% 聚类得到 label
estimator = KMeans(n_clusters=4)  # 构造聚类器
estimator.fit(y)
labels = [estimator.labels_]
# %%
labels
# %%
df_label = pd.DataFrame(labels)
df_label = df_label.T
df_label.columns = ["label"]
df_label["label"] = df_label["label"].map({0:0, 1:2, 2:1, 3:3})
# %% 将 label 加入 df3x中
df_1 = df3_X.reset_index(drop=True)
df_2 = df_label.reset_index(drop=True)
df3_X_ = pd.concat([df_1,df_2], axis = 1)
# %%
(
    ggplot(df3_X_.reset_index())
    + geom_line(aes("index","企业生产重要性", color='label'))
)
# %%
df_ = df3_X_[df3_X_["label"] == 3]
df3_fenzu1 = pd.concat([df_[df_['材料分类'] == 'A'],df_[df_['材料分类'] == 'B'],df_[df_['材料分类'] == 'C']], axis=0).reset_index()
df_ = df3_X_[df3_X_["label"] == 2]
df3_fenzu2 = pd.concat([df_[df_['材料分类'] == 'A'],df_[df_['材料分类'] == 'B'],df_[df_['材料分类'] == 'C']], axis=0).reset_index()
df_ = df3_X_[df3_X_["label"] == 1]
df3_fenzu3 = pd.concat([df_[df_['材料分类'] == 'A'],df_[df_['材料分类'] == 'B'],df_[df_['材料分类'] == 'C']], axis=0).reset_index()
df_ = df3_X_[df3_X_["label"] == 0]
df3_fenzu4 = pd.concat([df_[df_['材料分类'] == 'A'],df_[df_['材料分类'] == 'B'],df_[df_['材料分类'] == 'C']], axis=0).reset_index()
df3_fenzu = pd.concat([df3_fenzu1,df3_fenzu2,df3_fenzu3, df3_fenzu4],  axis=0).reset_index()
df3_fenzu = df3_fenzu[['供应商ID', '材料分类', '总订货量', '总订货次数', '周供货量', '可靠度',
       '供应实力', '平均可靠度增长率', '供应商信誉实力', '合作亲密指数', '企业生产重要性', '50 家最重要的供应商',
       'label']]

# %%
# df3_fenzu['企业生产重要性'].plot()
(
    # 42, 121,170
    ggplot(df3_fenzu.reset_index() )
    + theme(text=element_text(family="SimHei"))
    + geom_line(aes("index", "企业生产重要性",shape="label"))
    + geom_vline(aes(xintercept=42), colour="#990000", linetype="dashed")
    + geom_vline(aes(xintercept=121), colour="#990000", linetype="dashed")
    + geom_vline(aes(xintercept=170), colour="#990000", linetype="dashed")
    + xlab("优先级序号")
    # + geom_area(aes(x="index", y="企业生产重要性", fill="材料分类"))
)
# %%
tp_ = df3_fenzu[['材料分类', '总订货量', '总订货次数', '周供货量', '可靠度', '供应实力', '平均可靠度增长率',
       '供应商信誉实力', '合作亲密指数', '企业生产重要性']].head(20)
tp_['材料分类'] = tp_['材料分类'].map({"A":1, "B":2, "C":3})
tp_.to_excel("matlab1.xlsx")
# %% 选择满足需求的吗？
n = 0 
cost = 2.82e4
tmp = 0
f = [1/0.6, 1/0.66, 1/0.72]
for i, row in df3_X.iterrows():
    n = n + 1
    tmp = tmp + row['周供货量'] * f[ord(row['材料分类']) - 65] * row['可靠度']
    if(tmp > cost) :
        print("n: ", n)
        break
    print(row['周供货量'] * f[ord(row['材料分类']) - 65] * row['可靠度'])
    print(tmp)
    print("---------------")
# %%
alist = []
blist = []
clist = []
for n in range(15, 300, 5):
    # print(n)
    df3_selected = df3_fenzu.head(n)
    alist.append(df3_selected['材料分类'].value_counts()['A'])
    blist.append(df3_selected['材料分类'].value_counts()['B'])
clist = [ 15 + 5*i - alist[i] - blist[i] for i in range(57)]
# %% 计算比率
for i in range(len(alist)):
    sum = alist[i] + blist[i] + clist[i]
    alist[i] = alist[i]/sum
    blist[i] = blist[i]/sum
    clist[i] = clist[i]/sum

# %%
tmp = []
for i in range(len(alist)):
    tmp.append((15 + 5*i, alist[i], "A"))
    tmp.append((15 + 5*i, blist[i], "B"))
    tmp.append((15 + 5*i, clist[i], "C"))

# %%
zhu = pd.DataFrame(tmp)
zhu.columns = ["n", "mix", "材料分类"]
# %% 
(
ggplot(zhu,aes(x='n',y='mix', fill = '材料分类'))#传入数据来源和映射
+ geom_bar(stat='identity', width=4)#统计方式为原数据
+ theme(text=element_text(family="SimHei"))
+ xlab("选择供应商数量/(个)")
+ ylab("不同原材料供应商占比")
+ scale_x_continuous(breaks=range(0,300,50))
)