# AUTHOR : 温幸文
# TIME : 2021/5/18  下午4:45
import os
from time import sleep

import numpy as np
import cv2
from tqdm import tqdm

"""
这个程序是将解压好的NV12图片文件夹处理出一个新的BGR图片的文件夹
适用于BGR和IR一样大的数据
"""


# 分割大的YUV文件的函数
def split_packed_yuv(yuv_packed_file_path, height, width):
    # 检查文件路径是否存在
    if os.path.exists(yuv_packed_file_path):
        for root, dirs_name, files_name in os.walk(yuv_packed_file_path):
            for i in files_name:
                # 拼接路径
                file_name = os.path.join(root, i)
                print(file_name)

                # YUV一个像素占1.5字节
                single_yuv_size = height * width * 1.5
                dst_path = file_name + "_single"

                os.mkdir(dst_path)

                # 分成single_yuv_size个字节，并添加'.NV12'这个后缀
                command = "split -b %d --additional-suffix='.NV12' %s" % (single_yuv_size, file_name)
                os.system(command)
                command = "mv *.NV12 %s" % dst_path
                os.system(command)

    else:
        print("The file open fail.")


def yuv2bgr(file_name, height, width):
    """
    :param file_name: 待处理 YUV 文件夹的名字
    :param height: YUV 图像的高
    :param width: YUV 图像的宽
    :return: None
    """
    if not os.path.exists(file_name):
        print("文件不存在！！！")
        return None

    d = {}

    for src, dirNames, fileNames in os.walk(file_name):
        # 目标文件夹
        if "NV12" in file_name:
            # 创建一个新目录，即把原来的文件夹的名字中的NV12改为BGR
            dest = os.path.join(os.path.dirname(file_name), file_name.replace("NV12", "BGR"))
        else:
            dest = file_name + "_BGR"
        # 如果目标主文件夹不存在，就创建
        if not os.path.exists(dest):
            os.mkdir(dest)
        for dirName in dirNames:
            subDir1 = os.path.join(src, dirName)
            subDir2 = os.path.join(dest, dirName)
            # 子文件夹判空操作，空文件夹则不转换
            if not os.listdir(subDir1):
                print(subDir1 + "是空文件夹！")
                continue
            # 如果子路径不存在
            if not os.path.exists(subDir2):
                os.mkdir(subDir2)

            # 调用转换方法
            # Turn(subDir2, subDir1, height, width)

            d = GetAllPath(subDir2, subDir1, d)

        AllTurn(d, height, width)

        break

    return None


# 将所有文件路径的对应关系存放在一个字典中
def GetAllPath(subDir2, subDir1, d):
    for pathName, dirNames, fileNames in os.walk(subDir1):
        # 对每一个子路径下的NV12文件
        for file in fileNames:
            fileName1 = os.path.join(subDir1, file)
            fileName2 = os.path.join(subDir2, file)
            d[fileName1] = fileName2
    return d


# 将字典所有路径指向的文件进行转换
def AllTurn(d, height, width):
    for fileName1 in tqdm(d, colour='#FFFFFF', ncols=150):
        fileName2 = d[fileName1]
        with open(fileName1, 'rb') as f1:
            frame_size = height * width * 3 // 2  # 一帧BGR图像所含的像素个数
            # 建立一个零矩阵，矩阵数据都是8位无符号整数，按行排列
            yyyy_uv = np.zeros(shape=frame_size, dtype='uint8', order='C')
            '''仅判断文件大小及字符长度版本'''
            f1.seek(0, 2)  # 设置文件指针到文件流的尾部 + 偏移 0
            f1_end = f1.tell()  # 获取文件尾指针位置
            if f1_end < frame_size:
                continue
            f1.seek(0, 0)
            for i in range(frame_size):
                k = f1.read(1)
                if len(k) == 0:
                    continue
                yyyy_uv[i] = ord(k)

        img = yyyy_uv.reshape((height * 3 // 2, width)).astype(
            'uint8')  # NV12 的存储格式为：YYYY UV 分布在两个平面（其在内存中为 1 维）
        bgr_img = cv2.cvtColor(img, cv2.COLOR_YUV2BGR_NV12)  # 由于 opencv 不能直接读取 YUV 格式的文件, 所以要转换一下格式

        # 新代码，保证NV12在最后面
        if fileName2.endswith(".NV12"):
            cv2.imwrite(fileName2.replace("NV12", "bmp"), bgr_img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)
        else:
            fileName2 = fileName2.replace(".", "_")
            cv2.imwrite(fileName2 + ".bmp", bgr_img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)


# NV12转BGR函数,已弃用，未实现模块化
def Turn(subDir2, subDir1, height, width):
    for pathName, dirNames, fileNames in os.walk(subDir1):
        # 对每一个子路径下的NV12文件
        for file in tqdm(fileNames, colour='#FFFFFF', ncols=150):
            fileName1 = os.path.join(subDir1, file)
            fileName2 = os.path.join(subDir2, file)
            with open(fileName1, 'rb') as f1:
                frame_size = height * width * 3 // 2  # 一帧BGR图像所含的像素个数
                # 建立一个零矩阵，矩阵数据都是8位无符号整数，按行排列
                yyyy_uv = np.zeros(shape=frame_size, dtype='uint8', order='C')
                '''仅判断文件大小及字符长度版本'''
                f1.seek(0, 2)  # 设置文件指针到文件流的尾部 + 偏移 0
                f1_end = f1.tell()  # 获取文件尾指针位置
                if f1_end < frame_size:
                    continue
                f1.seek(0, 0)
                for i in range(frame_size):
                    k = f1.read(1)
                    if len(k) == 0:
                        continue
                    yyyy_uv[i] = ord(k)

            img = yyyy_uv.reshape((height * 3 // 2, width)).astype(
                'uint8')  # NV12 的存储格式为：YYYY UV 分布在两个平面（其在内存中为 1 维）
            bgr_img = cv2.cvtColor(img, cv2.COLOR_YUV2BGR_NV12)  # 由于 opencv 不能直接读取 YUV 格式的文件, 所以要转换一下格式

            # 新代码，保证NV12在最后面
            if fileName2.endswith(".NV12"):
                cv2.imwrite(fileName2.replace("NV12", "bmp"), bgr_img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)
            else:
                fileName2 = fileName2.replace(".", "_")
                cv2.imwrite(fileName2 + ".bmp", bgr_img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)
            # print('搞定' + fileName2)

    # print("\n搞定一个", att)
    # sleep(0.01)

    return None


if __name__ == '__main__':
    fheight = 640
    fwidth = 360
    filePath1 = '/home/wenxingwen/Downloads/0624_RGB_noBG_common'
    split_packed_yuv(filePath1, fheight, fwidth)
    filePath2 = filePath1 + '_NV12'
    os.rename(filePath1, filePath2)
    yuv2bgr(file_name=filePath2, height=fheight, width=fwidth)
