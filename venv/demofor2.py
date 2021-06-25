# AUTHOR : 温幸文
# TIME : 2021/5/12  下午4:02
sum = 0
for item in range(100, 1000):
    a = item // 100
    b = (item % 100) // 10
    c = (item % 10)
    if a**3 + b**3 + c**3 == item:
        print(str(item) + "是水仙花数")
        sum += item
print("100~999水仙花数之和为" + str(sum))

