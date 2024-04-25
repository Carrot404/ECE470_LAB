"""
This code documention is designed to support a workflow with multiple realsense cameras.
(Single realsense camera operation is also supported.)

Author: Tengyue Wang
Email: tengyuewang7@gmail.com
Date: 2023-05-30
"""

import pyrealsense2 as rs
import numpy as np
import open3d as o3d
import cv2
import multiprocessing as mp
import threading

class RealsenseCamera: 
    """
    Process specified camera device"""
    def __init__(self, device=None, camera_width=640, camera_height=480, camera_fps=30):
        # Create a RealSense pipeline
        self.camera_name = device.get_info(rs.camera_info.name)
        self.camera_serial_number = device.get_info(rs.camera_info.serial_number)
        self.camera_width = camera_width
        self.camera_height = camera_height
        self.camera_fps = camera_fps
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_device(self.camera_serial_number)
        self.config.enable_stream(rs.stream.color, self.camera_width, 
                                  self.camera_height, rs.format.bgr8, 
                                  self.camera_fps)
        self.pipeline.start(self.config)
        # Get stream profile and camera intrinsics
        profile = self.pipeline.get_active_profile()
        print("    name:          ", self.camera_name)
        print("    serial number: ", self.camera_serial_number)
        # Create an align object
        # rs.align allows us to perform alignment of depth frames to others frames
        # The "align_to" is the stream type to which we plan to align depth frames.
        align_to = rs.stream.color
        self.align = rs.align(align_to)
        # Set placeholder for image information
        self.color_frame = None
        self.color_image = None

    def update_frames(self): 
        """Update depth frame and color frame (run every time when requiring new images )"""
        frames = self.pipeline.wait_for_frames()
        # Align the depth frame to color frame
        frames = self.align.process(frames)

        self.color_frame = frames.get_color_frame()
    
    def update_images(self): 
        """Update images after update frames"""
        self.color_image = np.asanyarray(self.color_frame.get_data())
    
    def stop(self):
        """Close camera pipeline when it is terminated"""
        self.pipeline.stop()

    def view_images(self): 
        cv2.namedWindow(self.camera_name, cv2.WINDOW_AUTOSIZE)
        cv2.imshow(self.camera_name, self.color_image)
        cv2.waitKey(1)

def processing(i, camera):
    while True:
        camera.update_frames()       
        camera.update_images()
        camera.view_images()

def main(): 
    # Read all connected realsense device 
    devices = rs.context().devices
    print("%d camera(s) is/are found!" %len(devices))
    camera_handlers = []
    # Start all realsense camera devices
    for i, device in enumerate(devices):
        print("Camera %d: " %i)
        camera_handlers.append(RealsenseCamera(device))    

    try:
        while True:
            for i, camera in enumerate(camera_handlers): 
                camera.update_frames()       
                camera.update_images()
                camera.view_images()
                # camera.view_pc()
    finally:
        for camera in camera_handlers: 
            camera.stop()

if __name__ == '__main__': 
    main()
