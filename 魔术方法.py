"""
魔术方法：
__init__ 构造方法
__str__ 字符串方法
__lt__ 小于、大于符号比较
__le__ 小于等于、大于等于符号比较
__eq__ ==符号比较
"""


# 字符串方法，内存地址没有多大作用，我们可以通过__str__方法，控制类转换为字符串的行为
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__魔术方法
    def __str__(self):
        return f"student类对象，name={self.name},age={self.age}"

    # __lt__小于符号比较方法
    def __lt__(self, other):
        return self.age < other.age

    # __lt__小于符号比较方法
    def __le__(self, other):
        return self.age <= other.age

    # __lt__小于符号比较方法，如果没有这个方法，比较的就是内存地址
    def __eq__(self, other):
        return self.age == other.age


stu2 = Student("ljj", 21)
stu1 = Student("zjl", 21)
print(stu1)
print(str(stu1))
print(stu1 < stu2)  # __lt__的功能
print(stu1 > stu2)
print(stu1 == stu2)

