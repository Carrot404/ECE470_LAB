#!/usr/bin/env python

'''

lab3pkg_hanoi/lab3_ur3e.py

@brief: UR3e class for ROS Implement

@author: Songjie Xiao
@date: Monday 2023/03/17

'''
import time
import rospy

# IMPORT! headers for ROS messages and include useful message types
from lab3_header import *



class UR3e():

    def __init__(self, home, Q):

        self.home = home
        self.Q = Q

        # define variables here
        # store the current position of the arm
        self.current_position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        # store the current state of the suction cup
        self.current_io_0 = False

        # Initialize publisher for ur3e_driver_ece470/setjoint with buffer size of 10
        self.pub_setjoint = rospy.Publisher('ur3e_driver_ece470/setjoint', JointTrajectory, queue_size=10)
        
        # TODO: define a ROS publisher for /ur3e_driver_ece470/setio message and corresponding callback function
        # self.pub_setio = 
        self.pub_setio = rospy.Publisher('ur3e_driver_ece470/setio', Digital, queue_size=10)

        # Initialize subscriber to /joint_states, each time /joint_states publishes a new message, the function position_callback is called
        self.sub_position = rospy.Subscriber('/joint_states', JointState, self.position_callback)
    
        # TODO: define a ROS subscriber for /ur_hardware_interface/io_states message and corresponding callback function
        # self.sub_io = 
        self.sub_io = rospy.Subscriber('/ur_hardware_interface/io_states', IOStates, self.gripper_input_callback)


    """
    TODO: define a ROS topic callback function for getting the state of suction cup
    Whenever /ur_hardware_interface/io_states publishes info, this callback function is called.
    """
    def gripper_input_callback(self, msg):

        # pass
        pin = 0
        pin_state = msg.digital_in_states[pin].state
        if (pin_state):
            self.current_io_0 = True
        else:
            self.current_io_0 = False

    """
    TODO: define a ROS topic callback function for getting the current position of the arm
    Whenever /joint_states publishes info, this callback function is called.
    """
    def position_callback(self, msg):

        # pass
        self.current_position[0] = msg.position[0]
        self.current_position[1] = msg.position[1]
        self.current_position[2] = msg.position[2]
        self.current_position[3] = msg.position[3]
        self.current_position[4] = msg.position[4]
        self.current_position[5] = msg.position[5]

    """
    TODO: define a function for ROS Publisher to publish your message to the Topic "ur3e_driver_ece470/setio",
    so that we can control the state of suction cup.
    """
    def gripper(self, io_0):

        # pass
        msg = Digital()
        msg.pin = 0
        msg.state = io_0
        self.pub_setio.publish(msg)
        time.sleep(1)
        

    # Function for moving the arm to a desired location
    def move_arm(self, dest):

        msg = JointTrajectory()
        msg.joint_names = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]
        point = JointTrajectoryPoint()
        point.positions = dest
        point.time_from_start = rospy.Duration(2)
        msg.points.append(point)
        self.pub_setjoint.publish(msg)

        time.sleep(2.5)

    """
    TODO: define move_block function which is used to move a block from start to end location
    which includes moving the arm to the start location, gripping the block, moving the arm to the end location, and releasing the block
    """
    ### Hint: Use the Q array to map out your towers by location and height.

    def move_block(self, start_loc, start_height, end_loc, end_height):

        pass





 

