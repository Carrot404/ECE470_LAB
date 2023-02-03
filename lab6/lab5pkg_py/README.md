### Step To RUN UR3e

## Terminal 1
1. $ roslaunch ur_robot_driver ur3e_bringup.launch robot_ip:=192.168.1.120
2. creat a program with the External Control program node in Teach Pendant and start program after launching the driver.
3. When you see those line in the terminal, that means Robot is ready!
   [ INFO] [1571124040.693851608]: Robot requested program
   [ INFO] [1571124040.693924407]: Sent program to robot
   [ INFO] [1571124040.772090597]: Robot ready to receive control commands.

## Terminal 2 (for compile your code)

1. $ cd catkin_(yourID)
2. $ catkin_make (compile)

## Terminal 3 (ctrl+shift+n to open a new terminal)

1. $ cd catkin_(yourID)
2. $ source devel/setup.bash
3. $ rosrun ur3e_driver_ece470 ur3e_driver_ece470

## Terminal 4 (for run your code)

1. $ cd catkin_(yourID)
2. $ source devel/setup.bash
3. $ cd catkin_(yourID)/src/lab4pkg_py/scripts 
4. $ chmod +x lab4_exec.py (to make .py file executable, ONCE)
4. $ rosrun lab4pkg_py lab4_exec.py  0.30154 -0.34018 0.14861 0

## Important
**Joint Position** you get from topic or you send to another topic is in an order like that：
[**elbow_joint**, shoulder_lift_joint, **shoulder_pan_joint**, wrist_1_joint, wrist_2_joint, wrist_3_joint]
And Joint Name in your Teach Pedant according to above order **should** be assigned like that:
[**Elbow** Shoulder **Base** Wrist1 Wrist2 Wrist3]
