#!/usr/bin/env python

'''

lab2pkg_turtle/turtle_spawn.py

@brief: This is an implementation of call spawn service to spawn a turtle.

@author: Songjie Xiao
@date: Monday 2023/1/16

'''

import rospy

import turtlesim.srv


def main():
    # Initialize a ROS node with the name turtle_spawn
    rospy.init_node('turtle_spawn')

    # Wait for the service /spawn to be running
    rospy.wait_for_service('/spawn')

    # Create the connection to the service
    spawn_turtle = rospy.ServiceProxy('/spawn', turtlesim.srv.Spawn)

    # Initialize the turtle_name with the default value
    turtle_name = rospy.get_param('turtle', 'turtle2')

    # Call the service to spawn a turtle
    spawn_turtle(4, 2, 0, turtle_name)

    # Print the result given by the service called
    rospy.loginfo("Spawn turtle %s successfully!", turtle_name)


if __name__ == '__main__':
	try:
		main()
	# Use Ctrl+C to stop this script
	except rospy.ROSInterruptException:
		pass
