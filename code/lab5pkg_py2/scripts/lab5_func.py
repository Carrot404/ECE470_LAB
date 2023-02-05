#!/usr/bin/env python
import numpy as np
import math
from scipy.linalg import expm
from lab5_header import *

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

	M[0,3] = 393#-70
	M[1,3] = -442
	M[2,3] = 167

	W = [	[0,0,1],
		[1,0,0],
		[1,0,0],
		[1,0,0],
		[0,-1,0],
		[1,0,0]] 
	Q = [	[100,100,167],
		[220,100,167],
		[220,-144,167],
		[127,-357,167],
		[231,-357,167],
		[231,-442,167]] 
	
	for i in range(6):
		Vi = -np.cross(W[i],Q[i])
		S[:,i] = W[i] + list(Vi)
	
	# ==============================================================#
	return M, S


"""
Function that calculates encoder numbers for each motor
"""
def lab_fk(theta1, theta2, theta3, theta4, theta5, theta6):

	# Initialize the return_value 
	return_value = [None, None, None, None, None, None]

	print("Foward kinematics calculated:\n")

	# =================== Your code starts here ====================#
	theta = np.array([theta1,theta2,theta3,theta4,theta5,theta6])
	T = np.eye(4)

	M, S = Get_MS()


	for i in range(6):
		Si = [	[0, 	 -S[2,i], S[1,i], S[3,i]],
			[S[2,i],  0, 	 -S[0,i], S[4,i]],
			[-S[1,i], S[0,i], 0,      S[5,i]],
			[0,       0,      0,      0     ]]
		T = np.dot(T, expm( np.dot(Si, theta[i]) ))

	T = np.dot(T,M)


	# ==============================================================#
	
	print(str(T) + "\n")

	return_value[0] = theta3
	return_value[1] = theta2
	return_value[2] = theta1 + (0.5*PI)
	return_value[3] = theta4 - (0.5*PI)
	return_value[4] = theta5
	return_value[5] = theta6

	return return_value


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

	# thetas = np.radians(thetas)
	return lab_fk(float(thetas[0]), float(thetas[1]), float(thetas[2]), \
		          float(thetas[3]), float(thetas[4]), float(thetas[5]) )
