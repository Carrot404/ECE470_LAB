#!/usr/bin/env python

'''

lab3pkg_hanoi/lab3_exec.py

@brief: Hanoi implementation in ROS.

@author: Songjie Xiao
@date: Monday 2023/1/16

'''

import copy
import time
import rospy
import numpy as np
# headers for ROS messages and include useful message types
from lab3_header import *

# 20Hz
SPIN_RATE = 20 

# UR3 home location
"""
TODO: Define your own Home position here (in radians)
"""
home = np.radians([0.00, 0.00, 0.00, 0.00, 0.00, 0.00])

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

Q = None





############### Your Code End Here ###############
 
 

 
 
############## Your Code Start Here ##############

"""
TODO: define a ROS topic callback function for getting the state of suction cup
Whenever /ur_hardware_interface/io_states publishes info, this callback function is called.
"""
def gripper_input_callback(msg):


	pass



 
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
# def gripper(pub_setio, io_0):
 


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
	pub_setjoint = rospy.Publisher('ur3e_driver_ece470/setjoint', JointTrajectory, queue_size=10)
	
	# TODO: define a ROS publisher for /ur3e_driver_ece470/setio message and corresponding callback function
	# pub_setio = 

	# Initialize subscriber to /joint_states, each time /joint_states publishes a new message, the function position_callback is called
	sub_position = rospy.Subscriber('/joint_states', JointState, position_callback)
 
	# TODO: define a ROS subscriber for /ur_hardware_interface/io_states message and corresponding callback function
	# sub_io = 
 
	############## Your Code Start Here ##############
	# This program will requires two user inputs to specify the start location and end location of the block
	# TODO: modify the code below so that program can get user input
 
	input_done = 0
	loop_count = 0
	start = 0
	mid = 1
	des = 2

	while(not input_done):
		input_string = raw_input("Enter number of loops <Either 1 2 3 or 0 to quit> ")
		print("You entered " + input_string + "\n")

		if(int(input_string) == 1):
			input_done = 1
			loop_count = 1
		elif (int(input_string) == 2):
			input_done = 1
			loop_count = 2
		elif (int(input_string) == 3):
			input_done = 1
			loop_count = 3
		elif (int(input_string) == 0):
			print("Quitting... ")
			# sys.exit()
		else:
			print("Please just enter the character 1 2 3 or 0 to quit \n\n")




			

	############### Your Code End Here ###############
 
	# Check if ROS is ready for operation
	while(rospy.is_shutdown()):
		print("ROS is shutdown!")
 
	rospy.loginfo("Sending Goals ...")
 
	loop_rate = rospy.Rate(SPIN_RATE)
 
	############## Your Code Start Here ##############
	# TODO: modify the code so that UR3 can move tower accordingly from user input
 
 
	move_block(pub_setjoint, pub_setio, start, 0, des,   2)





	
 
 
	############### Your Code End Here ###############
 
 
 
if __name__ == '__main__':
	
	try:
		main()
    # When Ctrl+C is executed, it catches the exception
	except rospy.ROSInterruptException:
		pass
