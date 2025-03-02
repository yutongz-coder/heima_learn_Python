# 类型注解：变量：类型
# https://blog.csdn.net/A_No2Tang/article/details/111300675
# 上文是关于容器类型
import random
import json
# 为变量设置类型注解
var_1: int = 10
var_2: float = 3.1415
var_3: bool = True
var_4: str = "itheima"


# 类对象类型注解
class Student:
    pass
stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {"itheima": 666}
my_str: str = "itheima"

# 容器类型详细注解
my_list: list[int, str, int] = [1, "2", 3]
my_tuple: tuple[str, int, bool] = ("itheima", 66, True)
my_set: set[int] = {1, 2, 3}
my_dict: dict[str, int] = {"itheima": 66}

print(my_tuple)
print(my_list)

# 在注释中进行类型注解
var_1 = random.randint(1, 20)  # type: int
var_2 = json.loads('{"name":"zhangda"}')  # type: dict[str,str]


def func():
    return 10


var_3 = func()  # type: int

