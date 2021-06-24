# AUTHOR : 温幸文
# TIME : 2021/6/10  下午2:12
import os.path
from pathlib import Path
from time import sleep
from tqdm import tqdm
import time



# 负责判断数据大小是否符合要求的方法
def if_size_ok(file, type):
    size = os.path.getsize(file)
    # 如果是RGB
    if type == 1:
        if size == 2050560:
            return True
        else:
            return False
    # 非RGB
    else:
        if size == 2048000:
            return True
        else:
            return False


data = Path('/media/wenxingwen/PTCJ010/himax/')
uns = set()
ls = []
dest = open('/home/wenxingwen/Documents/工作笔记/河南测试集/第三批/第6次/空文件.md', 'w')

for pathname, dirnames, filenames in tqdm(os.walk(data), colour='#FFFFFF', ncols=150):
    for filename in filenames:
        testp = Path(pathname) / Path(filename)

        if 'RGB' in filename:
            if not if_size_ok(testp, 1):
                uns.add(testp.parent)
        else:
            if not if_size_ok(testp, 2):
                uns.add(testp.parent)

for un in uns:
    ls.append(str(un))
ls.sort()

for lst in ls:
    dest.write(lst)
    dest.write('\n')

dest.flush()
dest.close()
# size = os.path.getsize(data)
# print(size)
