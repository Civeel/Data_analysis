from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts, ToolboxOpts
import json
f = open("F:/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()

data_dict = json.loads(data)

province_data_list = data_dict["areaTree"][0]["children"]

# 组装每个省份和确诊人数为元组数据
data_list = list()
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))

map = Map()
map.add("2021-8-18全国疫情地图", data_list, maptype="china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图", pos_left="center", pos_bottom="1%"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "lable": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100-999", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000-4999", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000-9999", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "lable": "10000-99999", "color": "#CC3333"},
            {"min": 100000, "lable": "100000", "color": "#990033"},
        ]
    ),
    toolbox_opts=ToolboxOpts(is_show=True, pos_bottom="bottom", pos_left="70%")
)

map.render(path="2021-8-18全国疫情地图.html")
