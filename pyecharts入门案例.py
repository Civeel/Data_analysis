from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 得到折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据
line.add_yaxis("GDP", [30, 20, 10])
# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="The exhibition of three countries GDP", pos_left="center", pos_bottom="0%"),
    # 设置标题（名称，左右位置，上下位置）
    legend_opts=LegendOpts(is_show=True, pos_bottom="center", pos_left="90%"),
    # 控制图例
    toolbox_opts=ToolboxOpts(is_show=True),
    # 控制工具箱
    visualmap_opts=VisualMapOpts(is_show=True,pos_bottom="12%")
    # 控制视觉图
)

# 生成图表
line.render()
