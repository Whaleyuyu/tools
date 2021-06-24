# AUTHOR : 温幸文
# TIME : 2021/6/15  下午2:31

# 测试第2步
import os

from tqdm import tqdm


def get_time(image_path):
    return image_path.split('_')[-3]


def get_FCnt(image_path):
    begin = image_path.rfind('FCnt') + 4
    end = image_path.rfind('.raw') if image_path.rfind('.raw') != -1 else image_path.rfind('.yuv')
    return int(image_path[begin:end])


leaf = []
fileName = '/media/wenxingwen/PTCJ010/himax/6-7/2949/'
for p,d,fs in os.walk(fileName):
    for f in fs:
        leaf.append(fileName+f)


# x1 = '/media/wenxingwen/PTCJ010/himax/6-7/2949/2949b/2949b&M_GN_D070_FCT_TC_A00K_N0023_Depth_1280x800_raw8x2_2dE14%2.97msS14%2.97ms-1mA_3dE14%2.97msS14%2.97ms1600mA_2021-06-07_10-17-50_AeOn_FCnt20454.raw'
# x2 = '/media/wenxingwen/PTCJ010/himax/6-7/2949/2949b/2949b&M_GN_D070_FCT_TC_A00K_N0023_Depth_1280x800_raw8x2_2dE14%2.97msS14%2.97ms-1mA_3dE14%2.97msS14%2.97ms1600mA_2021-06-07_10-17-50_AeOn_FCnt20460.raw'
# leaf.append(x1)
# leaf.append(x2)
rgb_map = {(get_time(x), get_FCnt(x)): x for x in leaf}

kk = rgb_map.keys()
fcnts = sorted(kk, key=lambda x: x[1])
fcnts = sorted(fcnts, key=lambda x: x[0])

for fc in fcnts:
    print(fc)

# groups = []
# begin = 0
# for i in range(1, len(fcnts)):
#     if fcnts[i][1] - fcnts[i - 1][1] != 1:
#         print(fcnts[i][1],fcnts[i - 1][1])
#         groups.append(fcnts[begin:i])
#         begin = i
# groups.append(fcnts[begin:])

