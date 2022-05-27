# region 问题2.2 求损耗率
# %%
# df2 = pd.read_excel("data/2.1问.xlsx")
# %%
df2 = pd.read_excel("data/附件2 近5年8家转运商的相关数据.xlsx")
# %%
sum = df2.iloc[:, 1:].sum(axis=1)
# %%
mu = (df2.iloc[:, 1:] != 0).astype(int).sum(axis=1)
# %%
df2['平均运输损耗率'] = sum/mu
# %%
from plotnine import *
(
    ggplot(df2)
    + geom_bar(aes("转运商ID", "平均运输损耗率"),stat='identity', width=0.5)
    + theme(text=element_text(family="SimHei"))
)
# 0    1.904769
# 1    0.921370
# 2    0.186056
# 3    1.570482
# 4    2.889825
# 5    0.543761
# 6    2.078833
# 7    1.010283
# %%
df2[['转运商ID','平均运输损耗率']].to_excel('平均运输损耗率.xlsx')
# %%
#endregion