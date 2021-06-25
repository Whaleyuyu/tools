# AUTHOR : 温幸文
# TIME : 2021/5/27  上午10:27
def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd, even


n = [12, 424, 235, 1245, 626, 2]
print(fun(n))
