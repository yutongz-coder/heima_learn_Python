# 私有成员变量，变量名字以__开头
# 私有成员方法，方法名字以__开头
# 私有成员无法被类对象使用，但是可以被其他成员使用
# 定义一个类，内含私有成员变量和私有成员方法

class Phone:

    __current_voltage = 0.1  # 当前手机运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

# call_by_5g可以使用类里面的私有方法__keep_single_core
    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已经开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g")


phone = Phone()
# phone.__keep_single_core() 无法运行
phone.call_by_5g()



