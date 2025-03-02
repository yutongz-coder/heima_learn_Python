# 如下嵌套列表，要求对外层列表进行排序
# 排序的依据是内层列表的第二个元素数字
# 以前学习的sorted函数就无法适用了。可以使用列表的sort方法
my_list = [["a", 33], ["b", 44], ["c", 55]]


# 定义排序方法
# 排序1，基于带名函数
# def choose_sort_key(element):
#     return element[1]
#
#
# # reverse=True表示降序
# my_list.sort(key=choose_sort_key, reverse=True)

# 排序2，基于lambda匿名函数
my_list.sort(key=lambda element: element[1], reverse=True)


print(my_list)
