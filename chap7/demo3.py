# AUTHOR : 温幸文
# TIME : 2021/5/17  下午3:42
scores = {"张三": 97, "李四": 98, "王五": 99}
k = scores.keys()
v = scores.values()

print(list(k))
print(list(v))

'''字典生成式'''
k0 = ['张三', '李四', '王五']
v0 = [97, 98, 99]

s = {k1: v1 for k1, v1 in zip(k0, v0)}
print(s)


