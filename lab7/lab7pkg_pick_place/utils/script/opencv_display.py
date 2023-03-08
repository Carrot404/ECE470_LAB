#!/usr/bin/env python

import cksdk
import cv2
import numpy as np
from ctypes import *



def opencv_display():
    # init camera
    result = cksdk.CameraInit(0)
    if result[0] != 0:
        print("open camera failed")
        return
    hCamera = result[1]
    # set camera parameters
    cksdk.CameraSetIspOutFormat(hCamera, cksdk.CAMERA_MEDIA_TYPE_RGB8)
    # set trigger mode
    cksdk.CameraSetTriggerMode(hCamera, 0)

    win_name = 'CKCamera Display'
    cv2.namedWindow(win_name)

    # open camera
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

    # pause camera
    cksdk.CameraPause(hCamera)
    cv2.destroyAllWindows()
    # uninit camera
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