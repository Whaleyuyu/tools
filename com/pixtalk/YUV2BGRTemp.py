# AUTHOR : 温幸文
# TIME : 2021/5/18  下午4:45
# file1 = open('/home/wenxingwen/Documents/banduan/DB/08_00_23_230YUV_BGR_DATA.yuv_single')
import os
import numpy as np
import cv2


def yuv2bgr(file_name, height, width):
    """
    :param file_name: 待处理 YUV 视频的名字
    :param height: YUV 视频中图像的高
    :param width: YUV 视频中图像的宽
    :param start_frame: 起始帧
    :return: None
    """

    fp = open(file_name, 'rb')
    # fp.seek(0, 2)  # 设置文件指针到文件流的尾部 + 偏移 0
    # fp_end = fp.tell()  # 获取文件尾指针位置

    # frame_size = height * width * 3 // 2  # 一帧BGR图像所含的像素个数
    frame_size = height * width  # 一帧IR图像所含的像素个数
    # num_frame = fp_end // frame_size  # 计算 YUV 文件包含图像数
    # print("This yuv file has {} frame imgs!".format(num_frame))
    # fp.seek(frame_size * start_frame, 0)  # 设置文件指针到文件流的起始位置 + 偏移 frame_size * startframe
    # print("Extract imgs start frame is {}!".format(start_frame + 1))

    # for i in range(num_frame - start_frame):
    yyyy_uv = np.zeros(shape=frame_size, dtype='uint8', order='C')
    for j in range(frame_size):
        yyyy_uv[j] = ord(fp.read(1))  # 读取 YUV 数据，并转换为 unicode

    # img = yyyy_uv.reshape((height * 3 // 2, width)).astype('uint8')  # NV12 的存储格式为：YYYY UV 分布在两个平面（其在内存中为 1 维）
    img = yyyy_uv.reshape((height, width)).astype('uint8')  # NV12 的存储格式为：YYYY UV 分布在两个平面（其在内存中为 1 维）
    # bgr_img = cv2.cvtColor(img, cv2.COLOR_YUV2BGR_NV12)  # 由于 opencv 不能直接读取 YUV 格式的文件, 所以要转换一下格式，支持的转换格式可参考资料 5
    # cv2.imwrite('yuv2bgr/{}.jpg'.format(i + 1), bgr_img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)
    cv2.imshow("windows_name", img)
    cv2.waitKey(0)
    # cv2.imwrite('/home/wenxingwen/Documents/{}.jpg'.format(3), bgr_img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)，此为单次
    # cv2.imwrite('/home/wenxingwen/Documents/{}.jpg'.format(3), img)  # 改变后缀即可实现不同格式图片的保存(jpg/bmp/png...)，此为单次

    # print("Extract frame {}".format(i + 1))

    fp.close()
    print("job done!")
    return None


if __name__ == '__main__':
    yuv2bgr(file_name='/home/wenxingwen/Documents/tttt_NV12', height=640, width=360)
