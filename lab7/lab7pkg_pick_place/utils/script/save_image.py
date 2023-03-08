#!/usr/bin/env python

import cksdk
from ctypes import *


def save_image():
    result = cksdk.CameraInit(0)
    if result[0] != 0:
        print("open camera failed")
        return
    hCamera = result[1]
    # set camera parameters
    cksdk.CameraSetTriggerMode(hCamera, 0)
    # open camera
    cksdk.CameraPlay(hCamera)
    for i in range(10):
        result = cksdk.CameraGetImageBufferEx(hCamera, 1000)
        img_data = result[0]
        if img_data is None:
            continue
        img_info = result[1]
        print("frame image width %d, height %d" % (img_info.iWidth, img_info.iHeight))
        # save image
        cksdk.CameraSaveImage(hCamera, "d:\\test{}".format(i), img_data, img_info, cksdk.FILE_BMP, 100)
    # pause camera
    cksdk.CameraPause(hCamera)

    result = cksdk.CameraUnInit(hCamera)

def main():
    result = cksdk.CameraEnumerateDevice()
    if result[0] != 0:
        print("Don't find camera")
        return
    print("Find cameras number: %d" % result[1])
    save_image()

if __name__ == '__main__':
    main()
