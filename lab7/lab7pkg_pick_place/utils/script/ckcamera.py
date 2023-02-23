#!/usr/bin/env python

import cksdk
import cv2
import numpy as np
from ctypes import *


class CKCamera():

    def __init__(self):
        pass

    def init(self):
        result = cksdk.CameraEnumerateDevice()
        if result[0] != 0:
            print("Error: Could not find camera!")
            return False
        print("INFO: Find cameras number: %d" % result[1])

        result = cksdk.CameraInit(0)
        if result[0] != 0:
            print("Error: failed to open camera!")
            return False
        
        self.hCamera = result[1]
        # 设置相机输出格式
        cksdk.CameraSetIspOutFormat(self.hCamera, cksdk.CAMERA_MEDIA_TYPE_RGB8)
        # 设置为连续拍照模式
        cksdk.CameraSetTriggerMode(self.hCamera, 0)

    def display(self):
        # 开启相机
        cksdk.CameraPlay(self.hCamera)

        win_name = 'CKCamera Display'
        cv2.namedWindow(win_name)

        print("CKCamera guide: ")
        print("1. Press 'Esc' to quit window")
        print("2. Press 's' to save image, default path: '../img/img_snap.bmp' ")

        while True:
            result = cksdk.CameraGetImageBufferEx(self.hCamera, 1000)
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
            elif key == ord('s'):
                path = input('input: where to save snapshot <<')
                cksdk.CameraSaveImage(self.hCamera, path, img_data, img_info, cksdk.FILE_BMP, 100)
        
        # 暂停相机
        cksdk.CameraPause(self.hCamera)
        cv2.destroyAllWindows()

        # 去初始化相机
        # cksdk.CameraUnInit(hCamera)

    def save_image(self, img_path):
        # 开启相机
        cksdk.CameraPlay(self.hCamera)

        result = cksdk.CameraGetImageBufferEx(self.hCamera, 1000)
        img_data = result[0]
        if img_data is not None:
            # continue
            img_info = result[1]
            print("frame image width %d, height %d" % (img_info.iWidth, img_info.iHeight))
            # 保存图片
            # Test
            cksdk.CameraSaveImage(self.hCamera, img_path, img_data, img_info, cksdk.FILE_BMP, 100)
        # 暂停相机
        cksdk.CameraPause(self.hCamera)

    def uninit(self):
        # 去初始化相机
        cksdk.CameraUnInit(self.hCamera)

# def main():
#     camera = CKCamera()
#     camera.init()
#     camera.display()
#     # camera.save_image(path)
#     camera.uninit()

# if __name__ == '__main__':
#     try:
#         main()
#     except Exception as ex:
#         print(str(ex))