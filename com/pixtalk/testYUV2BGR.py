# AUTHOR : 温幸文
# TIME : 2021/5/18  上午11:32
import cv2


def yuv2bgr(img):
    bgr_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    return bgr_img


def main():
    orig_img = cv2.imread('/home/wenxingwen/Documents/wxwtest.yuv.png')

    cv2.imshow("o", orig_img)

    print(orig_img)

    # bgr_img = yuv2bgr(orig_img)
    #
    # cv2.imshow('bgr_img', bgr_img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
