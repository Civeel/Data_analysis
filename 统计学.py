import random

import pandas as pd

# df = pd.read_csv("F:/chap01/exercise1_1.csv", encoding='gbk')
# Table_1 = pd.DataFrame(df)
# Table_1.to_csv("F:/df1.csv", index=False, encoding='UTF-8')

# # 1.2 (1)
# df = pd.read_csv("F:/chap01/exercise1_2.csv", encoding='gbk')
# tab1 = pd.crosstab(df.Sex, df.Survived, margins=True, margins_name='Total')
# print(tab1)
#
# # 1.2 (2)
# tab2 = pd.pivot_table(df, index=['Sex', 'Class'], columns=['Survived', 'Age'], margins=True,
#                       margins_name='Total', aggfunc=len)
# tab2.to_csv("F:/df2.csv", index=False)
# print(tab2)

# 1.3
import numpy.random as npr
r1 = npr.normal(loc=200, scale=10, size=1000)
n1 = pd.cut(r1, bins=7)
Table_2 = n1.value_counts()
print(Table_2)

