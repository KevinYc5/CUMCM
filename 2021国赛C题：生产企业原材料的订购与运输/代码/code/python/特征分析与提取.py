# %% X5 总订货量
df1_X = pd.DataFrame()
df1_X['供应商ID'] = df1_din['供应商ID']
df1_X['材料分类'] = df1_din['材料分类']
df1_X['X5'] = df1_din.iloc[:,2:].sum(axis=1)
# %% 总订货次数
df1_X['X4'] = (df1_din.iloc[:,2:] != 0).astype(int).sum(axis=1)
# %% 总供货量 -->周供货量
df1_X['X1'] = df1_gong.iloc[:,2:].sum(axis=1)

# 最大供货量
df_zhou_max = pd.DataFrame()
df_zhou_max['X1'] = df1_gong.iloc[:,2:].max(axis=1)
# %% 可靠度 X 2
df_ = (df1_gong.iloc[:,2:] / df1_din.iloc[:,2:])
# %%
count = (df_).count(axis=1)
# %%
df_ = df_.fillna(0)
df_[df_ > 1] = 1
# %%
df1_X['X2'] = df_.sum(axis=1)/count
df1_X['X2'].fillna(0)
# %% 供货实力 V
df1_X['V'] = df1_X['X1'] / count
df1_X['X1'] = df1_X['X1'] / count
# %% 可靠性变化率
df_ = (df1_gong.iloc[:,2:] / df1_din.iloc[:,2:])
for i, r in df_.iterrows():
    s = r
    s = s.dropna()
    if s.diff().sum()/s.count() >= -1000:
        df1_X.loc[i,"X3"] =  s.diff().sum()/s.count()
    else:
        df1_X.loc[i,"X3"] = 0
    # tmp_.append(s.diff().sum()/s.count())
    # if(i == 0):
        # print(s.diff().sum()/s.count())
        # s.hist()

# %% 信誉指数 C
df1_X['C'] = df1_X['X3'].map( lambda x : 1/(1+np.exp(-x))) * df1_X['X2']
# %% 合作关系实力 S
df_ = pd.DataFrame()
df_['X4'] = (df1_X['X4'] - df1_X['X4'].min())/(df1_X['X4'].max()-df1_X['X4'].min())
df_['X5'] = (df1_X['X5'] - df1_X['X5'].min())/(df1_X['X5'].max()-df1_X['X5'].min())

df1_X['S'] = df1_X['X4'].map( lambda x : 1/(1+np.exp(-x))) *  df_['X4'] + df1_X['X5'].map( lambda x : 1/(1+np.exp(-x))) * df_['X5']


# %% 熵权法
# 标准化 C S V
df1_X['S'] = (df1_X['S'] - df1_X['S'].min())/(df1_X['S'].max()-df1_X['S'].min())
df1_X['C'] = (df1_X['C'] - df1_X['C'].min())/(df1_X['C'].max()-df1_X['C'].min())
df1_X['V'] = (df1_X['V'] - df1_X['V'].min())/(df1_X['V'].max()-df1_X['V'].min())
# %%

# %%
df1_X['V'].describe()
# %%
df1_X.plot.scatter("V", "C")
# %%
df1_X.plot.scatter("S", "C")
# %%
df1_X.plot.scatter("S", "V")

# %%
#定义熵值法函数
def cal_weight(x):
    '''熵值法计算变量的权重'''
    # 标准化
    # x = x.apply(lambda x: ((x - np.min(x)) / (np.max(x) - np.min(x))))
 
    # 求k
    rows = x.index.size  # 行
    cols = x.columns.size  # 列
    k = 1.0 / math.log(rows)
 
    lnf = [[None] * cols for i in range(rows)]
 
    # 矩阵计算--
    # 信息熵
    # p=array(p)
    x = array(x)
    lnf = [[None] * cols for i in range(rows)]
    lnf = array(lnf)
    for i in range(0, rows):
        for j in range(0, cols):
            if x[i][j] == 0:
                lnfij = 0.0
            else:
                p = x[i][j] / x.sum(axis=0)[j]
                lnfij = math.log(p) * p * (-k)
            lnf[i][j] = lnfij
    lnf = pd.DataFrame(lnf)
    E = lnf
 
    # 计算冗余度
    d = 1 - E.sum(axis=0)
    # 计算各指标的权重
    w = [[None] * 1 for i in range(cols)]
    for j in range(0, cols):
        wj = d[j] / np.sum(d)
        w[j] = wj
        # 计算各样本的综合得分,用最原始的数据
 
    w = pd.DataFrame(w)
    return w
# %%
# 计算 df 各字段的权重
df1_X = df1_X.dropna(axis=0)
df = df1_X[['C', 'S', 'V']]
w = cal_weight(df)  # 调用cal_weight
w.index = df.columns
w.columns = ['weight']
print(w)
print('运行完成!')
     weight
C  0.157066
S  0.330897
V  0.512036
运行完成!