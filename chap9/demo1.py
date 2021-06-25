# AUTHOR : 温幸文
# TIME : 2021/5/26  上午10:39
import sys

s1 = '123'
s2 = sys.intern(s1)
print(s1 is s2)  # TRUE

