#!/usr/bin/env python

'''
We get inspirations of Tower of Hanoi algorithm from the website below.
This is also on the lab manual.
Source: https://www.cut-the-knot.org/recurrence/hanoi.shtml
'''

import copy
import time
import rospy
import numpy as np
from lab3_header import *

# 20Hz
SPIN_RATE = 20

# UR3 home location
"""
TODO: Define your own Home position
"""
home = np.radians([-87.42, -103.45, -72.77, -79.02, 89.95, 129.93])

# UR3 current position, using home position for initialization
current_position = copy.deepcopy(home)

thetas = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

digital_in_0 = 0
analog_in_0 = 0

suction_on = True
suction_off = False

current_io_0 = False
current_position_set = False

############## Your Code Start Here ##############

"""
TODO: Definition of position of our tower in Q
"""

Q11 = np.radians([-100.91, -120.18, -86.30, -48.79, 89.95, 116.40])
Q12 = np.radians([-102.12, -123.06, -86.30, -44.70, 89.95, 116.40])
Q13 = np.radians([-103.04, -126.38, -86.31, -40.46, 89.94, 116.40])

Q21 = np.radians([-106.01, -116.69, -72.78, -47.18, 89.96, 129.93])
Q22 = np.radians([-107.46, -120.17, -72.78, -42.24, 89.96, 129.93])
Q23 = np.radians([-108.44, -123.88, -72.78, -37.56, 89.95, 129.93])

Q31 = np.radians([-103.71, -117.83, -60.21, -48.34, 89.96, 142.50])
Q32 = np.radians([-105.19, -121.25, -60.21, -43.44, 89.95, 142.50])
Q33 = np.radians([-106.17, -124.88, -60.21, -38.83, 89.95, 142.50])

Q = [ [Q11, Q12, Q13], \
      [Q21, Q22, Q23], \
      [Q31, Q32, Q33]]

############### Your Code End Here ###############
 
 

 
 
############## Your Code Start Here ##############

"""
TODO: define a ROS topic callback function for getting the state of suction cup
Whenever /ur_hardware_interface/io_states publishes info, this callback function is called.
"""
def gripper_input_callback(msg):
    global digital_in_0
    pin = 0 
    pinstate = True
    pinstate = msg.digital_in_states[pin].state
    if(pinstate):
        digital_in_0 = 1
    else:
        digital_in_0 = 0

############### Your Code End Here ###############
 

"""
Whenever /joint_states publishes info, this callback function is called.
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


############## Your Code Start Here ##############

"""
TODO: define a function for ROS Publisher to publish your message to the Topic "ur3e_driver_ece470/setio",
so that we can control the state of suction cup.
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

############### Your Code End Here ###############
 
def move_arm(pub_setjoint, dest):
	msg = JointTrajectory()
	msg.joint_names = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint","wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]
	point = JointTrajectoryPoint()
	point.positions = dest
	point.time_from_start = rospy.Duration(2)
	msg.points.append(point)
	pub_setjoint.publish(msg)
	time.sleep(2.5)

############## Your Code Start Here ##############
"""
TODO: function to move block from start to end
"""
### Hint: Use the Q array to map out your towers by location and height.

def move_block(pub_setjoint, pub_setio, start_loc, start_height, end_loc, end_height):
	global Q
	global digital_in_0
	error = True

	move_arm(pub_setjoint, home)

	move_arm(pub_setjoint, Q[start_loc][start_height])
	gripper(pub_setio, suction_on)
	time.sleep(1.0)

	if (digital_in_0):
		return 1
	else:
		move_arm(pub_setjoint, home)

		move_arm(pub_setjoint, Q[end_loc][end_height])
		gripper(pub_setio, suction_off)
		time.sleep(1.0)

	return error

############### Your Code End Here ###############
 
 
def main():
 
	global home
	global Q
	global SPIN_RATE

    # Definition of our tower

    # 2D layers (top view)

    # Layer (Above blocks)
    # | Q[0][2][1] Q[1][2][1] Q[2][2][1] |   Above third block
    # | Q[0][1][1] Q[1][1][1] Q[2][1][1] |   Above point of second block
    # | Q[0][0][1] Q[1][0][1] Q[2][0][1] |   Above point of bottom block

    # Layer (Gripping blocks)
    # | Q[0][2][0] Q[1][2][0] Q[2][2][0] |   Contact point of third block
    # | Q[0][1][0] Q[1][1][0] Q[2][1][0] |   Contact point of second block
    # | Q[0][0][0] Q[1][0][0] Q[2][0][0] |   Contact point of bottom block

    # First index - From left to right position A, B, C
    # Second index - From "bottom" to "top" position 1, 2, 3
    # Third index - From gripper contact point to "in the air" point

    # How the arm will move (Suggestions)
    # 1. Go to the "above (start) block" position from its base position
    # 2. Drop to the "contact (start) block" position
    # 3. Rise back to the "above (start) block" position
    # 4. Move to the destination "above (end) block" position
    # 5. Drop to the corresponding "contact (end) block" position
    # 6. Rise back to the "above (end) block" position

	# Initialize ROS node
	rospy.init_node('lab3_node')
 
    # Initialize publisher for ur3e_driver_ece470/setjoint with buffer size of 10

	pub_setjoint = rospy.Publisher('ur3e_driver_ece470/setjoint',JointTrajectory,queue_size=10)
	
	############## Your Code Start Here ##############
	# TODO: define a ROS publisher for /ur3e_driver_ece470/setio message 

	pub_setio = rospy.Publisher('ur3e_driver_ece470/setio',Digital,queue_size=10)
 
	############### Your Code End Here ###############


	# Initialize subscriber to /joint_states and callback fuction
	# each time data is published
	sub_position = rospy.Subscriber('/joint_states', JointState, position_callback)
 
	############## Your Code Start Here ##############
	# TODO: define a ROS subscriber for /ur_hardware_interface/io_states message and corresponding callback function

	sub_gripper_input = rospy.Subscriber('/ur_hardware_interface/io_states', IOStates, gripper_input_callback)

	############### Your Code End Here ###############
 
 
	############## Your Code Start Here ##############
	# TODO: modify the code below so that program can get user input
 
	input_done = 0
	loop_count = 0
	start = 0
	mid = 1
	des = 2

	while(not input_done):
		input_string_start = raw_input("Enter number of loops <Either 1 2 or 3> ")
		start = int(input_string_start) - 1
		print("You entered " + input_string_start + "\n")

		if(int(input_string_start) == 1):
			input_done = 1
			loop_count = 1
		elif (int(input_string_start) == 2):
			input_done = 1
			loop_count = 2
		elif (int(input_string_start) == 3):
			input_done = 1
			loop_count = 3
		else:
			print("Please just enter the character 1 2 or 3 \n\n")

	input_done = 0
	loop_count = 0
 
	while(not input_done):
		input_string_des = raw_input("Enter number of destination stack <Either 1 2 or 3> ")
		des = int(input_string_des) - 1
		print("You entered " + input_string_des + "\n")
 
		if(int(input_string_des) == 1):
			input_done = 1
			loop_count = 1
		elif (int(input_string_des) == 2):
			input_done = 1
			loop_count = 2
		elif (int(input_string_des) == 3):
			input_done = 1
			loop_count = 3
		else:
			print("Please just enter the character 1 2 or 3 \n\n")

	if((start == 0) & (des == 1)):
		mid = 2
	elif ((start == 0) & (des == 2)):
		mid = 1
	elif ((start == 1) & (des == 2)):
		mid = 0
	elif ((start == 1) & (des == 0)):
		mid = 2
	elif ((start == 2) & (des == 1)):
		mid = 0
	elif ((start == 2) & (des == 0)):
		mid = 1
	else:
		start = 0
		mid = 1
		end = 2
		printf("Wrong number \n\n")

	############### Your Code End Here ###############
 
	# Check if ROS is ready for operation
	while(rospy.is_shutdown()):
		print("ROS is shutdown!")
 
	rospy.loginfo("Sending Goals ...")
 
	loop_rate = rospy.Rate(SPIN_RATE)
 
	############## Your Code Start Here ##############
	# TODO: modify the code so that UR3 can move tower accordingly from user input

	move_block(pub_setjoint, pub_setio, start, 0, des,   2)
	move_block(pub_setjoint, pub_setio, start, 1, mid,   2)
	move_block(pub_setjoint, pub_setio, des,   2, mid,   1)
	move_block(pub_setjoint, pub_setio, start, 2, des,   2)
	move_block(pub_setjoint, pub_setio, mid,   1, start, 2)
	move_block(pub_setjoint, pub_setio, mid,   2, des,   1)
	move_block(pub_setjoint, pub_setio, start, 2, des,   0)

	move_arm(pub_setjoint, home)

	############### Your Code End Here ###############
 
 
 
if __name__ == '__main__':
	
	try:
		main()
    # When Ctrl+C is executed, it catches the exception
	except rospy.ROSInterruptException:
		pass
