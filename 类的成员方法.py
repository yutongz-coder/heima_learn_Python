# 类里面可以定义属性和行为
# 行为就是写到类里面的函数，成为成员行为
# 类内部的属性就是成员变量
# self是定义成员方法的时候的关键字
# 定义一个带有成员方法的类
class Student:
    name = None

    def say_hi1(self):
        print(f"i am {self.name}, hello")

    def say_hi2(self, msg):
        print(f"hello, i am {self.name}, {msg}")


stu = Student()
stu.name = "zjl"
stu.say_hi2("i like you")   # 调用的时候不用写self
stu.say_hi1()

