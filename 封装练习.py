class Phone:
    # 私有成员变量，True表示开启5g，False表示关闭5g
    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()
