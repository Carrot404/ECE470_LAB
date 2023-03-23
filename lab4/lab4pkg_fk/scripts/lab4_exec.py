#!/usr/bin/env python

'''

lab4pkg_fk/lab4_exec.py

@brief: compute forward kinematics of UR3e robot arm
@author: Songjie Xiao
@date: Monday 2023/3/20

'''

import sys
from lab4_func import *

def main():

	if(len(sys.argv) != 7):
		print("\n")
		print("Command should be entered in degrees with format: \n")
		print("rosrun lab4pkg_fk lab4_exec.py theta1 theta2 theta3 theta4 theta5 theta6 \n")
	else:
		print("\ntheta1: " + sys.argv[1] + ", theta2: " + sys.argv[2] + \
			  ", theta3: " + sys.argv[3] + ", theta4: " + sys.argv[4] + \
			  ", theta5: " + sys.argv[5] + ", theta6: " + sys.argv[6] + "\n")

	T = lab_fk(float(sys.argv[1])*PI/180.0, float(sys.argv[2])*PI/180.0, \
		              float(sys.argv[3])*PI/180.0, float(sys.argv[4])*PI/180.0, \
		              float(sys.argv[5])*PI/180.0, float(sys.argv[6])*PI/180.0,)


if __name__ == '__main__':
	
	try:
		main()
	except:
		print("Error occurs!")
