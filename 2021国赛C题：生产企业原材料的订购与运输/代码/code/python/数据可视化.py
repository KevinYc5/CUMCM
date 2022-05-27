# 数据可视化
# region 画 a，b图
# %%
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1, 1, 100)
y1 = -x + 0.1
y2 = -x - 0.1
y3 = -x
# %%
import mpl_toolkits.axisartist as axisartist
#创建画布
fig = plt.figure(figsize=(8, 8))
#使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111) 

#将绘图区对象添加到画布中
fig.add_axes(ax)
#通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis[:].set_visible(False)
#ax.new_floating_axis代表添加新的坐标轴
ax.axis["x"] = ax.new_floating_axis(0,0)

#给x坐标轴加上箭头
ax.axis["x"].set_axisline_style("->", size = 1.0)
#添加y坐标轴，且加上箭头
ax.axis["y"] = ax.new_floating_axis(1,0)

ax.axis["y"].set_axisline_style("-|>", size = 1.0)
#设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right")
ax.plot(x,y1,linestyle="-.")
ax.plot(x,y2, linestyle='--') 
ax.plot(x,y3) 

ax.fill_between(x, 0.3, y1, alpha=0.3)
plt.xlim((-0.3, 0.3))
plt.ylim((-0.3, 0.3))
#设置坐标轴刻度
# my_x_ticks = np.arange(-2, 2, 0.5)

# my_y_ticks = np.arange(-2, 2, 0.5)
# plt.xticks(my_x_ticks)
# plt.yticks(my_y_ticks)
# %%
# endregion
# region
# %%
df = pd.read_excel("data/问题2.xlsx")
df = df.T
df =df.reset_index()
df = df.iloc[1:, :]
df.columns=['合计2','合计3']
# %%
df = df.fillna(0)
# %%
df
# %%
ar1 = np.array(df['合计2'])
# %%
ar1.reshape(24,8)
# %%
df
# %%
data = [199.555902777778,	5850.85391997084,	5974.10808050543,	1332.84138350215,	0,	5976.58995573448,	0,	5693.84417888425]
# %%
label = [1,2,3,4,5,6,7,8]
# %%
plt.bar(label, data)
plt.xlabel("转运商ID")
plt.ylabel("周平均转运量")
# %%
df = pd.read_csv("data/第三问.csv")
# %%
df = df.reset_index()
# %%
df['index'] = df['index'] + 1
# %%
df['index_'] = df['index'].map({5:8,7:7,1:6,8:5,4:4,2:3,6:2,3:1})
# %%
# %%
df = df.melt(id_vars=["index_","index"])
# %%

(
ggplot(df,aes(x='index_',y='value', fill = 'variable')) #传入数据来源和映射
+ geom_bar(stat='identity') #统计方式为原数据
+ theme(text=element_text(family="SimHei"))
+ xlab("转运商编号")

+ ylab("不同原材料供应商占比")

+ xlim(0,6)
# + scale_x_continuous(breaks=range(1,7,1))

)
# %%
df = pd.DataFrame(
    {
        "A与C的采购价格比值":[0.5, 1, 1.5, 2, 3,4],
        "订购量比值":[1.25053859444714,1.24025882266888, 1.10447226722918,1.10674567848540,1.0728983592134,1.09904625188386]
    }
)

# %%
(
    ggplot(df,aes("A与C的采购价格比值", "订购量比值"))
    + geom_line()
    + geom_point()
    # + geom_smooth()
    + geom_hline(aes(yintercept=1.07), colour="#990000", linetype="dashed")
    + ylim(0.3, 1.5)
    + theme(text=element_text(family="SimHei"))
)
# %% 
# endregion
# region
# %%
df = pd.read_excel("data/task3.xlsx")
# %%
df.columns = ['转运商编号', 'a', 'b', 'c', 'al']
# %%
df1 = df[df['al'] == "1/0.6"][['转运商编号', 'a', 'b', 'c']]
df1 = df1.melt(id_vars=['转运商编号'], var_name='原材料种类')
# %%
(
    ggplot(df1, aes(x='转运商编号', y='value', fill='原材料种类'))
    + geom_bar(stat='identity', width=0.5)
    + theme(text=element_text(family="SimHei"))
    + ylab("不同原材料供应/（$m^3$/每周）")
    + scale_x_continuous(breaks=range(0,9,1))
    + ggtitle('$f_A$ = 1/0.6')
)
# %%
df1 = df[df['al'] == "1/0.72"][['转运商编号', 'a', 'b', 'c']]
df1 = df1.melt(id_vars=['转运商编号'], var_name='原材料种类')
# %%
(
    ggplot(df1, aes(x='转运商编号', y='value', fill='原材料种类'))
    + geom_bar(stat='identity', width=0.5)
    + theme(text=element_text(family="SimHei"))
    + ylab("不同原材料供应/（$m^3$/每周）")
    + scale_x_continuous(breaks=range(0,9,1))
    + ggtitle('$f_A$ = 1/0.72')
)
# %%
df1 = df[df['al'] == "1/0.84"][['转运商编号', 'a', 'b', 'c']]
df1 = df1.melt(id_vars=['转运商编号'], var_name='原材料种类')
# %%
(
    ggplot(df1, aes(x='转运商编号', y='value', fill='原材料种类'))
    + geom_bar(stat='identity', width=0.5)
    + theme(text=element_text(family="SimHei"))
    + ylab("不同原材料供应/（$m^3$/每周）")
    + scale_x_continuous(breaks=range(0,9,1))
    + ggtitle('$f_A$ = 1/0.84')
)
# %%
# endregion 

# region 产能的灵敏度
# endregion