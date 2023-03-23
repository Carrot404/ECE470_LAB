#!/usr/bin/env python

'''

lab5pkg_ik/lab5_func.py

@brief: functions for computing forward and inverse kinematics of UR3e robot arm
@author: Songjie Xiao
@date: Monday 2023/3/20

'''

import numpy as np
import math
from scipy.linalg import expm

PI = np.pi

"""
Use 'expm' for matrix exponential.
Angles are in radian, distance are in meters.
Add any helper functions as you need.
"""
def Get_MS():
	# =================== Your code starts here ====================#
	# Fill in the correct values for S1~6, as well as the M matrix
	M = np.eye(4)
	S = np.zeros((6,6))




	
	# ==============================================================#
	return M, S


"""
Function that calculates encoder numbers for each motor
"""
def lab_fk(theta1, theta2, theta3, theta4, theta5, theta6):

	# =========== Implement joint angle to encoder expressions here ===========
	print("Forward kinematics calculated:\n")

	# =================== Your code starts here ====================#
	theta = np.array([theta1,theta2,theta3,theta4,theta5,theta6])
	T = np.eye(4)

	M, S = Get_MS()








	# ==============================================================#
	
	print(str(T) + "\n")

	return T


"""
Function that calculates an elbow up Inverse Kinematic solution for the UR3
"""
def lab_invk(xWgrip, yWgrip, zWgrip, yaw_WgripDegree):

    # theta1 to theta6
	thetas = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

	l01 = 0.152
	l02 = 0.120
	l03 = 0.244
	l04 = 0.093
	l05 = 0.213
	l06 = 0.104
	l07 = 0.085
	l08 = 0.092
	l09 = 0

	# xgrip = ?
	# ygrip = ?
	# zgrip = ?

	# xcen = ?
	# ycen = ?
	# zcen = ?

	# theta1
	thetas[0] = 0        # Default value Need to Change

	# theta6
	thetas[5] = PI/2     # Default value Need to Change
 
	# x3end = ?
	# y3end = ?
	# z3end = ?

	thetas[1]= -PI/4     # Default value Need to Change
	thetas[2]= PI/2      # Default value Need to Change
	thetas[3]= (-PI*3)/4 # Default value Need to Change
	thetas[4]=-PI/2      # Default value Need to Change

	print("theta1 to theta6: " + str(thetas) + "\n")

	thetas = np.radians(thetas)
	return thetas
