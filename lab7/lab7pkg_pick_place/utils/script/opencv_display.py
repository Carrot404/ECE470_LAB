#!/usr/bin/env python

import cksdk
import cv2
import numpy as np
from ctypes import *



def opencv_display():
    # 初始化相机
    result = cksdk.CameraInit(0)
    if result[0] != 0:
        print("open camera failed")
        return
    hCamera = result[1]
    # 设置相机输出格式
    cksdk.CameraSetIspOutFormat(hCamera, cksdk.CAMERA_MEDIA_TYPE_RGB8)
    # 设置为连续拍照模式
    cksdk.CameraSetTriggerMode(hCamera, 0)

    win_name = 'CKCamera Display'
    cv2.namedWindow(win_name)

    # 开启相机
    cksdk.CameraPlay(hCamera)
    while True:
        result = cksdk.CameraGetImageBufferEx(hCamera, 1000)
        img_data = result[0]
        if img_data is not None:
            img_info = result[1]
            bytes_count = img_info.iWidth * img_info.iHeight * 3
            img_array = cast(img_data, POINTER(c_char*bytes_count))
            np_arr = np.frombuffer(img_array.contents, dtype=np.uint8, count=bytes_count)
            np_arr.shape = (img_info.iHeight, img_info.iWidth, 3)
            dstImg = cv2.resize(np_arr, (800, 600))
            cv2.imshow(win_name, dstImg)

        key = cv2.waitKey(30)
        if key == 27:
            break
        elif key == ord('b'):
            cksdk.CameraSetOnceWB(hCamera)

    #暂停相机
    cksdk.CameraPause(hCamera)
    cv2.destroyAllWindows()
    # 去初始化相机
    cksdk.CameraUnInit(hCamera)

def main():
    result = cksdk.CameraEnumerateDevice()
    if result[0] != 0:
        print("Don't find camera")
        return
    print("Find cameras number: %d" % result[1])
    opencv_display()

if __name__ == '__main__':
    main()
    print("exit!!!")