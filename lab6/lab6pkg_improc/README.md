# README

## How to connect and run your robot

1. roslaunch ur_robot_driver ur3e_bringup.launch robot_ip:=192.168.1.120
2. creat a program with the External Control program node in Teach Pendant and start program after launching the driver.
3. When you see those line in the terminal, that means Robot is ready!
   [ INFO] [1571124040.693851608]: Robot requested program
   [ INFO] [1571124040.693924407]: Sent program to robot
   [ INFO] [1571124040.772090597]: Robot ready to receive control commands.

## How to compile your workspace

1. cd catkin_(yourID)
2. catkin_make

## How to source your workspace (before open a new terminal )
> before you open a new terminal, it is important to source your workspace. Then your package could be found.
1. cd catkin_(yourID)
2. source devel/setup.bash

## How to make your script executable

1. cd catkin_(yourID)
2. cd catkin_(yourID)/src/lab6pkg_improc/scripts 
3. chmod +x lab6_img.py

## Steps of run your code

1. roscore 
2. rosrun lab6pkg_improc lab6_img.py (another terminal, make sure it executable)
