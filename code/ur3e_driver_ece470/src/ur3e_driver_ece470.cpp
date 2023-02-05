#include <ros/ros.h>
#include <actionlib/client/simple_action_client.h>
#include <ur_msgs/SetIO.h>
#include <ur_msgs/Digital.h>
#include <control_msgs/FollowJointTrajectoryAction.h>
#include <control_msgs/FollowJointTrajectoryGoal.h>
#include <control_msgs/FollowJointTrajectoryResult.h>
#include <control_msgs/FollowJointTrajectoryFeedback.h>
#include <trajectory_msgs/JointTrajectory.h>

class URDriverECE
{
public:
	// Constructor/Destructor
	URDriverECE(const ros::NodeHandle& nh);
	~URDriverECE(){}

	// Callback function
	void SetIOCallback(const ur_msgs::Digital& msg);
	void SetJointCallback(const trajectory_msgs::JointTrajectory& msg);
	
private:
	// ROS Parameters
	ros::NodeHandle nh_;
	ros::NodeHandle priv_nh_;

	// ROS Subscriber
	ros::Subscriber setio_sub_;
	ros::Subscriber setjoint_sub_;

	// ROS Service Client
	ros::ServiceClient setio_ser_client_;

	// ROS Action Client
	actionlib::SimpleActionClient<control_msgs::FollowJointTrajectoryAction> fjt_Client_;

	// Action Callback
	void doneCallback(const actionlib::SimpleClientGoalState& state,const control_msgs::FollowJointTrajectoryResultConstPtr& result);
	void activeCallback();
	void feedbackCallback(const control_msgs::FollowJointTrajectoryFeedbackConstPtr& feedback);
};

URDriverECE::URDriverECE(const ros::NodeHandle& nh) : nh_(nh), priv_nh_("~"), fjt_Client_("scaled_pos_joint_traj_controller/follow_joint_trajectory",true)
{
	// ROS Subscriber
	setio_sub_ = nh_.subscribe("ur3e_driver_ece470/setio", 10, &URDriverECE::SetIOCallback, this);
	setjoint_sub_ = nh_.subscribe("ur3e_driver_ece470/setjoint", 10, &URDriverECE::SetJointCallback, this);

	// ROS Service Client
	setio_ser_client_ = nh_.serviceClient<ur_msgs::SetIO>("ur_hardware_interface/set_io");

	// ROS Action Client
	fjt_Client_.waitForServer();
}

void URDriverECE::SetIOCallback(const ur_msgs::Digital& msg)
{
	ur_msgs::SetIO srv;
	srv.request.fun = 1;
	srv.request.pin = msg.pin;
	if(msg.state)
		srv.request.state = 1;
	else
		srv.request.state = 0;
	if(setio_ser_client_.call(srv)){
		ROS_INFO_STREAM("success to set io!");
	}
	else{
		ROS_INFO_STREAM("fail to set io!");
	}
}

void URDriverECE::doneCallback(const actionlib::SimpleClientGoalState& state,const control_msgs::FollowJointTrajectoryResultConstPtr& result)
{
	ROS_INFO_STREAM("Finished in state:" << state.toString().c_str());
}

void URDriverECE::activeCallback()
{
	ROS_INFO_STREAM("Goal just went active.");
}

void URDriverECE::feedbackCallback(const control_msgs::FollowJointTrajectoryFeedbackConstPtr& feedback)
{}

void URDriverECE::SetJointCallback(const trajectory_msgs::JointTrajectory& msg)
{
	control_msgs::FollowJointTrajectoryGoal goal;
	goal.trajectory = msg;
	fjt_Client_.sendGoal(goal,
						boost::bind(&URDriverECE::doneCallback, this, _1, _2),
						boost::bind(&URDriverECE::activeCallback, this),
						boost::bind(&URDriverECE::feedbackCallback, this, _1));
	
}

int main(int argc, char** argv)
{
	ros::init(argc, argv, "ur3e_driver_ece470");
	ros::NodeHandle nh;

	URDriverECE driver(nh);

	ros::Rate loop_rate(20);
	while (ros::ok())
	{
		ros::spinOnce();
		loop_rate.sleep();
	}

	return 0;
}