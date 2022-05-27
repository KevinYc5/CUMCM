# region 问题2 求最小n
# %%
df2_X = df1_X.sort_values("企业生产重要性", ascending= False).head(50)
# %%
df2_X.reset_index(inplace=True)
# %%
df2_X['周供货量'].plot()
# %%
df1_din.iloc[200, 2:].sum()/(df1_din.iloc[200, 2:] != 0).astype(int).sum()
# %%  以 200 举例 说明删除较小值的必要性
fig, ax = plt.subplots()
ttt = df1_din.iloc[200, 2:]
ttt.plot(ax=ax)
ax.axhline(y=1673.24, linestyle=':', color="red")
ax.axhline(y=7116.30, linestyle='-.', color="red")
ax.text(-20,1673.24, "{:.0f}".format(1673.24), color="red",ha="right", va="center")
ax.text(-20,7116.30, "{:.0f}".format(7116.30), color="red",ha="right", va="center")
     
ax.set_xlabel("时间/(周数)")
ax.set_ylabel("向 S201供应商订购量/($m^3$)")
# %%
# (
#     ggplot(df1_din.iloc[200, 2:])
#     ++ geom_point(aes(""))
# )

# %%
df1_sort = df1_X.sort_values("企业生产重要性",ascending=False)


# %%
df_zhou_max.reset_index(inplace=True)
# %%
df_ = pd.concat([df1_X, df_zhou_max['X1']], axis=1)
df_res = df_.sort_values("企业生产重要性", ascending=False)
# %%
n = 0 
cost =  2.82e4
tmp = 0
f = [1/0.6, 1/0.66, 1/0.72]
for i, row in df_.sort_values("企业生产重要性",ascending=False) .iterrows():
    n = n + 1
    tmp = tmp + row['周供货量'] * f[ord(row['材料分类']) - 65] * row['可靠度']
    if(tmp > cost) :
        print("n: ", n)
        break
    print(row['周供货量'] * f[ord(row['材料分类']) - 65] * row['可靠度'])
    print(i, tmp)
    print("---------------")
# %%
df_res['周供货量'].count()
# 348 / 402
# %%
df_res1 = df_res.head(19)
# %%
df_res1['材料分类'] = df_res1['材料分类'].map({"A":1, "B":2, "C":3})
# %%
df_res1.to_excel("matlab.xlsx")
# %%

# %%
# endregion