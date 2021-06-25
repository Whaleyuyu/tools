# AUTHOR : 温幸文
# TIME : 2021/5/27  下午5:54
import traceback

print('-------')
try:
    print(10 / 0)
except ZeroDivisionError:
    traceback.print_exc()