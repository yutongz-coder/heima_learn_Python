# 子类继承父类的成员属性和成员方法之后，如果对其不满意，可以进行复写
# 即在子类中重新定义同名的属性或方法即可

class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("5g")


# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "ITHEIMA"  # 复写父类的成员属性

    def call_by_5g(self):
        # 还想使用父类的同名属性，有2种方法调用父类成员
        # # 方法一
        print(f"父类的厂商是：{Phone.producer}")
        Phone.call_by_5g(self)  # 一定要记得传入self
        # # 方法二
        # print(f"父类的厂商是：{super().producer}")
        # super().call_by_5g()

        print("开启CPU单核模式，确保通话的时候省电")


phone = MyPhone()
phone.call_by_5g()
print(f"厂商是：{phone.producer}")


