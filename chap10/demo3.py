# AUTHOR : 温幸文
# TIME : 2021/5/27  下午2:15
# 后面指定关键字参数
def fun1(a, *, d, r):
    print(a)
    print(d)
    print(r)


fun1(1, d=5, r=6)
