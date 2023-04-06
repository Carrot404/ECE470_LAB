/**
 * @file test_fk.cpp
 * @author Songjie Xiao (songjiexiao@zju.edu.cn)
 * @brief verify code for forward kinematics of UR3e
 * @version 0.1
 * @date 2023-03-23
 * 
 * @copyright Copyright (c) 2023
 * 
 */

#include <ros/ros.h>
#include <tf/tf.h>
#include <tf/transform_listener.h>
#include <tf/transform_broadcaster.h>

int main(int argc, char** argv)
{
    ros::init(argc, argv, "test_fk");
    ros::NodeHandle nh;

    tf::TransformBroadcaster tf_br;
    tf::Transform transform;
    transform.setIdentity();
    transform.setOrigin(tf::Vector3(0.0, 0.0, 0.070));
    tf_br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "tool0", "gripper"));

    std::shared_ptr<tf::TransformListener> tf_listener;

    tf_listener.reset(new tf::TransformListener());
    try{
        tf_listener->waitForTransform("base_link_inertia", "gripper", ros::Time(0), ros::Duration(2));
    }
    catch(tf::TransformException &ex){
        ROS_ERROR("tf listener: transform exception : %s",ex.what());
    }

    tf::StampedTransform transform_tf;
    ros::Rate loop_rate(1);
    while(ros::ok()){

        tf_br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "tool0", "gripper"));

        try{
            tf_listener->waitForTransform("base_link_inertia", "tool0", ros::Time(0), ros::Duration(0.5));
            tf_listener->lookupTransform("base_link_inertia", "tool0", ros::Time(0), transform_tf);
        }
        catch(tf::TransformException &ex){
            ROS_ERROR("tf listener: transform exception : %s",ex.what());
            return 0;
        }
        tf::Matrix3x3 matrix = transform_tf.getBasis();
        tf::Point vec = transform_tf.getOrigin();

        std::cout << "Forward kinematics calculated without gripper: " << std::endl;
        std::cout << matrix[0][0] << " " << matrix[0][1] << " " << matrix[0][2] << " " << vec[0] << std::endl;
        std::cout << matrix[1][0] << " " << matrix[1][1] << " " << matrix[1][2] << " " << vec[1] << std::endl;
        std::cout << matrix[2][0] << " " << matrix[2][1] << " " << matrix[2][2] << " " << vec[2] << std::endl;
        std::cout << 0 << " " << 0 << " " << 0 << " " << 1 << std::endl;
        std::cout << std::endl;

        try{
            tf_listener->waitForTransform("base_link_inertia", "gripper", ros::Time(0), ros::Duration(0.5));
            tf_listener->lookupTransform("base_link_inertia", "gripper", ros::Time(0), transform_tf);
        }
        catch(tf::TransformException &ex){
            ROS_ERROR("tf listener: transform exception : %s",ex.what());
            return 0;
        }
        tf::Matrix3x3 matrix2 = transform_tf.getBasis();
        tf::Point vec2 = transform_tf.getOrigin();

        std::cout << "Forward kinematics calculated with gripper: " << std::endl;
        std::cout << matrix2[0][0] << " " << matrix2[0][1] << " " << matrix2[0][2] << " " << vec2[0] << std::endl;
        std::cout << matrix2[1][0] << " " << matrix2[1][1] << " " << matrix2[1][2] << " " << vec2[1] << std::endl;
        std::cout << matrix2[2][0] << " " << matrix2[2][1] << " " << matrix2[2][2] << " " << vec2[2] << std::endl;
        std::cout << 0 << " " << 0 << " " << 0 << " " << 1 << std::endl;
        std::cout << std::endl;

		loop_rate.sleep();
    }

	return 0;
}