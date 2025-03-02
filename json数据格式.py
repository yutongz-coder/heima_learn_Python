"""
演示JSON数据和Python字典的相互转换,json本质上是一个字符串
"""
import json
# 准备列表
data = [{"name": "周", "age": 18}, {"name": "x", "age": 15}]
json_str = json.dumps(data, ensure_ascii=False)  # 将数据转换为字符串
# ensure_ascii=False表示直接输出内容
print(type(json_str))
print(json_str)
# 准备字典，将字典转换为json,json就是有特殊格式的字符串
data2 = {"name": "周", "age": 17}
json_str2 = json.dumps(data2)  # 将数据转换为字符串
# ensure_ascii=False表示直接输出内容， 没有就是输出ASCII码
print(type(json_str2))
print(json_str2)
# 将json字符串转换为python数据类型
s = '[{"name":"周","age":18},{"name":"x","age":15}]'
l = json.loads(s)  # list
print(type(l))
print(l)
# 将json字符串转换为python数据类型
s2 = '{"name":"周","age":18}'
# 长得和字典一模一样的字符串也能转换成python字符串
l2 = json.loads(s2)  # list
print(type(l2))
print(l2)