import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, LabelOpts, VisualMapOpts

# 美国数据
f_US = open("F:/美国.txt", "r", encoding="UTF-8")
US_data = f_US.read()
# 日本数据
f_JP = open("F:/日本.txt", "r", encoding="UTF-8")
JP_data = f_JP.read()
# 印度数据
f_IN = open("F:/印度.txt", "r", encoding="UTF-8")
IN_data = f_IN.read()

# 去除不符合JSON规范的部分
US_data = US_data.replace("jsonp_1629344292311_69436(", "")
US_data = US_data[:-2]

JP_data = JP_data.replace("jsonp_1629350871167_29498(", "")
JP_data = JP_data[:-2]

IN_data = IN_data.replace("jsonp_1629350745930_63180(", "")
IN_data = IN_data[:-2]

# JSON转python
US_dict = json.loads(US_data)
JP_dict = json.loads(JP_data)
IN_dict = json.loads(IN_data)

# 获取trend key
US_trend_data = US_dict['data'][0]['trend']
JP_trend_data = JP_dict['data'][0]['trend']
IN_trend_data = IN_dict['data'][0]['trend']

# 获取日期数据，给到x轴，只取2020年
US_x_data = US_trend_data['updateDate'][:314]
JP_x_data = JP_trend_data['updateDate'][:314]
IN_x_data = IN_trend_data['updateDate'][:314]

# 获取确诊数据，用于y轴，只取2020年
US_y_diagnosed_data = US_trend_data['list'][0]['data'][:314]
JP_y_diagnosed_data = JP_trend_data['list'][0]['data'][:314]
IN_y_diagnosed_data = IN_trend_data['list'][0]['data'][:314]

# 获取治愈数据，用于y轴，只取2020年
US_y_cured_data = US_trend_data['list'][1]['data'][:314]
JP_y_cured_data = JP_trend_data['list'][1]['data'][:314]
IN_y_cured_data = IN_trend_data['list'][1]['data'][:314]

# 获取死亡数据，用于y轴，只取2020年
US_y_death_data = US_trend_data['list'][2]['data'][:314]
JP_y_death_data = JP_trend_data['list'][2]['data'][:314]
IN_y_death_data = IN_trend_data['list'][2]['data'][:314]

# 获取新增确诊数据，用于y轴，只取2020年
US_y_newlyDiagnosed_data = US_trend_data['list'][3]['data'][:314]
JP_y_newlyDiagnosed_data = JP_trend_data['list'][3]['data'][:314]
IN_y_newlyDiagnosed_data = IN_trend_data['list'][3]['data'][:314]

# 生成图表
line = Line()
line.add_xaxis(US_x_data)  # 共用x轴数据
line.add_yaxis("美国确诊人数", US_y_diagnosed_data, label_opts=LabelOpts(is_show=False))  # 图例设置
line.add_yaxis("日本确诊人数", JP_y_diagnosed_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", IN_y_diagnosed_data, label_opts=LabelOpts(is_show=False))

line.add_yaxis("美国治愈人数", US_y_cured_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本治愈人数", JP_y_cured_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度治愈人数", IN_y_cured_data, label_opts=LabelOpts(is_show=False))

line.add_yaxis("美国死亡人数", US_y_death_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本死亡人数", JP_y_death_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度死亡人数", IN_y_death_data, label_opts=LabelOpts(is_show=False))

line.add_yaxis("美国新增确诊人数", US_y_newlyDiagnosed_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本新增确诊人数", JP_y_newlyDiagnosed_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度新增确诊人数", IN_y_newlyDiagnosed_data, label_opts=LabelOpts(is_show=False))

# 全局配置
line.set_global_opts(
    title_opts=TitleOpts(title="2020年三国疫情折线图", pos_left="center", pos_bottom="bottom"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True, pos_bottom="2%", pos_left="65%"),
    visualmap_opts=VisualMapOpts(is_show=True, pos_bottom="bottom", pos_left="0%", orient="horizontal", is_calculable=True, max_=10000000)
)

line.render(path="2020年三国疫情折线图.html")  # 自定义图名和文件名

# 关闭文件
f_US.close()
f_JP.close()
f_IN.close()
