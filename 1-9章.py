"""
# if 语句的基本格式（判断语句）
# else不需要条件
age = input("请输入你的年龄：")
age = int(age)
if age >= 18:
    print(f"she is a grown up")
else:
    print(f"she is under 18") # 需要四个空格作为缩进
print("have a nice day")

print("welcome！")
height = int(input("please input your height:"))
if height > 120:
    print("you should buy tickets")
else:
    print("you don't have to buy tickets")
print("have a nice trip")


height = int(input("height:"))
vip_level = int(input("vip_level:"))
vip_level = 4
if(height <= 120):
    print("not free")
elif(vip_level >= 3):
    print("free")
else:
    print("not free")



print("欢迎来到黑马动物园")
if int(input("请输入你的身高：")) > 120:
    print("你的身高大于120，不可以免费")
    print("不过如果你的VIP等级高于3，可以免费")

    if int(input("请输入你的vip等级")) > 3:
        print("可以免费游玩")
    else:
        print("不免费")
else:
    print("欢迎小朋友")


# 构建随机数字
import random
num = random.randint(1,10)
# print(num)
guess_num = int(input("输入你要猜测的数字:"))
#开始猜测
if guess_num == num:
    print("猜中了")
else:
    if guess_num > num:
        print("猜大了")
    else:
        print("猜小了")
print(num)


# 生成随机数字
import random
num = random.randint(1,100)
# 通过一个布尔类型的变量，做循环是否继续的标记
flag = True
# 记录猜测次数
count = 0
while flag:
    guess_num = int(input("请输入你猜测的数据："))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")
print(f"总共猜了{count}次")


# 定义全局变量money name
money = 5000000
name = None

# 要求客户输入姓名
name = input("请输入您的姓名：")
# 定义查询函数
def query(show_header):
    if show_header:
        print("---查询余额---")
    print(f"{name}您好，您的余额剩余：{money}元")

# 定义存款函数
def saving(num):
    global money
    money += num
    print("---存款---")
    print(f"{name}您好，您的余额剩余：{money}元")
    query(False)

# 定义取款函数
def get_money(num):
    global money
    money -= num
    print("---取款---")
    print(f"{name}您好，您的余额剩余：{money}元")
    query(False)
# 定义主菜单函数
def main():
    print("---主菜单---")
    print(f"{name}:欢迎，请选择操作：")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("退出\t\t【输入4】")
    return input("请输入您的选择")

#设置无限循环，确保程序不退出
while True:
    keyboard_input = main() # main函数输出的就是input，input赋值给keyboard_input
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int(input("您想要存多少钱，请输入："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取多少钱，请输入："))
        get_money(num)
        continue
    else:
        print("程序退出")
        break
    """    


from my_module1 import *
test_a(1,2)
test_b(2,1)

        