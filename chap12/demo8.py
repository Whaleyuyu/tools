# AUTHOR : 温幸文
# TIME : 2021/5/31  上午10:46
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name)
        print(self.age)

class Student(Person):
    def __init__(self, name, age, stu_no):
        # 调用父类构造函数
        super().__init__(name, age)
        self.stu_no = stu_no

    # 重写父类方法
    def info(self):
        # 调用被重写的方法
        super().info()
        print('学生编号是：', self.stu_no)


class Teacher(Person):
    def __init__(self, name, age, tea_no):
        # 调用父类构造函数
        super().__init__(name, age)
        self.tea_no = tea_no

    def info(self):
        super().info()
        print('教师编号是：', self.tea_no)


s = Student('张三', 18, '1101')
t = Teacher('李四', 28, '0011')
print(s)
s.info()
print('---------------------')
t.info()
