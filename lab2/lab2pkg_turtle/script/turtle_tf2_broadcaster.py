#!/usr/bin/env python

'''

lab2pkg_turtle/turtle_tf2_broadcaster.py

@brief: This is an implementation of broadcast transform between turtle and world..

@author: Songjie Xiao
@date: Monday 2023/1/16

'''

import rospy

# Because of transformations
import tf

import tf2_ros
import geometry_msgs.msg
import turtlesim.msg


# This function is called when a new turtle pose is received
def handle_turtle_pose(msg, turtlename):
    
    # Create a TransformBroadcaster
    br = tf2_ros.TransformBroadcaster()

    # Create a transform from the turtle to the world
    t = geometry_msgs.msg.TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "world"
    t.child_frame_id = turtlename
    t.transform.translation.x = msg.x
    t.transform.translation.y = msg.y
    t.transform.translation.z = 0.0
    q = tf.transformations.quaternion_from_euler(0, 0, msg.theta)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    # Send the transform
    br.sendTransform(t)

def main():
	# Initialize a ROS node with the name turtle_tf2_broadcaster
    rospy.init_node('turtle_tf2_broadcaster')

    # Get turtle name from parameter server
    turtlename = rospy.get_param('~turtle')

    # Subscribe to turtle1/pose and call handle_turtle_pose on each message
    rospy.Subscriber('/%s/pose' % turtlename, turtlesim.msg.Pose, handle_turtle_pose, turtlename)
    
    rospy.spin()

if __name__ == '__main__':
	try:
		main()
	# Use Ctrl+C to stop this script
	except rospy.ROSInterruptException:
		pass