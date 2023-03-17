#!/usr/bin/env python

from ur_msgs.msg import IOStates, Digital
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory,JointTrajectoryPoint

"""
# rosmsg show ur_msgs/Digital
------------------------
uint8 pin
bool state

# rosmsg show ur_msgs/IOStates
------------------------
ur_msgs/Digital[] digital_in_states
    uint8 pin
    bool state
ur_msgs/Digital[] digital_out_states
    uint8 pin
    bool state
ur_msgs/Digital[] flag_states
    uint8 pin
    bool state
ur_msgs/Analog[] analog_in_states
    uint8 CURRENT=0
    uint8 VOLTAGE=1
    uint8 pin
    uint8 domain
    float32 state
ur_msgs/Analog[] analog_out_states
    uint8 CURRENT=0
    uint8 VOLTAGE=1
    uint8 pin
    uint8 domain
    float32 state

# rosmsg show sensor_msgs/JointState
------------------------
std_msgs/Header header
    uint32 seq
    time stamp
    string frame_id
string[] name 
float64[] position
float64[] velocity
float64[] effort

# rosmsg show trajectory_msgs/JointTrajectoryPoint
------------------------
float64[] positions
float64[] velocities
float64[] accelerations
float64[] effort
duration time_from_start

# rosmsg show trajectory_msgs/JointTrajectory
------------------------
std_msgs/Header header
    uint32 seq
    time stamp
    string frame_id
string[] joint_names
trajectory_msgs/JointTrajectoryPoint[] points
    float64[] positions
    float64[] velocities
    float64[] accelerations
    float64[] effort
    duration time_from_start

SetIO srv
------------------------
Request:
int8 fun
int8 pin
float32 state
---
Response:
bool success

### FUN
int8 FUN_SET_DIGITAL_OUT = 1
int8 FUN_SET_FLAG = 2
int8 FUN_SET_ANALOG_OUT = 3
int8 FUN_SET_TOOL_VOLTAGE = 4

### valid values for 'state' when setting digital IO or flags
int8 STATE_OFF = 0
int8 STATE_ON = 1

### valid 'state' values when setting tool voltage
int8 STATE_TOOL_VOLTAGE_0V = 0
int8 STATE_TOOL_VOLTAGE_12V = 12
int8 STATE_TOOL_VOLTAGE_24V = 24


"""
