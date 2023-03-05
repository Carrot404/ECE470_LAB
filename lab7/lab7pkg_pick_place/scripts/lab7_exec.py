#!/usr/bin/env python

import copy
import time
import rospy

from lab7_header import *
from lab7_func import *
from lab7_img import *

import sys
sys.path.append("../utils/script/")
from ckcamera.py import *


# UR3 home location
home = [0*PI/180.0, 0*PI/180.0, 0*PI/180.0, 0*PI/180.0, 0*PI/180.0, 0*PI/180.0]

# UR3 current position, using home position for initialization
current_position = copy.deepcopy(home)

thetas = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

digital_in_0 = 0.0
analog_in_0 = 0.0

suction_on = True
suction_off = False

current_io_0 = False
current_position_set = False

"""
Whenever /ur_hardware_interface/io_states publishes info this callback function is called.
"""
def input_callback(msg):

	global digital_in_0
	pin = 0
	pin_state = msg.digital_in_states[pin].state
	
	if(pin_state):
		digital_in_0 = 1
	else:
		digital_in_0 = 0

"""
Whenever ur3/position publishes info, this callback function is called.
"""
def position_callback(msg):

	global thetas
	global current_position
	global current_position_set

	thetas[0] = msg.position[0]
	thetas[1] = msg.position[1]
	thetas[2] = msg.position[2]
	thetas[3] = msg.position[3]
	thetas[4] = msg.position[4]
	thetas[5] = msg.position[5]

	current_position[0] = thetas[0]
	current_position[1] = thetas[1]
	current_position[2] = thetas[2]
	current_position[3] = thetas[3]
	current_position[4] = thetas[4]
	current_position[5] = thetas[5]

	current_position_set = True

"""
Function to control the suction cup on/off
"""
def gripper(pub_setio, io_0):

	global current_io_0

	error = 0

	current_io_0 = io_0

	msg = Digital()
	msg.pin = 0
	msg.state = io_0
	pub_setio.publish(msg)
	time.sleep(1)

	return error

"""
Move robot arm from one position to another
"""
def move_arm(pub_setjoint, dest):

	msg = JointTrajectory()
	msg.joint_names = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint","wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]
	point = JointTrajectoryPoint()
	point.positions = dest
	point.time_from_start = rospy.Duration(2)
	msg.points.append(point)
	pub_setjoint.publish(msg)
	time.sleep(2.5)

"""
Program run from here
"""
def main():

	# Initialize ROS node
	rospy.init_node('lab7_node')

	# Initialize publisher for ur3e_driver_ece470/setjoint with buffer size of 10
	pub_setio = rospy.Publisher('ur3e_driver_ece470/setio',Digital,queue_size=10)
	pub_setjoint = rospy.Publisher('ur3e_driver_ece470/setjoint',JointTrajectory,queue_size=10)

	# Initialize subscriber to /joint_states & /ur_hardware_interface/io_states and callback function
	# each time data is published
	sub_position = rospy.Subscriber('/joint_states', JointState, position_callback)
	sub_gripper_input = rospy.Subscriber('/ur_hardware_interface/io_states', IOStates, input_callback)

	############## Your Code Start Here ############## 	
	# TODO: modify by yourself

	
#     camera = CKCamera()
#     camera.init()
#     camera.display()
#     # camera.save_image(path)
#     camera.uninit()


	center_values, shape, theta = ImgProcess(img_cali1, img_cali2, [[-361.8, -187.6], [-436.45, -107]], img_snap)

	############### Your Code End Here ###############


	# Check if ROS is ready for operation
	while(rospy.is_shutdown()):
		print("ROS is shutdown!")

	rospy.loginfo("Sending Goals ...")

	############## Your Code Start Here ############## 
	# TODO: finish the task

	






























	
	############### Your Code End Here ###############

	rospy.loginfo("Destination is reached!")


if __name__ == '__main__':
	
	try:
		main()
    # When Ctrl+C is executed, it catches the exception
	except rospy.ROSInterruptException:
		pass
