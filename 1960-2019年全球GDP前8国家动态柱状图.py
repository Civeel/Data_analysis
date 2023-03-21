from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取文件
f = open("F:/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
f.close()

# 删除第一天无用数据
data_lines.pop(0)

# 将数据转换为字典储存
data_dict = dict()
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    GDP = float(line.split(",")[2])
    try:
        data_dict[year].append([country, GDP])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, GDP])

# 添加时间线
timeline = Timeline(
    {"theme": ThemeType.LIGHT}
)

# 排序年份
sorted_year_dict = sorted(data_dict.keys())
for year in sorted_year_dict:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][:8]
    x_data = list()
    y_data = list()
    for country_GDP in year_data:
        x_data.append(country_GDP[0])  # x轴添加国家
        y_data.append(country_GDP[1] / 100000000)  # y轴添加GDP

    # 添加柱状图对象
    bar = Bar()

    # 反转数据，绘图时大数据在上
    x_data.reverse()
    y_data.reverse()

    # 添加x，y轴数据
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()

    # 全局配置
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}全球前8的GDP情况", pos_left="center", pos_top="6%"),
        toolbox_opts=ToolboxOpts(is_show=True, pos_left="70%", pos_top="top"),
    )
    timeline.add(bar, str(year))

# 自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

timeline.render("1960-2019年全球GDP前8国家.html")
