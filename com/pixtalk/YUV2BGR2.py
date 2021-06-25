# AUTHOR : 温幸文
# TIME : 2021/5/21  下午2:10
import os
import numpy as np
import cv2


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

    for src, dirNames, fileNames in os.walk(file_name):
        # 目标文件夹
        dest = file_name + "_BGR"
        # 如果目标主文件夹不存在
        if not os.path.exists(dest):
            os.mkdir(dest)
        for fileName in fileNames:
            subFile1 = os.path.join(src, fileName)
            subFile2 = os.path.join(dest, fileName)

            # 如果子路径不存在
            if not os.path.exists(subFile2):
                os.mkdir(subFile2)

            # 用于判断是否BGR文件
            keyword = 'BGR'

            if keyword in fileName:
                bgrTurn(subFile1, subFile2, height, width)
            else:
                irTurn(subFile1, subFile2, height, width)

        break

    return None


# NV12转BGR函数
def bgrTurn(subFile2, subFile1, height, width):
    with open(subFile1, 'rb') as f1:
        frame_size = height * width * 3 // 2  # 一帧BGR图像所含的像素个数
        # 建立一个零矩阵，矩阵数据都是8位无符号整数，按行排列
        yyyy_uv = np.zeros(shape=frame_size, dtype='uint8', order='C')
        for i in range(frame_size):
            k = f1.read(1)
            # bytes转int要使用这个方法
            # 两个判断k的范围是否合法
            if int.from_bytes(k, 'big') < 0:
                k = bytes([0])
            elif int.from_bytes(k, 'big') > 255:
                k = bytes([255])
            # 判断k是否空值，很重要，因为ord实参不能为空值
            elif len(k) == 0:
                continue
            yyyy_uv[i] = ord(k)  # 读取 YUV 数据，并转换为 unicode

    img = yyyy_uv.reshape((height * 3 // 2, width)).astype(
        'uint8')  # NV12 的存储格式为：YYYY UV 分布在两个平面（其在内存中为 1 维）
    bgr_img = cv2.cvtColor(img, cv2.COLOR_YUV2BGR_NV12)  # 由于 opencv 不能直接读取 YUV 格式的文件, 所以要转换一下格式
    if "NV12" in subFile1:
        cv2.imwrite(subFile2.replace("NV12", "bmp"),
                    bgr_img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)    cv2.imwrite(fileName2.replace("NV12", "bmp"), bgr_img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)
    else:
        cv2.imwrite(subFile2 + ".bmp", bgr_img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)cv2
    # print("准备转换" + fileName2)

    print("搞定一个BGR")

    return None


# NV12转IR函数
def irTurn(subFile2, subFile1, height, width):
    with open(subFile1, 'rb') as f1:
        frame_size = height * width  # 一帧BGR图像所含的像素个数
        # 建立一个零矩阵，矩阵数据都是8位无符号整数，按行排列
        yyyy_uv = np.zeros(shape=frame_size, dtype='uint8', order='C')
        for i in range(frame_size):
            k = f1.read(1)
            # bytes转int要使用这个方法
            if int.from_bytes(k, 'big') < 0:
                k = bytes([0])
            elif int.from_bytes(k, 'big') > 255:
                k = bytes([255])
            elif len(k) == 0:
                continue
            yyyy_uv[i] = ord(k)  # 读取 YUV 数据，并转换为 unicode
    img = yyyy_uv.reshape((height, width)).astype('uint8')  # NV12 的存储格式为：YYYY UV 分布在两个平面（其在内存中为 1 维）
    # print("准备转换" + fileName2)
    if "NV12" in subFile2:
        cv2.imwrite(subFile2.replace("NV12", "bmp"), img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)
    else:
        cv2.imwrite(subFile2 + ".bmp", img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)cv2
    # print("准备转换" + fileName2)


    print("搞定一个IR")

    return None
