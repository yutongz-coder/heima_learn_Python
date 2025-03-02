# def test(a,b):
#     print(a+b)

# if __name__ == "__main__":
#     test(1,2)
# # 内置变量__name__运行时自动标记成__main__

__all__ = ["test_a"]
# all是一个列表，指定*当中哪些可以导入

def test_a(a,b):
    print(a + b)

def test_b(a,b):
    print(a - b)    