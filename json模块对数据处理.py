# 处理数据
import json
from pyecharts.charts import Line

f_us = open("D:/美国.txt","r",encoding="UTF-8")
us_data = f_us.read() #美国的全部内容
# 去掉不合JSON规范的结尾
us_data = us_data.replace(","," ")
# JSON转python字典
us_dict = json.loads(us_data)
# print(type(us_dict))
# print(us_dict)
# 获取trend key
us_trend_data = us_dict["data"][0]["trend"]

# 获取日期数据
us_x_data = us_trend_data["updateDate"][:314]
# print(x_data)
# 获取确认数据
us_y_data = us_trend_data["list"][0]["data"][:314]

# 生成图表
line = Line() # 构建折线图对象
# 添加x轴数据
line.add_xaxis(us_x_data)
line.add_yaxis(us_y_data)
# 调用render方法生成图表
line.render()
# 关闭文件
f_us.close()