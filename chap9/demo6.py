# AUTHOR : 温幸文
# TIME : 2021/5/27  上午9:44
s1 = "我爱"
s2 = s1.encode()
print(s2)  # b'\xe6\x88\x91\xe7\x88\xb1'
s2 = s1.encode('UTF-8')
print(s2)  # b'\xe6\x88\x91\xe7\x88\xb1'
s2 = s1.encode('GBK')
print(s2)  # b'\xce\xd2\xb0\xae'
