"""
演示面向对象的多态特性以及抽象类（接口）的使用
多态常用在继承关系上
比如函数，以父类做定义声明，以子类做实际工作，用以获得同一行为不同状态
"""

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("wangwangwang")


class Cat(Animal):
    def speak(self):
        print("miaomiaomiao")


def make_noise(animal: Animal):
# 制造噪音，需要传入Animal对象
    animal.speak()


# 演示多态，使用2个子类来调用函数
dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


# 如果父类的函数（方法）是空实现，这就是一个抽象类（也称为接口），含有抽象方法的类称之为抽象类，
# 方法体是空实现的（pass）称之为抽象方法。
# 这种设计的意义是，父类用来确定有哪些方法，具体的方法实现，由子类自行决定


class AC:
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_l_r(self):
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷技术")

    def hot_wind(self):
        print("美的空调加热技术")

    def swing_l_r(self):
        print("美的左右摆风技术")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷技术")

    def hot_wind(self):
        print("格力空调加热技术")

    def swing_l_r(self):
        print("格力左右摆风技术")


def make_cool(ac: AC):
    ac.hot_wind()


midea_ac = Midea_AC()
gree_ac = GREE_AC()
make_cool(midea_ac)
make_cool(gree_ac)
