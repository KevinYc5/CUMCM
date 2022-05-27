# %%
df1_X['企业生产重要性'] = w.loc["C","weight"] * df1_X["C"] \
    + w.loc["S","weight"] * df1_X["S"] \
    + w.loc["V","weight"] * df1_X["V"]
# %%
df_sort = df1_X.sort_values("企业生产重要性", ascending=False)
# %% 直接取前50
df_res = df_sort.head(50)
df_res['材料分类'].value_counts()
# %%

# %% 按照 18. 17. 15 选
# df_res = pd.concat([df_sort[df_sort["材料分类"] == "A"].head(18), \
#     df_sort[df_sort["材料分类"] == "B"].head(17), \
#     df_sort[df_sort["材料分类"] == "C"].head(15)], axis=0)
# df_res = df_res.sort_values("企业生产重要性", ascending=False)
# %%
df_  =df_res.reset_index()
df_["企业生产重要性"].plot()
# %%
df1_X['50 家最重要的供应商'] = 0
df1_X.loc[df_['index'], "50 家最重要的供应商"] = 1
# %% 绘制 所有企业按企业序号 
# %%
# --重要性
from plotnine import *
(
    ggplot(df1_X.reset_index())
    + geom_point(aes('index', '企业生产重要性', shape='材料分类'))
    + geom_hline(yintercept = 0.393355,
        color='red',    # set line colour
        size=1,            # set line thickness
        linetype="dashed"  # set line type
        )
    # + theme(legend_position = 'none')
    + theme(text=element_text(family="SimHei"))
    # + geom_text(aes(label='efef', x=0, y=0.121))
    # + annotate('text', x=0, y = 0.121, label='0.121', size=2)
    + xlab("供应商ID")
)
# %%

# %%
df1_X.columns=['供应商ID', '材料分类', '总订货量', '总订货次数', '周供货量', '可靠度', '供应实力', '平均可靠度增长率', '供应商信誉实力', '合作亲密指数', '企业生产重要性',
       '50 家最重要的供应商']
       
# %%
df1_din.T.iloc[3:, 2].plot()
# %%
(
    ggplot(df1_X.reset_index())
    + geom_point(aes('index', '企业生产重要性', fill =  '50 家最重要的供应商'))
    # + theme(legend_position = 'none')
    + theme(text=element_text(family="SimHei"))
)
# %%
(
    ggplot(df1_X.reset_index())
    + geom_point(aes('index', '合作亲密指数', fill =  '50 家最重要的供应商'))
    # + theme(legend_position = 'none')
    + theme(text=element_text(family="SimHei"))
)
# %%
(
    ggplot(df1_X.reset_index())
    + geom_point(aes('index', '供应商信誉实力', fill =  '50 家最重要的供应商'))
    # + theme(legend_position = 'none')
    + theme(text=element_text(family="SimHei"))
)
# %%
(
    ggplot(df1_X.reset_index())
    + geom_point(aes('合作亲密指数', '供应实力', fill =  '50 家最重要的供应商'))
    # + theme(legend_position = 'none')
    + theme(text=element_text(family="SimHei"))
)
# %%
(
    ggplot(df1_X.reset_index())
    + geom_point(aes('供应商信誉实力', '供应实力', fill =  '50 家最重要的供应商'))
    # + theme(legend_position = 'none')
    + theme(text=element_text(family="SimHei"))
)
# %%
(
    ggplot(df1_X.reset_index())
    + geom_point(aes('供应商信誉实力', '合作亲密指数', fill =  '50 家最重要的供应商'))
    # + theme(legend_position = 'none')
    + theme(text=element_text(family="SimHei"))
)
# %%
