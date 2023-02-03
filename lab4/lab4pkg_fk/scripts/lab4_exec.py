#!/usr/bin/env python
import copy
import time
import rospy
import sys
import numpy as np
from lab3_header import *
from lab3_func import *

# 20Hz
SPIN_RATE = 20 

# UR3 home location
home = [0*PI/180.0, 0*PI/180.0, 0*PI/180.0, 0*PI/180.0, 0*PI/180.0, 0*PI/180.0]

# UR3 current position, using home position for initialization
current_position = copy.deepcopy(home)

thetas = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

digital_in_0 = 0
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
	pinstate = True
	pinstate = msg.digital_in_states[pin].state
	
	if(pinstate):
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
def gripper(pub_setio, loop_rate, io_0):

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
	msg.joint_names = ["elbow_joint", "shoulder_lift_joint", "shoulder_pan_joint","wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]
	point = JointTrajectoryPoint()
	point.positions = dest
	point.time_from_start = rospy.Duration(2)
	msg.points.append(point)
	pub_setjoint.publish(msg)

	time.sleep(4)

"""
Program run from here
"""
def main():

	global home

	# Initialize ROS node
	rospy.init_node('lab3node')

	# Initialize publisher for ur3e_driver_ece470/setjoint with buffer size of 10
	pub_setjoint = rospy.Publisher('ur3e_driver_ece470/setjoint',JointTrajectory,queue_size=10)

	# Initialize subscriber to /joint_states & /ur_hardware_interface/io_states and callback function
	# each time data is published
	sub_position = rospy.Subscriber('/joint_states', JointState, position_callback)
	sub_gripper_input = rospy.Subscriber('/ur_hardware_interface/io_states', IOStates, input_callback)


	new_dest = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

	if(len(sys.argv) != 7):
		print("\n")
		print("Command should be entered in degrees with format: \n")
		print("rosrun lab3pkg_py lab3_exec.py theta1 theta2 theta3 theta4 theta5 theta6 \n")
	else:
		print("\ntheta1: " + sys.argv[1] + ", theta2: " + sys.argv[2] + \
			  ", theta3: " + sys.argv[3] + ", theta4: " + sys.argv[4] + \
			  ", theta5: " + sys.argv[5] + ", theta6: " + sys.argv[6] + "\n")

	new_dest = lab_fk(float(sys.argv[1])*PI/180.0, float(sys.argv[2])*PI/180.0, \
		              float(sys.argv[3])*PI/180.0, float(sys.argv[4])*PI/180.0, \
		              float(sys.argv[5])*PI/180.0, float(sys.argv[6])*PI/180.0,)


	# Check if ROS is ready for operation
	while(rospy.is_shutdown()):
		print("ROS is shutdown!")

	rospy.loginfo("Sending Goals ...")

	# Initialize the rate to publish to ur3e_driver_ece470/setjoint
	loop_rate = rospy.Rate(SPIN_RATE)

	while(  abs(thetas[0]-new_dest[0]) > 0.005 or \
			abs(thetas[1]-new_dest[1]) > 0.005 or \
			abs(thetas[2]-new_dest[2]) > 0.005 or \
			abs(thetas[3]-new_dest[3]) > 0.005 or \
			abs(thetas[4]-new_dest[4]) > 0.005 or \
			abs(thetas[5]-new_dest[5]) > 0.005 ):
		move_arm(pub_setjoint, new_dest)

	rospy.loginfo("Destination is reached!")



if __name__ == '__main__':
	
	try:
		main()
    # When Ctrl+C is executed, it catches the exception
	except rospy.ROSInterruptException:
		pass
