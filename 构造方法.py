"""
__init__()构造方法
在创建类对象的时候会自动执行（不需要调用）
在创建类对象（构造类）的时候，将括号里面的传入参数自动传递给__init__方法使用
"""


class Student:
    name = None
    age = None
    tel = None  # 这三行成员变量其实可以不写

    def __init__(self, name, age, tel):
        self.name = name
        self.tel = tel
        self.age = age
        print("Student类创建了一个类对象")


stu = Student("zjl", 31, 321)  # 如果没有构造方法，是没法直接这么传入参数的
print(stu.name)
print(stu.age)
print(stu.tel)
print(stu)  # 返回的是内存地址，但是没有用，用字符串方法（魔术方法）可以变成返回信息

