"""
语法：
def 函数方法名字(形参名：类型，形参名：类型)：
    pass
"""


def add(x: int, y: int):
    return x+y


def func(data: list):
    pass


# 对返回值进行注解，注解只是建议，不影响运行
def func2(data: list) -> list:
    return data

print(func2(1))  # 运行不会报错，注解只是建议，不影响运行
