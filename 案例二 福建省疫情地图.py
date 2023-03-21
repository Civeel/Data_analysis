from pyecharts.charts import Map
from pyecharts.options import ToolboxOpts, TitleOpts, VisualMapOpts
import json

f = open("F:/疫情.txt", "r", encoding="UTF-8")
pre_data = f.read()
f.close()
aft_data = json.loads(pre_data)

data = aft_data["areaTree"][0]["children"][9]["children"]

final_data = list()
for FJ_data in data:
    FJ_name = FJ_data["name"] + "市"
    FJ_confirm = FJ_data["total"]["confirm"]
    final_data.append((FJ_name, FJ_confirm))

map = Map().add("福建疫情地图", final_data, "福建").set_global_opts(
    title_opts=TitleOpts(title="福建疫情地图", pos_bottom="1%", pos_left="center"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=(
            {"min": 1, "max": 10, "lable": "1-10", "color": "#CCFFFF"},
            {"min": 11, "max": 30, "lable": "11-30", "color": "#FFFF99"},
            {"min": 31, "max": 45, "lable": "31-45", "color": "#FF9966"},
            {"min": 46, "max": 60, "lable": "46-60", "color": "#FF6666"},
            {"min": 61, "max": 85, "lable": "61-85", "color": "#ED3131"},
            {"min": 86, "max": 100, "lable": "86-99", "color": "#990033"},
        )
    ),
    toolbox_opts=ToolboxOpts(is_show=True, pos_bottom="bottom", pos_left="70%")
).render(path="福建疫情地图.html")





