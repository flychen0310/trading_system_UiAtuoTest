#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/28 15:08
# @Author: jackchen
str1 = '1234568988'
print(str1[:-1])


class Animal(object):

    def __init__(self, name, *args, **kwargs):
        print("Animal的init开始被调用")
        self.name = name
        print("Animal的init的调用结束")


class Lion(Animal):
    def __init__(self, name, age, *args, **kwargs):
        print("Lion的init开始被调用")
        self.age = age
        super().__init__(name, *args, **kwargs)
        print("Lion的init的调用结束")


class Tiger(Animal):
    def __init__(self, name, gender, *args, **kwargs):
        print("Tiger的init开始被调用")
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print("Tiger的init的调用结束")


class Liger(Lion, Tiger):
    def __init__(self, name, age, gender):
        print("Liger的init开始被调用")
        super().__init__(self, name, age, gender)
        print("Liger的init的调用结束")


print(Lion.__mro__)

liger = Liger('luna', 6, '女')
print('name', liger.name)
print('gender', liger.age)
print('age', liger.gender)
