# README

## 1. Task

Calculate the inverse kinematics of UR3e arm according to geometry.

Specifically:

1. $\theta_6$  is given by your input, $\theta_5$ is constant.
2. calculate $\theta_1$ first according to the top view.
3. then calculate $\theta_2$ and $\theta_3$ according to the side view.
4. derive $\theta_4 = \theta_3 + \theta_2 - \pi/2$ ; (it may vary with each group)
5. offset of joint1 and joint4 should be considered. (refer to lab4)

## 2. Code

- `lab5_exec.py`: main execution code to compute inverse kinematics and move arm to destination
- `lab5_exec_online.py`: main execution code to compute inverse kinematics for students doing this task online
- `lab5_ur3e.py`: define ur3e's publisher and subscriber (*NO MODIFICTION*)
- `lab5_func.py`: function to compute inverse kinematics (*TODO*)


## 3. utils

### 3.1 how to verify code offline

```bash
$ roslaunch ur_robot_driver ur3e_bringup.launch robot_ip:=192.168.1.120
# (new terminal)
$ rosrun ur3e_driver_ece470 ur3e_driver_ece470
# (new terminal)
$ rosrun lab5pkg_ik lab5_exec.py xWgrip yWgrip zWgrip yaw_WgripDegree
# Then the robot will move to destination, check it on the panel.
```

### 3.2 how to verify code online

```bash
$ python lab5_exec_online.py 0.257 -0.350 0.067 0
# 1. compute inverse kinematics using Given (x,y,z,theta)
# 2. compute forward kinematics using theta derived by inverse kinematics
# 3. compare the position derived by fk with desired (x,y,z)
```

### 3.3 How to connect your robot

```bash
$ roslaunch ur_robot_driver ur3e_bringup.launch robot_ip:=192.168.1.120

# create a program with External Control program in Teach Pendant and start program after launching the driver.
# when you see following responses in the terminal, that means Robot is ready!
$ [INFO] [1571124040.693851608]: Robot requested program
$ [INFO] [1571124040.693924407]: Sent program to robot
$ [INFO] [1571124040.772090597]: Robot ready to receive control commands.
```

### 3.4 How to compile your workspace

```bash
$ cd catkin_(yourID)
$ catkin_make
```

### 3.5 How to source your workspace (before open a new terminal )

```bash
$ cd catkin_(yourID)
$ source devel/setup.bash
```

### 3.6 How to make your script executable

```bash
$ cd catkin_(yourID)/src/lab5pkg_ik/scripts 
$ chmod +x lab5_exec.py
```
