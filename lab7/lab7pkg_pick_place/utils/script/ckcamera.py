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
        # set camera parameters
        cksdk.CameraSetIspOutFormat(self.hCamera, cksdk.CAMERA_MEDIA_TYPE_RGB8)
        # set trigger mode
        cksdk.CameraSetTriggerMode(self.hCamera, 0)

    def display(self):
        # open camera
        cksdk.CameraPlay(self.hCamera)

        win_name = 'CKCamera Display'
        cv2.namedWindow(win_name)

        print("CKCamera guide: ")
        print("1. Press 'Esc' to quit window")
        print("2. Press 's' to save image, default path: '../img/img_name.bmp' ")

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
                path = '../img/'
                name = input('input: image name to save <<')
                cksdk.CameraSaveImage(self.hCamera, path + name, img_data, img_info, cksdk.FILE_BMP, 100)
        
        # pause camera
        cksdk.CameraPause(self.hCamera)
        cv2.destroyAllWindows()

    def save_image(self, img_name):
        # open camera
        cksdk.CameraPlay(self.hCamera)

        result = cksdk.CameraGetImageBufferEx(self.hCamera, 1000)
        img_data = result[0]
        if img_data is not None:
            # continue
            img_info = result[1]
            print("frame image width %d, height %d" % (img_info.iWidth, img_info.iHeight))
            # save image
            cksdk.CameraSaveImage(self.hCamera, '../img/'+img_name, img_data, img_info, cksdk.FILE_BMP, 100)
        # pause camera
        cksdk.CameraPause(self.hCamera)

    def uninit(self):
        # uninit camera
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