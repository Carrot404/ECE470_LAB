#!/usr/bin/env python

'''

lab3pkg_hanoi/lab3_ur3e.py

@brief: UR3e class include functions for controlling the UR3e arm and the gripper

@author: Songjie Xiao
@date: Monday 2023/03/17

'''
import time
import rospy

# IMPORT! headers for ROS messages and include useful message types
from lab3_header import *

class UR3e():

    def __init__(self):

        # define variables here
        # store the current position of the arm
        # store the current state of the suction cup
        self.current_io_0 = False

        # Initialize publisher for ur3e_driver_ece470/setjoint with buffer size of 10
        self.pub_setjoint = rospy.Publisher('ur3e_driver_ece470/setjoint', JointTrajectory, queue_size=10)

        # TODO: define a ROS publisher for /ur3e_driver_ece470/setio message with buffer size of 10
        # self.pub_setio =

        # Initialize subscriber to /joint_states, each time /joint_states publishes a new message, the function position_callback is called
        self.sub_position = rospy.Subscriber('/joint_states', JointState, self.position_callback)

        # TODO: define a ROS subscriber for /ur_hardware_interface/io_states message and corresponding callback function
        # self.sub_io =
    
    def init_array(self, home, Q):

        # initialize the home position and Q array
        self.home = home
        self.Q = Q

    def gripper_input_callback(self, msg):
        """
        TODO: define a ROS topic callback function for getting the state of suction cup
        Whenever /ur_hardware_interface/io_states publishes info, this callback function is called.
        """
        ############## Your Code Start Here ##############

        pass

        ############## Your Code End Here ##############


    def position_callback(self, msg):
        """
        TODO: define a ROS topic callback function for getting the current position of the arm
        Whenever /joint_states publishes info, this callback function is called.
        """
        ############## Your Code Start Here ##############

        pass

        ############### Your Code End Here ###############


    def gripper(self, io_0):
        """
        TODO: define a function for ROS Publisher to publish your message to the Topic "ur3e_driver_ece470/setio",
        so that we can control the state of suction cup.
        """
        ############## Your Code Start Here ##############

        pass
    
        ############### Your Code End Here ###############


    def move_arm(self, dest):
        """
        Function for moving the arm to a desired location
        """
        # define msg
        msg = JointTrajectory()
        msg.joint_names = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]
        point = JointTrajectoryPoint()
        point.positions = dest
        point.time_from_start = rospy.Duration(2)
        msg.points.append(point)
        # publish msg
        self.pub_setjoint.publish(msg)
        time.sleep(2.5)


    def move_block(self, start_loc, start_height, end_loc, end_height):
        """
        TODO: define move_block function which is used to move a block from start to end location
        which includes moving the arm to the start location, gripping the block, moving the arm to the end location, and releasing the block

        Hint: Use the Q array to map out your towers by location and height.
        """
        ############## Your Code Start Here ##############

        pass

        ############### Your Code End Here ###############





