# AUTHOR : 温幸文
# TIME : 2021/5/26  下午3:40
s1 = '7+-hello,world'
s2 = s1.upper()
print(s1 is s2)  # False
print(s1)  # hello,world
s3 = s1.lower()
print(s1 is s3)  # False
s4 = s1.title()
print(s4)  # Hello,World

print(s1.zfill(20))
