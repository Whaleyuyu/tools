# AUTHOR : 温幸文
# TIME : 2021/6/24  上午9:58
import os
import time

if __name__ == '__main__':
    # tftp文件夹
    tftpDir = '/tftp'
    # 检查时间间隔
    timeGap = 1
    # 存放yuv文件路径的字典
    yuvPaths = {}
    # 新的大小
    sizeNew = {}
    # 旧的大小
    sizeOld = {}
    for path, dirs, files in os.walk(tftpDir):
        for f in files:
            if 'yuv' in f:
                yuvPaths[f] = tftpDir + '/' + f

while True:
    if len(sizeOld) == 0:
        for f in yuvPaths:
            sizeOld[f] = os.path.getsize(yuvPaths[f])
        time.sleep(timeGap)

    elif len(sizeNew) == 0:
        for f in yuvPaths:
            sizeNew[f] = os.path.getsize(yuvPaths[f])
        for f in yuvPaths:
            speed = (sizeNew[f] - sizeOld[f]) / timeGap / 1024
            if speed != 0:
                print(f, '的速度是:', (sizeNew[f] - sizeOld[f]) / timeGap / 1024, 'KB每秒')
        time.sleep(timeGap)

    else:
        for f in yuvPaths:
            sizeOld[f] = sizeNew[f]
            sizeNew[f] = os.path.getsize(yuvPaths[f])
        for f in yuvPaths:
            # 以KB为单位
            speed = (sizeNew[f] - sizeOld[f]) / timeGap / 1024
            if speed != 0:
                print(f, '的速度是:', (sizeNew[f] - sizeOld[f]) / timeGap / 1024, 'KB每秒')
        time.sleep(timeGap)
