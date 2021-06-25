# AUTHOR : 温幸文
# TIME : 2021/5/25  下午6:19
s1 = {1, 2, 3, 4, 5, 6, 7}
s2 = {1, 2, 3, 4, 5, 6, 7}
s3 = {1, 2, 3}
s4 = {7, 8}

print(s1 == s2)  # True
print(s3.issubset(s1))  # True
print(s1.issuperset(s3))  # True
print(s1.isdisjoint(s4))  # False
