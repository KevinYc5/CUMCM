# 数据预处理
# region import package needed
# %% 

import math
from os import access
from numpy import array
import pandas as pd
import numpy as np
from plotnine import *
import matplotlib.pyplot as plt
from plotnine.labels import xlab
plt.rcParams['font.sans-serif'] = ['SimHei']#声明黑体解决中文乱码,这里有好几种方式，篇幅有限，一种就够了
plt.rcParams['axes.unicode_minus'] = False
import warnings
warnings.filterwarnings(action = 'ignore')#忽略代码运行过程中的警告信息

# %% 决策树
from sklearn.model_selection import train_test_split,KFold,LeaveOneOut,LeavePOut
from sklearn.model_selection import cross_val_score,cross_validate#计算交叉验证下的测试误差 
from sklearn.preprocessing import LabelEncoder
import sklearn.linear_model as LM
from sklearn.metrics import classification_report
from sklearn.datasets import make_regression
from sklearn import tree
# %%
# endregion
# region 数据预处理
# %% 
df1_din = pd.read_excel('data/附件1 近5年402家供应商的相关数据.xlsx',sheet_name="企业的订货量（m³）")
df1_gong = pd.read_excel('data/附件1 近5年402家供应商的相关数据.xlsx',sheet_name="供应商的供货量（m³）")

# df1 = pd.read_excel("data/附件1 近5年402家供应商的相关数据.xlsx")
# df2 = pd.read_excel("data/附件2 近5年8家转运商的相关数据.xlsx")
# df3 = pd.read_excel("data/附件A 订购方案数据结果.xlsx")
# df4 = pd.read_excel("data/附件B 转运方案数据结果.xlsx")
# %% 数据整体信息 删除不考虑的数据

t_ = df1_din.iloc[:, 2:]
t_[t_ < 10] = 0
df1_din.iloc[:, 2:] = t_

t__ = df1_gong.iloc[:, 2:]
t__[t_ < 10] = 0
df1_gong.iloc[:, 2:] = t__
