# AUTHOR : 温幸文
# TIME : 2021/5/27  下午2:44
def feipo(n):
    lst0 = [1, 1]
    print(lst0[0])
    print(lst0[1])
    if n > 2:
        for i in range(n - 2):
            temp = lst0[0] + lst0[1]
            lst0.pop(0)
            lst0.append(temp)
            # print('第', i + 3, '个斐波那契数是', lst0[1])
            print(lst0[1], end=' ')
            if i % 6 == 0:
                print()


feipo(100)
