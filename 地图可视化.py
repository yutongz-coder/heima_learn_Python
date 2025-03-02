
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
map = Map()

# 准备数据
# 要把省份名字写完整“省”，地图才会显示出来数据
data = [
    ("北京市",99),
    ("湖南省",299),
    ("广东省",399),
    ("上海市",499),
    ("重庆市", 399)
]

# 添加数据
map.add("测试地图", data, "china")  # china只有小写才能把html加载出来

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,  # 表示允许手动校准范围
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}
        ]
    )
)

#绘图
map.render()