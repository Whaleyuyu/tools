# AUTHOR : 温幸文
# TIME : 2021/5/27  下午2:32
def p(n):
    sum = 1
    res = list()
    for i in range(n):
        res.append(i + 1)
    for j in res:
        sum *= j
        print(j, '的阶乘是', sum)


p(6)
