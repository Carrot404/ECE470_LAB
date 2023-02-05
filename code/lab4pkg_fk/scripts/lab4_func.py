#!/usr/bin/env python

import numpy as np
from scipy.linalg import expm

PI = 3.1415926535

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
	# Fill in the correct values for a1~6 and q1~6, as well as the M matrix
	M = np.eye(4)
	S = np.zeros((6,6))

	# UR3e with tool
	# M = [[0, 0, 1, 293],
	# 	[0, 1, 0, -542],
	# 	[-1, 0, 0, 152],
	# 	[0, 0, 0, 1]]

	# S = [[0, 1,   	 1, 	1, 		0, 		1],
	# 	 [0, 0,   	 0, 	0, 		-1, 	0],
	#  	 [1, 0,   	 0, 	0, 		0, 		0],
	# 	 [0, 0,   	 0, 	0, 		0.152, 	0],
	# 	 [0, 0.152,  0.152, 0.152, 	0, 		0.152],
	# 	 [0, 0, 	 0.244, 0.457, 	-0.131, 0.542]]
	
	# UR3e without tool
	# M = [[0, 0, 1, 223],
	# 	[0, 1, 0, -542],
	# 	[-1, 0, 0, 152],
	# 	[0, 0, 0, 1]]

	# S = [[0, 1,   	 1, 	1, 		0, 		1],
	# 	 [0, 0,   	 0, 	0, 		-1, 	0],
	#  	 [1, 0,   	 0, 	0, 		0, 		0],
	# 	 [0, 0,   	 0, 	0, 		0.152, 	0],
	# 	 [0, 0.152,  0.152, 0.152, 	0, 		0.152],
	# 	 [0, 0, 	 0.244, 0.457, 	-0.131, 0.542]]

	# UR3 without tool
	M = [[0, 0, 1, 0.192],
		[0, 1, 0, -0.540],
		[-1, 0, 0, 0.152],
		[0, 0, 0, 1]]

	S = [[0, 1,   	 1, 	1, 		0, 		1],
		 [0, 0,   	 0, 	0, 		-1, 	0],
	 	 [1, 0,   	 0, 	0, 		0, 		0],
		 [0, 0,   	 0, 	0, 		0.152, 	0],
		 [0, 0.152,  0.152, 0.152, 	0, 		0.152],
		 [0, 0, 	 0.244, 0.457, 	-0.110, 0.540]]
	




	
	# ==============================================================#
	return M, S


"""
Function that calculates encoder numbers for each motor
"""
def lab_fk(theta1, theta2, theta3, theta4, theta5, theta6):

	# =========== Implement joint angle to encoder expressions here ===========
	print("Forward kinematics calculated:\n")

	# =================== Your code starts here ====================#
	theta = np.array([theta1-(0.5*PI), theta2, theta3, theta4+(0.5*PI),theta5,theta6])
	
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



