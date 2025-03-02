"""
演示面向对象：继承的基础语法
"""


# 演示单继承
class Phone:
    IMEI = None  # 序列号
    producer = "HM"  # 厂商

    def call_by_4g(self):
        print("2023功能，4g通话")


class Phone2024(Phone):
    face_id = "10001"  # 面部识别ID

    def call_by_5g(self):
        print("2024新功能，5g通话")


phone = Phone2024()
phone.call_by_4g()
phone.call_by_5g()
print(phone.producer)
print(phone.IMEI)


# 演示多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")


class MyPhone(Phone, NFCReader, RemoteControl):
    pass  # 不想再添加新功能了，表示这里什么都没有，也不好报错


phone = MyPhone()
phone.call_by_4g()
phone.control()
phone.read_card()
phone.write_card()
# 多继承时，对于同名成员，谁在左先继承谁

