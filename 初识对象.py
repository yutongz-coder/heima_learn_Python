# 设计一个类
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None


# 创建一个对象
stu_1 = Student()
# 对象属性进行赋值
stu_1.name = "abc"
stu_1.age = 18
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "重庆市"
# 获取对象中记录的信息
print(stu_1.native_place)
