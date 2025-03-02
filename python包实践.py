"""
演示my_package包
"""
# 创建一个包
# 导入自定义的包中的模块并使用
# import my_package.my_module1
# import my_package.my_module2
# my_package.my_module2.info_print2()
# my_package.my_module1.info_print1()

# 第二种导入方式
# from my_package import my_module1
# from my_package import my_module2
# my_module1.info_print1()
# my_module2.info_print2()

# 第三种导入方式
# from my_package.my_module1 import info_print1
# from my_package.my_module2 import info_print2
# info_print1()
# info_print2()

# 导入*
# from my_package import *
# my_module1.info_print1()
# my_module2.info_print2()

"""
my_utils演示
"""
import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("heima"))
# 如果把上面那一行注释掉，就不会输出str_util模块里面的print,因为print是在main下面的，直接运行str_util时才会运行main下面的代码
print(my_utils.str_util.substr("heima",0,2))

file_util.append_to_file("D:/test_append.txt","zyt")
file_util.print_file_info("D:/test_append.txt")