# AUTHOR : 温幸文
# TIME : 2021/5/18  下午4:45
import os
import numpy as np
import cv2

"""
这个程序是将解压好的NV21图片文件夹处理出一个新的BGR图片的文件夹
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

                keyword = "BGR"
                if keyword in file_name:
                    single_yuv_size = height * width * 1.5
                else:
                    single_yuv_size = height * width
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

    for src, dirNames, fileNames in os.walk(file_name):
        # 目标文件夹
        if "NV21" in file_name:
            # 创建一个新目录，即把原来的文件夹的名字中的NV12改为BGR
            dest = os.path.join(os.path.dirname(file_name), file_name.replace("NV21", "BGR"))
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

            # 用于判断是否BGR文件
            keyword = 'BGR'

            # if keyword in dirName:
            bgrTurn(subDir2, subDir1, height, width)
            # else:
            #     irTurn(subDir2, subDir1, height, width)

        break

    return None


# NV12转BGR函数
def bgrTurn(subDir2, subDir1, height, width):
    for pathName, dirNames, fileNames in os.walk(subDir1):
        # 对每一个子路径下的NV12文件
        for file in fileNames:
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

                '''多判断版本'''
                # for i in range(frame_size):
                #     k = f1.read(1)
                #     # bytes转int要使用这个方法
                #     # 两个判断k的范围是否合法
                #     if int.from_bytes(k, 'big') < 0:
                #         k = bytes([0])
                #     elif int.from_bytes(k, 'big') > 255:
                #         k = bytes([255])
                #     # 判断k是否空值，很重要，因为ord实参不能为空值
                #     elif len(k) == 0:
                #         continue
                #     yyyy_uv[i] = ord(k)  # 读取 YUV 数据，并转换为 unicode

            img = yyyy_uv.reshape((height * 3 // 2, width)).astype(
                'uint8')  # NV12 的存储格式为：YYYY UV 分布在两个平面（其在内存中为 1 维）
            bgr_img = cv2.cvtColor(img, cv2.COLOR_YUV2BGR_NV21)  # 由于 opencv 不能直接读取 YUV 格式的文件, 所以要转换一下格式

            # 新代码，保证NV12在最后面
            if fileName2.endswith(".NV21"):
                cv2.imwrite(fileName2.replace("NV21", "bmp"), bgr_img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)
            else:
                fileName2 = fileName2.replace(".", "_")
                cv2.imwrite(fileName2 + ".bmp", bgr_img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)
            print('搞定' + fileName2)
    print("搞定一个BGR")

    return None


# NV12转IR函数
def irTurn(subDir2, subDir1, height, width):
    for pathName, dirNames, fileNames in os.walk(subDir1):
        # 对每一个子路径下的NV12文件
        for file in fileNames:
            fileName1 = os.path.join(subDir1, file)
            fileName2 = os.path.join(subDir2, file)
            with open(fileName1, 'rb') as f1:
                frame_size = height * width  # 一帧BGR图像所含的像素个数
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
                    # 关键，判断字符长度是否为0，因为k长度为0时ord会抛出TypeError异常
                    if len(k) == 0:
                        continue
                    yyyy_uv[i] = ord(k)

                '''多判断版本'''
                # for i in range(frame_size):
                #     k = f1.read(1)
                #     # bytes转int要使用这个方法
                #     if int.from_bytes(k, 'big') < 0:
                #         k = bytes([0])
                #     elif int.from_bytes(k, 'big') > 255:
                #         k = bytes([255])
                #     elif len(k) == 0:
                #         continue
                #     yyyy_uv[i] = ord(k)  # 读取 YUV 数据，并转换为 unicode
            img = yyyy_uv.reshape((height, width)).astype('uint8')  # NV12 的存储格式为：YYYY UV 分布在两个平面（其在内存中为 1 维）

            # 新代码，保证NV12在最后面
            if fileName2.endswith(".NV21"):
                cv2.imwrite(fileName2.replace("NV21", "bmp"), img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)
            else:
                fileName2 = fileName2.replace(".", "_")
                cv2.imwrite(fileName2 + ".bmp", img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)
            print('搞定' + fileName2)
    print("搞定一个IR")

    return None


if __name__ == '__main__':
    filePath1 = '/home/wenxingwen/Downloads/0525_light'
    fheight = 800
    fwidth = 1280
    # split_packed_yuv(filePath1, fheight, fwidth)
    # filePath2 = filePath1 + '_NV12'
    # os.rename(filePath1, filePath2)
    yuv2bgr(file_name=filePath1, height=fheight, width=fwidth)
