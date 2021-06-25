# AUTHOR : 温幸文
# TIME : 2021/5/25  上午11:49
"""集合的添加操作"""
s1 = {3, 5, 6, 7, 'Python'}
s1.add(18)  # 添加一个元素
print(s1)  # {3, 5, 6, 7, 'Python', 18}

s2 = ()
s1.update(s2)  # 直接添加一个集合，里面也可以放元组，列表
print(s1)  # {3, 5, 6, 7, 'Python', 18}

"""集合的删除操作"""
s1.remove(3)
print(s1)  # {5, 6, 7, 'Python', 18}
s1.discard(199)
print(s1)  # {5, 6, 7, 'Python', 18}
s1.pop()
print(s1)  # {6, 7, 'Python', 18}
s1.pop()
print(s1)  # {7, 'Python', 18}
s1.clear()
print(s1)  # set()
