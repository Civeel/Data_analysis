from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 生成地图对象
map = Map()

data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("广东省", 499)
]

# 添加数据
map.add("测试地图1", data, "china")

# 全局配置
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,  # 视觉图分段
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}
        ]
    )
)

# 绘图
map.render(path="测试地图.html")
