# AUTHOR : 温幸文
# TIME : 2021/5/25  上午11:33
s = {'Python', 3, 5, 5, 6, 7, 7}
print(s)  # {1, 3, 5, 6, 7}

s1 = set([1, 3, 5, 5, 6, 7, 7])
print(s1)  # {1, 3, 5, 6, 7}

s2 = set('Python')
print(s2)  # {'P', 'o', 't', 'h', 'n', 'y'}

s3 = set({'Python', 3, 5, 5, 6, 7, 7})
print(s3)  # {1, 3, 5, 6, 7}

s4 = set((1, 3, 5, 5, 6, 7, 7))
print(s4)  # {1, 3, 5, 6, 7}
