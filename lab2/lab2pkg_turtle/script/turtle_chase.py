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
import math
from turtlesim.srv import Spawn

# TODO: import necessary ROS message types and libraries
# from turtlesim.msg import ()
# from geometry_msgs.msg import ()




########## Define Global Variable Here ##########
# leader turtle pose
goal_pose = Pose()
# follower turtle pose
current_pose = Pose()


############## Your Code Start Here ##############
"""
TODO: define ROS topic callback functions to obtain the pose of leader turtle and follower turtle, and then store it to goal_pose and current_pose.
Whenever topic receive new info, callback function is called.
"""
def leader_pose_callback(msg):

	global goal_pose

	pass


def follower_pose_callback(msg):

	global current_pose

	pass

############### Your Code End Here ###############

def main():

	# Initialize ROS node
	rospy.init_node('turtle_chase')

	# follower_turtle name
	follower_name = 'turtle2'

	# Initialize service client
	spawner_cli = rospy.ServiceProxy('/spawn', Spawn)
	# Calling spawn function to spawn a turtle in the corresponding random position
	random_x = random.randrange(2,10)
	random_y = random.randrange(2,10)
	spawner_cli(random_x, random_y, 0, follower_name)

	publish_rate = rospy.Rate(10)

	############## Your Code Start Here ##############

	# Initialize Publisher/Subscriber
	leader_pose_sub = rospy.Subscriber('/turtle1/pose', Pose, leader_pose_callback)
	# TODO: define subscriber for follower turtle pose
	# follower_pose_sub = rospy.Subscriber('topic_name', topic_type, callback_function)
	# TODO: define publisher for follower turtle velocity
	# follower_vel_pub = rospy.Publisher('topic_name', topic_type, queue_size=10)
	
	vel_msg = Twist()

	while not rospy.is_shutdown():

		"""
		TODO: compute the desired velocity of follower and send it to topic
		"""
		
		while(euclidean_distance(current_pose, goal_pose) >= float(distance_tolerance)):

			# only linear velocity in the x-axis and angular velocity in the z-axis are considered.
			# TODO: compute the desired linear velocity and angular velocity and publish to the topic.
			# choose proper proportional gain for linear velocity and angular velocity
			# recommended value: linear velocity proportional gain = 1, angular velocity proportional gain = 4.0

		


			pass




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