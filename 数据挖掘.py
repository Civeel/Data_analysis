import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

# df = pd.read_csv("F:/birth-rate.csv")
# # print(df.describe())
#
# birth_rate_2008 = df['2008']  # 拿出2008年的数据
# # print(birth_rate_2008)
# birth_rate_2008_droped = birth_rate_2008.dropna()  # 去除带空值的数据行
# # print(birth_rate_2008_droped)
#

# # 直方图
# num_bins = int((max(birth_rate_2008_droped) - min(birth_rate_2008_droped)) // 2)
# plt.hist(birth_rate_2008_droped, num_bins, density=True, edgecolor='r')  # 直方图（数据，组数，是否归一化，条形边框颜色）
# plt.title('the world birth-rate in 2008')
# plt.xlabel('amount')
# plt.ylabel('the rate of birth in world')
# plt.grid(linestyle='-', alpha=0.5)  # 添加格子
# # plt.show()
#

# # 箱型图
# data = pd.read_excel('f:/catering_sale.xls', index_col='日期')
# # print(data.describe())
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
# plt.figure()
# p = data.boxplot(return_type='dict')  # 画箱型图
# x = p['fliers'][0].get_xdata()  # ‘fliers为异常值的标签
# y = p['fliers'][0].get_ydata()
# y.sort()  # 从小到大排序
# for i in range(len(x)):
#     if i > 0:
#         plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
#     else:
#         plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))
# plt.show()


# 频率分布直方图
# df = pd.read_excel('f:/catering_sale.xls')
# data_sale = df['销量']
# stas = data_sale.describe()
# # print(stas)
# stas['range'] = stas['max'] - stas['min']  # 在stas中增加一行名为range（极差）的数据
# # print(stas['range'])
# labels = ['[0-1k)', '[1k-2k)', '[2k-3k)', '[3k-4k)',
#           '[4k-5k)', '[5k-6k)', '[6k-7k)', '[7k-8k)', '[8k-9k)']  # 标签
# df['sales class'] = pd.cut(data_sale, bins=9, labels=labels)  # 分割数据
# # print(df)
# aggResult = df.groupby(by=['sales class'])['销量'].agg(np.size)
# # print(aggResult)
# paggResult = round(aggResult / aggResult.sum(), 2) * 100
# # print(paggResult)
# plt.figure(figsize=(16, 9))
# paggResult.plot(kind='bar', width=0.8, fontsize=10, edgecolor='r')
# plt.title("Quarter Sales Chart", fontsize=28)
# plt.xticks(rotation=45)
# plt.ylabel('Percentage', fontsize=15)
# plt.grid(linestyle='-', alpha=0.5)
# plt.show()


# # 柱状+折线
# '''
# 柱状图部分
# '''
# df = pd.read_csv('f:/Data/flight_delays.csv')
# month_delay = df.sum(axis=1)  # 默认按列相加
# month_delay1 = round(month_delay / 14, 2)  # 平均每家公司的delay时间
# plt.figure(figsize=(16, 9))
# plt.bar(x=df['Month'],
#         height=month_delay1,
#         tick_label=df['Month'],
#         width=0.8,
#         color='mediumslateblue',
#         alpha=0.6,
#         label='Average delay',  # 图例名称
#         edgecolor='r'  # 边框颜色
#         )
#
# '''
# 折线图部分
# '''
# df_month_delay_F9 = df['F9']
# plt.plot(df['Month'],
#          df_month_delay_F9,
#          linestyle='-',
#          linewidth=2,
#          color='g',
#          markersize=3,
#          label='AirlineF9'
#          )
# plt.title('Average Arrival Delay for ASF')
# plt.xlabel('Month')
# plt.ylabel('By minute')
# plt.legend()  # 是否显示图例
# plt.show()


# # 热力图(by seaborn)
# df = pd.read_csv('f:/Data/flight_delays.csv')
# plt.figure(figsize=(16, 9))
# sns.heatmap(data=df,
#             annot=True,  # 数据标签
#             cmap='inferno_r'  # 颜色模式，_r代表颜色反转（颜色可去matplotlib.org找）
#             )
# plt.title('Average Arrival Delay for ASF')
# plt.xlabel('Airline')
# plt.show()


# 折线图(plot)
# spotify = pd.read_csv('f:/Data/spotify.csv')
# plt.figure(figsize=(16, 10))
# plt.plot(spotify.Date,
#          spotify['Shape of You'],
#          linestyle='-',
#          linewidth=2,
#          color='slateblue',
#          label='Shape of You'
#          )
# plt.plot(spotify.Date,
#          spotify['Despacito'],
#          linestyle='-',
#          linewidth=2,
#          color='r',
#          label='Despacito'
#          )
# plt.plot(spotify.Date,
#          spotify['Something Just Like This'],
#          linestyle='-',
#          linewidth=2,
#          color='g',
#          label='Something Just Like This'
#          )
# plt.title('2017-2018 US spotify Pop Streaming Numbers', fontsize=24)
# plt.xlabel('Date', fontsize=15)
# plt.ylabel('Songs', fontsize=15)
# plt.xticks(range(0, len(spotify['Date']), 20), rotation=45)
# axes = plt.gca()  # 获取当前图标的坐标轴
# axes.ticklabel_format(style='plain', axis='y')  # 对轴进行操作，style决定是否使用科学计数法
# plt.legend()
# plt.show()

# 折线图(seaborn)
spotify = pd.read_csv('f:/Data/spotify.csv', index_col='Date', parse_dates=True)  # 将索引列解析为pandas中的时间格式
plt.figure(figsize=(16, 9))
sns.lineplot(data=spotify)
axes = plt.gca()
axes.ticklabel_format(style='plain', axis='y')
plt.show()

