#!/usr/bin/env python

'''

lab2pkg_turtle/turtle_chase.py

@brief: This is an implementation of chase and catch game done using ROS Turtlesim.
		Initially there will be two turtles at the middle. When we teleoperate one turtle, the other turtle will do chase and catch.

@author: Songjie Xiao
@date: Monday 2023/1/16

'''

import rospy
import random
from math import pow, atan2, sqrt
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn

########## Define Global Variable Here ##########
# leader turtle pose
goal_pose = Pose()
# follower turtle pose
current_pose = Pose()
# distance between leader turtle and follower turtle
distance = 0
# distance tolerance
distance_tolerance = 0.5
# proportional parameter 
k_linear = 1.0
k_angular = 4.0

# Euclidean distance between current_pose(follower) and goal_pose(leader).
def euclidean_distance(current_pose, goal_pose):
	global distance
	distance = sqrt(pow((goal_pose.x - current_pose.x), 2) +pow((goal_pose.y - current_pose.y), 2))
	return distance

def steering_angle(current_pose, goal_pose):
	# atan2 may cause some small problem (turtle run around?)
	return atan2(goal_pose.y - current_pose.y, goal_pose.x - current_pose.x)

############## Your Code Start Here ##############
"""
TODO: define ROS topic callback functions to obtain the pose of leader turtle and follower turtle, and then store it to goal_pose and current_pose.
Whenever topic /turtle1/pose or /turtle2/pose receive new info, callback function is called.
"""
def leader_pose_callback(msg):

	global goal_pose

	#TODO:


def follower_pose_callback(msg):

	global current_pose

	#TODO:

############### Your Code End Here ###############

def main():

	# Initialize ROS node
	rospy.init_node('turtle_chase')

	# follower_turtle name
	follower_name = 'turtle2'

	# Initialize Publisher/Subscriber
	leader_pose_sub = rospy.Subscriber('/turtle1/pose', Pose, leader_pose_callback)
	follower_pose_sub = rospy.Subscriber('/turtle2/pose', Pose, follower_pose_callback)
	follower_vel_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

	# Initialize service client
	spawner_cli = rospy.ServiceProxy('/spawn', Spawn)
	# Calling spawn function to spawn a turtle in the corresponding random position
	random_x = random.randrange(2,10)
	random_y = random.randrange(2,10)
	spawner_cli(random_x, random_y, 0, follower_name)

	vel_msg = Twist()
	publish_rate = rospy.Rate(10)

	while(True):

		############## Your Code Start Here ##############
		"""
		TODO: compute the desired velocity of follower and send it to /turtle2/cmd_vel
		"""
		
		while(euclidean_distance(current_pose, goal_pose) >= float(distance_tolerance)):

			# Porportional controller.
			
			#TODO:




		
		############### Your Code End Here ###############
		
		# Stopping turtle after the goal_location is achieved.

		# Linear velocity in the x-axis.
		vel_msg.linear.x = 0
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0

		# Angular velocity in the z-axis.
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 0

		# Publishing vel_msg
		follower_vel_pub.publish(vel_msg)
		# Publish at the desired rate.
		publish_rate.sleep()

if __name__ == '__main__':
	try:
		main()
    # When Ctrl+C is executed, it catches the exception
	except rospy.ROSInterruptException:
		pass