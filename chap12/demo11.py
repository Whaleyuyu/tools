# AUTHOR : 温幸文
# TIME : 2021/6/16  上午11:48
from pathlib import Path

import numpy as np

def cos(f1, f2):
    feature_1 = np.loadtxt(f1, np.uint8)
    feature_2 = np.loadtxt(f2, np.uint8)

    feature_1.dtype = np.float32
    feature_2.dtype = np.float32

    print(feature_1.shape, feature_2.shape)

    feature_1 /= np.linalg.norm(feature_1, axis=0)
    feature_2 /= np.linalg.norm(feature_2, axis=0)

    print(np.sum(feature_1 * feature_2))

f1 = '/home/wenxingwen/Documents/pan.txt'
f2 = '/home/wenxingwen/Documents/dj.txt'
f2 = Path(f2)
print(f2.parent.name)

# cos(f1, f2)