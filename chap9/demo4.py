# AUTHOR : 温幸文
# TIME : 2021/5/26  下午4:08
s1 = 'hello|world|python'
s2 = s1.split('|', 1)  # 根据‘|’（默认为空格）来分，最多分一次（默认全分）
print(s2)  # ['hello', 'world|python']

s3 = '5'
print(s3.isnumeric())
print('123四'.isdecimal())  # False
print('123四'.isnumeric())  # True
