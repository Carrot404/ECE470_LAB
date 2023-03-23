#!/usr/bin/env python

'''

lab5pkg_ik/lab5_exec.py

@brief: compute inverse kinematics of UR3e robot arm
@author: Songjie Xiao
@date: Monday 2023/3/20

'''

import sys
import time
import rospy
from lab5_func import *
from lab5_ur3e import UR3e

def main():

	# Initialize ROS node
	rospy.init_node('lab5_node')

	# Get input from command line
	if(len(sys.argv) != 5):
		print("\n")
		print("Invalid number of input!\n")
		print("rosrun lab5pkg_ik lab5_exec.py xWgrip yWgrip zWgrip yaw_WgripDegree \n")
	else:
		print("\nxWgrip: " + sys.argv[1] + ", yWgrip: " + sys.argv[2] + \
			  ", zWgrip: " + sys.argv[3] + ", yaw_WgripDegree: " + sys.argv[4] + "\n")

	# Initialize UR3e robot arm
	ur3e = UR3e()
	time.sleep(2)

	# calculate inverse kinematics
	new_dest = lab_invk(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))

	# verify the result through move the arm to the destination
	rospy.loginfo("Sending Goals ...")

	while(  abs(ur3e.current_position[0]-new_dest[0]) > 0.01 or \
			abs(ur3e.current_position[1]-new_dest[1]) > 0.01 or \
			abs(ur3e.current_position[2]-new_dest[2]) > 0.01 or \
			abs(ur3e.current_position[3]-new_dest[3]) > 0.01 or \
			abs(ur3e.current_position[4]-new_dest[4]) > 0.01 or \
			abs(ur3e.current_position[5]-new_dest[5]) > 0.01 ):
		ur3e.move_arm(new_dest)

	rospy.loginfo("Destination is reached!")

if __name__ == '__main__':
	
	try:
		main()
    # When Ctrl+C is executed, it catches the exception
	except rospy.ROSInterruptException:
		pass
