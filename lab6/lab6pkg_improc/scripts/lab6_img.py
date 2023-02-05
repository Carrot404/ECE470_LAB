#!/usr/bin/env python

#########################################################################
#
#  Lab 6-Image Processing
#  Main task is to pick and place all the blocks to your destination.
#  Camera is used to detect blocks. With image processing methods, 
#  robot is able to know the position, shape and orientation of the blocks.
#  Since block's position is based on image coordinate, what we should do
#  is to transform it into robot coordinate. (refer to manual)
#
#########################################################################

import rospy
import rospkg
import os
import math
import cv2
import numpy as np

class Camera():
    def __init__(self, img_path):

        rospack = rospkg.RosPack()
        lab6_path = rospack.get_path('lab6pkg_improc')

        self.img_path = os.path.join(lab6_path, 'img', img_path)
        self.img = cv2.imread(self.img_path)
        if self.img is None:
            print('Image is None, Please check image path!')

        self.temp_path = os.path.join(lab6_path, 'img', 'template.jpg')
        self.img_temp = cv2.imread(self.temp_path)
        if self.img_temp is None:
            print('Template Image is None, Please check image path!')
        
    def template_process(self):

        if self.img_temp is None:
            print('Template Image is None, Please check image path!')
            return

        temp_copy = self.img_temp.copy()

        # Bilateral Filter smooths images while preserving edges,
        # by means of a nonlinear combination of nearby image values.
        # cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)
        # d - Diameter of each pixel neighborhood that is used during filtering.

        temp_blur = cv2.bilateralFilter(temp_copy, 19, 130, 30)
        temp_blur = cv2.medianBlur(temp_blur, 9)

        temp_gray = cv2.cvtColor(temp_blur, cv2.COLOR_BGR2GRAY)
        x_grid = cv2.Sobel(temp_gray, cv2.CV_16SC1, 1, 0)
        y_grid = cv2.Sobel(temp_gray, cv2.CV_16SC1, 0, 1)
        temp_canny = cv2.Canny(x_grid, y_grid, 30, 220)

        # show image using the code below
        # cv2.imshow('canny image', temp_canny)
        # cv2.waitKey()
        # cv2.destroyAllWindows()

        weight, height = temp_canny.shape
        temp_rect = temp_canny[:, :weight]
        temp_elip = temp_canny[:, weight:]

        # cv2.findContours to find contour
        # variable contours_1 stores all contours, each of which is composed of
        # a series of pixel point 
        # For example: len(contours) contours[0] 
        # rectangle
        self.contours_rect, hierarchy = cv2.findContours(temp_rect, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # elipse
        self.contours_elip, hierarchy = cv2.findContours(temp_elip, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        


    def image_process(self):

        self.template_process()

        if self.img is None:
            print('Image is None, Please check image path!')
            return
        
        img_copy = self.img.copy()

        ############## Your Code Start Here ##############
        # TODO: image process including filtering, edge detection, 
        # contour detection and make sure every contour available
        # Tips: cv2.contourArea(contour) as threshold

        pass


















        ############### Your Code End Here ###############

    
        ############## Your Code Start Here ##############
        # TODO: compute the center of contour and the angle of your object,
        # as well as match shapes of your object
        center_value = []
        shape = [] # 0 represents rectangle while 1 represents circle or ellipse
        theta = []
        for i in range(len(contours) // 2):
            if i % 2 == 0:
                ############## Your Code Start Here ##############
                # TODO: compute the center of contour as well as match shapes of your object
                # Tips: ret = cv2.matchShapes(contour1, contour2, 1, 0.0) 

                # cv2.circle(draw_img, (int(center_x), int(center_y)), 7, [0,0,255], -1)

                pass











                ############### Your Code End Here ###############

            else:
                # compute the center of a contour
                N = cv2.moments(contours[i * 2])
                _center_x = int(N["m10"] / N["m00"])
                _center_y = int(N["m01"] / N["m00"])
                # draw a circle on the center point
                cv2.circle(self.img, (int(_center_x), int(_center_y)), 7, [0,255,0], -1)

                ############## Your Code Start Here ##############
                # TODO: compute the angle of your object
                # Tips: compute the distance between center point of object and every point of contour,
                # choose the furthest point, then you can compute the angle

                # cv2.line(draw_img, (_center_x, _center_y), (x, y), (128, 0, 0), 2)

                pass
















            
                ############### Your Code End Here ###############

        cv2.imshow('image with center and orientation', self.img)
        cv2.waitKey()
        cv2.destroyAllWindows()
        return center_value, shape, theta

def coordinate_transform(center_cam, center_robot, center_snap):

    ############## Your Code Start Here ##############
    # TODO: transform camera coordinate to robot coordinate
    # Tip: center_value: [[Object1],[Object2],...]

    pass










    
    ############### Your Code End Here ###############


def ImgProcess(img_cali1, img_cali2, center_robot, img_snap):

    # Step1 Camera Calibration and transform camera coordinate to robot coordinate
    # save two snapshots, get the coordinate of center in two coordinate system (camera and robot)

    cam_cali1 = Camera(img_cali1)
    center_cali1, shape_cali1, theta_cali1 = cam_cali1.image_process()

    cam_cali2 = Camera(img_cali2)
    center_cali2, shape_cali2, theta_cali2 = cam_cali2.image_process()

    center_cam = []
    center_cam.append(center_cali1[0])
    center_cam.append(center_cali2[0])
    # center_robot = [[-361.8, -187.6], [-436.45, -107]]

    # Step2 compute the coordinate of your object in robot coordinate system
    cam_snap = Camera(img_snap)
    center_snap, shape, theta = cam_snap.image_process()

    center_snap_robot = coordinate_transform(center_cam, center_robot, center_snap)

    return center_snap_robot, shape, theta

def main():

    # Initialize ROS node
	rospy.init_node('lab6_node')

	ImgProcess('img_cali_1.bmp', 'img_cali_2.bmp', [[-361.8, -187.6], [-436.45, -107]], 'img_snap.bmp')
    
if __name__ == '__main__':
	
	try:
		main()
    # When Ctrl+C is executed, it catches the exception
	except rospy.ROSInterruptException:
		pass