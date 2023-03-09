# README

## 1. Task

Calculate the forward kinematics of UR3e using PoE method.

- base frame: robot's base frame 
- target frame: suction cup's frame shown in the manual
- compute transformation from target frame to base frame

### what to do 

1. decide your initial state and compute matrix `M`

   any pose is fine theoretically. what to do is to minus bias of joint angles.

   The manual will recommend one pose for you.

2. according to PoE method, decide and compute all things.

## 3. utils

### 3.1 how to run code

```bash
$ roscore 
# new terminal
$ rosrun lab4pkg_fk lab4_exec.py theta1 theta2 theta3 theta4 theta5 theta6
```

### 3.2 how to verify answer

```bash
$ roslaunch ur_robot_driver ur3e_bringup.launch robot_ip:=192.168.1.120
# (new terminal)
$ rosrun lab4pkg_fk lab4_exec.py theta1 theta2 theta3 theta4 theta5 theta6
# (new terminal) build this code before run it
$ rosrun lab4pkg_fk test_fk
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
$ cd catkin_(yourID)/src/lab7pkg_pick_place/scripts 
$ chmod +x lab7_exec.py
```
