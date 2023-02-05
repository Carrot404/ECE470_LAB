#include <ros/ros.h>
#include <trajectory_msgs/JointTrajectory.h>
#include <trajectory_msgs/JointTrajectoryPoint.h>

int main(int argc, char** argv)
{
	ros::init(argc, argv, "test_move_arm");
	ros::NodeHandle nh;

    ros::Publisher setjoint_pub = nh.advertise<trajectory_msgs::JointTrajectory>("ur3e_driver_ece470/setjoint", 10);

    trajectory_msgs::JointTrajectory trajectory;
    trajectory.joint_names.push_back("shoulder_pan_joint");
    trajectory.joint_names.push_back("shoulder_lift_joint");
    trajectory.joint_names.push_back("elbow_joint");
    trajectory.joint_names.push_back("wrist_1_joint");
    trajectory.joint_names.push_back("wrist_2_joint");
    trajectory.joint_names.push_back("wrist_3_joint");
    
    trajectory_msgs::JointTrajectoryPoint point;
	point.positions.push_back(1.570);
	point.positions.push_back(-1.570);
	point.positions.push_back(0.000);
	point.positions.push_back(-1.570);
	point.positions.push_back(0.000);
	point.positions.push_back(1.570);
	point.time_from_start = ros::Duration(5);
	trajectory.points.push_back(point);

	ros::Rate loop_rate(20);
    while(ros::ok()){
        setjoint_pub.publish(trajectory);
        ros::spinOnce();
		loop_rate.sleep();
    }

	return 0;
}