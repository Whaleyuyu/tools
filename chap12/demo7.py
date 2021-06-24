# AUTHOR : 温幸文
# TIME : 2021/5/31  上午10:18
# 继承object类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name)
        print(self.age)

# 继承Person类
class Student(Person):
    def __init__(self, name, age, stu_no):
        # 调用父类构造函数
        super().__init__(name, age)
        self.stu_no = stu_no

# 继承Person类
class Teacher(Person):
    def __init__(self, name, age, tea_no):
        # 调用父类构造函数
        super().__init__(name, age)
        self.tea_no = tea_no

s = Student('张三', 18, '1101')
t = Teacher('李四', 28, '0011')
s.info()
t.info()
