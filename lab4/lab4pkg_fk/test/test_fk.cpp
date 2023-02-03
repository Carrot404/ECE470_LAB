#include <ros/ros.h>
#include <tf/tf.h>
#include <tf/transform_listener.h>

int main(int argc, char** argv)
{
	ros::init(argc, argv, "test_fk");
	ros::NodeHandle nh;

    std::shared_ptr<tf::TransformListener> tf_listener;

    tf_listener.reset(new tf::TransformListener());
    try{
        tf_listener->waitForTransform("base_link_inertia", "tool0", ros::Time(0), ros::Duration(2));
    }
    catch(tf::TransformException &ex){
        ROS_ERROR("tf listener: transform exception : %s",ex.what());
    }

    tf::StampedTransform transform_tf;
    ros::Rate loop_rate(1);
    while(ros::ok()){

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

        std::cout << "Forward kinematics calculated: " << std::endl;
        std::cout << matrix[0][0] << " " << matrix[0][1] << " " << matrix[0][2] << " " << vec[0] << std::endl;
        std::cout << matrix[1][0] << " " << matrix[1][1] << " " << matrix[1][2] << " " << vec[1] << std::endl;
        std::cout << matrix[2][0] << " " << matrix[2][1] << " " << matrix[2][2] << " " << vec[2] << std::endl;
        std::cout << 0 << " " << 0 << " " << 0 << " " << 1 << std::endl;
        std::cout << std::endl;

		loop_rate.sleep();
    }

	return 0;
}