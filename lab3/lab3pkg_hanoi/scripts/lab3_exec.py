#!/usr/bin/env python

'''

lab3pkg_hanoi/lab3_exec.py

@brief: Hanoi implementation in ROS.

@author: Songjie Xiao
@date: Monday 2023/1/16

'''

import sys
import rospy
import numpy as np

from lab3_ur3e import UR3e


def main():
	# Initialize ROS node
	rospy.init_node('lab3_node')

	# Definition of our tower

	# block contact position
	# | Q[0][0] Q[0][1] Q[0][2] |   Contact point of top block
	# | Q[1][0] Q[1][1] Q[1][2] |   Contact point of middle block
	# | Q[2][0] Q[2][1] Q[2][2] |   Contact point of bottom block
	# | Tower1  Tower2  Tower3  |

	# First index - From "top" to "bottom"
	# Second index - From "left" to "right"

	# How the arm will move (Suggestions)
	# 1. Go to the "home" position
	# 2. Drop to the "contact (start) block" position
	# 3. Rise back to the "home" position
	# 4. Drop to the corresponding "contact (end) block" position
	# 5. Rise back to the "home" position


	"""
	TODO: define position of our tower in Q array and home position of the arm
	"""
	############## Your Code Start Here ##############

	home = np.radians([0.00, 0.00, 0.00, 0.00, 0.00, 0.00])

	Q = None

	############### Your Code End Here ###############

	ur3e = UR3e(home, Q)

	# This program will require two user inputs to specify the start location and end location of the block
	# TODO: modify the code below so that program can get two user inputs
	############## Your Code Start Here ##############

	# example code for getting user input is provided below
	input_done = 0
	start = 0
	mid = 1
	des = 2

	while not input_done:
		input_string = input("Enter number of loops <Either 1 2 3 or 0 to quit> ")
		print("You entered " + input_string + "\n")

		if int(input_string) == 1:
			input_done = 1
		elif int(input_string) == 2:
			input_done = 1
		elif int(input_string) == 3:
			input_done = 1
		elif int(input_string) == 0:
			print("Quitting... ")
			sys.exit()
		else:
			print("Please just enter the character 1 2 3 or 0 to quit \n\n")

	############### Your Code End Here ###############

	rospy.loginfo("Sending Goals ...")

	# Main manipulation code defined here
	# move_arm function is used to move the arm to a desired position
	# move_block function is used to move a block from start to end location
	# which includes moving the arm to the start location, gripping the block, moving the arm to the end location, and releasing the block
	# TODO: here to define a series of move_block or move_arm function calls to solve the Hanoi Tower problem
	############## Your Code Start Here ##############

	# ur3e.move_block(start, 0, des,   2)
	# ...

	ur3e.move_arm(home)

	############### Your Code End Here ###############


if __name__ == '__main__':
	try:
		main()
	# When Ctrl+C is executed, it catches the exception
	except rospy.ROSInterruptException:
		pass
