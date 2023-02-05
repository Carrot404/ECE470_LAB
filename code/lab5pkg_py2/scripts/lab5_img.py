import math
import cv2
import numpy as np
import rospkg
import os

class Camera():
    def __init__(self,save_imgpath):
        self.save_imgpath = save_imgpath

    def read_image(self):
        img = cv2.imread(self.save_imgpath)
        return img

    def image_process(self, img):
        if img is None:
            return
        draw_img = img.copy()

        ############## Your Code Start Here ##############
        # TODO: image process including filtering, edge detection, 
        # contour detection and make sure every contour available
        # Tips: cv2.contourArea(contour) as threshold

        blur = cv2.bilateralFilter(img, 29, 70, 200)
        blur = cv2.medianBlur(blur, 9)

        img_gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        xgrd = cv2.Sobel(img_gray, cv2.CV_16SC1, 1, 0)
        ygrd = cv2.Sobel(img_gray, cv2.CV_16SC1, 0, 1)
        img = cv2.Canny(xgrd, ygrd, 50, 150) 

        cv2.imshow('1', img)
        cv2.waitKey()
        cv2.destroyAllWindows()

        img, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        len_con = len(contours)
        for i in range(len_con):
            area = cv2.contourArea(contours[len_con-1-i])
            if area < 500 :
                contours.pop(len_con-1-i)

        ############### Your Code End Here ###############


        # template preprocess 
        rospack = rospkg.RosPack()
        lab5_path = rospack.get_path('lab5pkg_py')
        img_path = os.path.join(lab5_path, 'scripts', 'example.jpg')
        _img = cv2.imread(img_path)
        _draw_img = _img.copy()

        # Bilateral Filter smoothes images while preserving edges,
        # by means of a nonlinear combination of nearby image values.
        # cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)
        # d - Diameter of each pixel neighborhood that is used during filtering.
        _blur = cv2.bilateralFilter(_img, 19, 130, 30)
        _blur = cv2.medianBlur(_blur, 9)

        _img_gray = cv2.cvtColor(_blur, cv2.COLOR_BGR2GRAY)
        _xgrd = cv2.Sobel(_img_gray, cv2.CV_16SC1, 1, 0)
        _ygrd = cv2.Sobel(_img_gray, cv2.CV_16SC1, 0, 1)
        _img = cv2.Canny(_xgrd, _ygrd, 30, 220)

        # Here we obtain the edge, then show using code below
        # cv2.imshow('1', img)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        
        _w, _h = _img.shape
        _img_1 = _img[:, :_w]
        _img_2 = _img[:, _w:]

        # cv2.findContours to find contour
        # variable _contours_1 stores all contours, each of which is composed of
        # a series of pixel point 
        # For example: len(contours) contours[0] 
        # rectangle
        _img_1, _contours_1, hierarchy = cv2.findContours(_img_1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # circle
        _img_2, _contours_2, hierarchy = cv2.findContours(_img_2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
    
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

                M = cv2.moments(contours[i * 2])
                center_x = int(M["m10"] / M["m00"])
                center_y = int(M["m01"] / M["m00"])
                cv2.circle(draw_img, (int(center_x), int(center_y)), 7, [0,0,255], -1)
                center_value.append([center_x, center_y])

                ret_1 = cv2.matchShapes(contours[i * 2], _contours_1[0], 1, 0.0)
                ret_2 = cv2.matchShapes(contours[i * 2], _contours_2[0], 1, 0.0)
                ret = np.array([ret_1, ret_2])
                shape.append(np.argmin(ret))
                
                ############### Your Code End Here ###############

            else:
                # compute the center of a contour
                N = cv2.moments(contours[i * 2])
                _center_x = int(N["m10"] / N["m00"])
                _center_y = int(N["m01"] / N["m00"])
                # draw a circle on the center point
                cv2.circle(draw_img, (int(_center_x), int(_center_y)), 7, [0,255,0], -1)

                ############## Your Code Start Here ##############
                # TODO: compute the angle of your object
                # Tips: compute the distance between center point of object and every point of contour,
                # choose the furthest point, then you can compute the angle

                # cv2.line(draw_img, (_center_x, _center_y), (x, y), (128, 0, 0), 2)

                center = np.array([center_x, center_y])
                index = np.argmax(np.sum(np.square(contours[i * 2][:, 0, :] - center), axis=1))
                x, y = contours[i * 2][:, 0, :][index][0], contours[i * 2][:, 0, :][index][1]
                cv2.line(draw_img, (_center_x, _center_y), (x, y), (128, 0, 0), 2)
                _x = contours[i * 2][:, 0, :][index][0] - _center_x
                _y = contours[i * 2][:, 0, :][index][1] - _center_y
                
                theta.append(np.arctan2(_y,_x))
            
                ############### Your Code End Here ###############

        cv2.imshow('2', draw_img)
        cv2.waitKey()
        cv2.destroyAllWindows()
        return center_value, shape, theta

def coordinate_transform(center_cam, center_robot, center_value):
    ############## Your Code Start Here ##############
    # TODO: transform camera coordinate to robot coordinate
    # Tip: center_value: [[Object1],[Object2],...]

    x1 = center_cam[0][0]
    y1 = center_cam[0][1]
    x2 = center_cam[1][0]
    y2 = center_cam[1][1]
    x1_ = center_robot[0][0]
    y1_ = center_robot[0][1]
    x2_ = center_robot[1][0]
    y2_ = center_robot[1][1]

    x_ratio = (x2_ - x1_) / (y2 - y1)
    y_ratio = (y2_ - y1_) / (x2 - x1)

    center_values = []

    for i, j in center_value:
        x_ = x1_ + x_ratio * (j - y1)
        y_ = y1_ + y_ratio * (i - x1)
        center_values.append([x_, y_])

    return center_values

    ############### Your Code End Here ###############


def ImgProcess(_test1, _test2, center_robot, _img):
    # Step1 Camera Calibration and transform camera coordinate to robot coordinate
    # save two snapshots, get the coordinate of center in two coordinate system (camera and robot)

    test1 = Camera(_test1)
    image1 = test1.read_image()
    center_cam1, shape1, theta1 = test1.image_process(image1)

    test2 = Camera(_test2)
    image2 = test2.read_image()
    center_cam2, shape2, theta2 = test2.image_process(image2)

    center_cam = []
    center_cam.append(center_cam1[0])
    center_cam.append(center_cam2[0])
    # center_robot = [[-361.8, -187.6], [-436.45, -107]]

    # Step2 compute the coordinate of your object in robot coordinate system
    camera = Camera(_img)
    img = camera.read_image()
    center_value, shape, theta = camera.image_process(img)

    center_values = coordinate_transform(center_cam, center_robot, center_value)

    return center_values, shape, theta
    
# if __name__ == '__main__':
# 	ImgProcess('_test1.bmp', '_test2.bmp', [[-361.8, -187.6], [-436.45, -107]], '_lab5.bmp')
    
    






