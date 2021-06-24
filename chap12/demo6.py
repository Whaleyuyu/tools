# AUTHOR : 温幸文
# TIME : 2021/5/28  下午2:32
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, '在吃饭')


def dance():
    print('在跳舞')


s1 = Student('张三', 20)
s1.gender = '男'
s1.dance = dance
print(s1.name, s1.age, s1.gender)
s1.dance()
