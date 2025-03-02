"""
演示动态柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
# 读取数据
f = open("D:/GDP.csv", "r", encoding="GB2312")
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一行数据
data_lines.pop(0)
# 将数据转换为字典存储，格式为：
# {年份：[[国家,GDP],...,[国家，GDP]],...,年份：[[国家,GDP],...,[国家，GDP]]}
# 定义一个字典对象
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])  # 年份转换为整数
    country = line.split(",")[1]   # 国家
    gdp = float(line.split(",")[2])  # 有的GDP使用的是科学计数法，这里全部转换为float
    # 如何判断字典里面有没有指定的key
    # 出现异常表示里面没有year，没有异常则表示里面已经有year
    try:
        data_dict[year].append([country, gdp])
    except KeyError:  # 捕获到异常了，说明没有key year
        data_dict[year] = []  # 如果字典里面没有year，就构建一个空的列表
        data_dict[year].append([country, gdp])

# print(data_dict)
# 创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})
# 排序年份，因为字典的key可能是没有顺序的
# 取出全部的key然后排序
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份前8名的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # x轴添加国家
        y_data.append(country_gdp[1]/100000000)  # y轴添加GDP

    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转x轴和y
    bar.reversal_axis()
    # 设置每一年标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    timeline.add(bar, str(year))

# 设置自动播放
timeline.add_schema(
    play_interval=1000,  # 自动播放的时间间隔
    is_timeline_show=True,  # 是否在自动播放的时候显示时间线
    is_auto_play=True,  # 是否自动播放
    is_loop_play=True  # 是否循环自动播放
)

# 绘图
timeline.render("全球GDP前8.html")
