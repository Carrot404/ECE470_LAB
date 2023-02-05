#!/usr/bin/env python

import numpy as np
import math
from scipy.linalg import expm

PI = np.pi

"""
You may write some helper functions as you need
Use 'expm' for matrix exponential
Angles are in radian, distance are in meters.
"""

def get_screw(S):
	screw = [[0, -S[2], S[1], S[3]],
			[S[2], 0, -S[0], S[4]],
			[-S[1], S[0], 0, S[5]],
			[0, 0, 0, 0]]
	return screw

def get_column(S,d):
	S_inv = [S[0][d], S[1][d], S[2][d], S[3][d], S[4][d], S[5][d]]
	return S_inv

def Get_MS():
	# =================== Your code starts here ====================#
	# Fill in the correct values for S1~6, as well as the M matrix
	M = np.eye(4)
	S = np.zeros((6,6))

	# UR3e with tool
	M = [[0, 0, 1, 293],
		[0, 1, 0, -542],
		[-1, 0, 0, 152],
		[0, 0, 0, 1]]

	S = [[0, 1,   	 1, 	1, 		0, 		1],
		 [0, 0,   	 0, 	0, 		-1, 	0],
	 	 [1, 0,   	 0, 	0, 		0, 		0],
		 [0, 0,   	 0, 	0, 		0.152, 	0],
		 [0, 0.152,  0.152, 0.152, 	0, 		0.152],
		 [0, 0, 	 0.244, 0.457, 	-0.131, 0.542]]

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

	T = M

	for i in range(6):
		S_inv = get_column(S, 5-i)
		S_screw = get_screw(S_inv)
		exp = expm(np.array(S_screw) * theta[5-i])
		T= np.dot(exp, T)

	# ==============================================================#
	
	print(str(T) + "\n")

	return T

"""
Function that calculates an elbow up Inverse Kinematic solution for the UR3
"""
def lab_invk(xWgrip, yWgrip, zWgrip, yaw_WgripDegree):

	# TODO: verify ik answer (gripper??)
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
	l10 = 0.0   # thickness of aluminum plate is around 0.01

	xgrip = -yWgrip 
	ygrip = xWgrip 
	zgrip = zWgrip 

	xcen = xgrip - l09*np.sin(yaw_WgripDegree)
	ycen = ygrip - l09*np.cos(yaw_WgripDegree)
	zcen = zgrip

	# theta1
	alpha = np.arcsin( (l02-l04+l06) / (xcen**2+ycen**2)**0.5 )
	thetas[0] = math.atan2(ycen,xcen) - alpha        # Default value Need to Change

	# theta6
	thetas[5] = yaw_WgripDegree    # Default value Need to Change
 
	x3end = -l07*np.cos(thetas[0])+(-l06-0.027)*(-np.sin(thetas[0]))+xcen
	y3end = -l07*np.sin(thetas[0])+(-l06-0.027)*(np.cos(thetas[0]))+ycen
	z3end = l08+l10+zcen

	xy3 = (x3end**2 + y3end**2)**0.5
	z3 = z3end - l01
	beta = math.atan2(z3,xy3)

	l35 = (xy3**2 + z3**2)**0.5
	a35 = np.arccos( (l03**2+l05**2-l35**2) / (2*l03*l05) )
	a3 = np.arccos( (l35**2+l05**2-l03**2) / (2*l35*l05) )
	a5 = np.arccos( (l03**2+l35**2-l05**2) / (2*l03*l35) )

	thetas[1]= -a5 - beta     # Default value Need to Change
	thetas[2]= PI - a35      # Default value Need to Change
	thetas[3]= -a3 + beta  # Default value Need to Change
	thetas[4]= -PI/2      # Default value Need to Change

	print("theta1 to theta6: " + str(thetas) + "\n")

	# TODO: theta offset?

	thetas = np.radians(thetas)

	return thetas
