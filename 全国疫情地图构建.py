import json
from pyecharts.charts import Map
from pyecharts.options import *
# 读取数据文件
f = open("D:/疫情.txt", "r", encoding="UTF-8")
data = f.read()  # 全部数据
# 关闭文件
f.close()
# 取到各省数据
# 将字符串json转换为python的字典
data_dict = json.loads(data)  # 基础数据字典
# 从字典中取出省份的数据
province_data_list = data_dict["areaTree"][0]["children"]
# 组装每个省份和确诊人数为元组，将各个省份的数据封装入列表内
data_list = []  # 绘图需要用的数据列表
for province_data in province_data_list:
    province_name = province_data["name"]  # 省份名称
    province_confirm = province_data["total"]["comfirm"]  # 确诊人数
    data_list.append(province_name, province_confirm)
print(data_list)

# 创建地图对象
map = Map()
# 添加数据
map.add("各省份确诊人数", data_list, "china")
# 设置全局配置
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  #是否显示
        is_piecewise=True,  #是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999", "color": "#990033"}
        ]
    )
)

map.render("全国疫情地图.html")