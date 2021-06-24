# AUTHOR : 温幸文
# TIME : 2021/5/28  下午12:00
class Student:
    native_town = '吉林'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, '在吃饭')

    @staticmethod
    def study():
        print("静态方法，学生在上课")

    @classmethod
    def walk(cls):
        print('类方法，学生在走路')


s = Student('张三', 18)
s.eat()
Student.study()
Student.walk()
