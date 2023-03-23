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

## 2. Code

- `lab4_exec.py`: main code to execute forward kinematics
- `lab4_func.py`: function to compute forward kinematics using PoE method (*TODO*)
- `test_fk.cpp`: verify code (*NO MODIFICTION*)

## 3. utils

### 3.1 how to run code

```bash
$ python lab4_exec.py theta1 theta2 theta3 theta4 theta5 theta6
```

### 3.2 how to verify answer offline

```bash
$ roslaunch ur_robot_driver ur3e_bringup.launch robot_ip:=192.168.1.120
# (new terminal)
$ python lab4_exec.py theta1 theta2 theta3 theta4 theta5 theta6
# (new terminal) build this code before run it
$ rosrun lab4pkg_fk test_fk
```

### 3.3 How to verify answer online

```bash
$ python lab4_exec.py 1.57 0.00 0.00 -1.57 0.00 0.00
# Forward kinematics calculated with gripper: 
# 3.55283e-06 0.00565484 0.999984 0.29008
# 0.000628308 0.999984 -0.00565484 -0.543749
# -1 0.000628318 -2.05104e-10 0.151796
# 0 0 0 1

$ python lab4_exec.py 1.04 -0.79 -0.48 0.06 -0.23 -0.55
# Forward kinematics calculated with gripper: 
# -0.263007 0.395416 0.880042 0.0955197
# -0.0699828 0.901933 -0.426167 -0.407005
# -0.962252 -0.173673 -0.209543 0.463785
# 0 0 0 1

$ python lab4_exec.py 1.63 -1.25 -0.17 -1.54 -0.54 0.84
# Forward kinematics calculated with gripper: 
# -0.318115 0.343549 0.883616 0.28087
# -0.446133 0.76814 -0.459267 -0.191219
# -0.836522 -0.54031 -0.0910886 0.662953
# 0 0 0 1
```

### 3.4 How to connect your robot

```bash
$ roslaunch ur_robot_driver ur3e_bringup.launch robot_ip:=192.168.1.120

# create a program with External Control program in Teach Pendant and start program after launching the driver.
# when you see following responses in the terminal, that means Robot is ready!
$ [INFO] [1571124040.693851608]: Robot requested program
$ [INFO] [1571124040.693924407]: Sent program to robot
$ [INFO] [1571124040.772090597]: Robot ready to receive control commands.
```

### 3.5 How to compile your workspace

```bash
$ cd catkin_(yourID)
$ catkin_make
```

### 3.6 How to source your workspace (before open a new terminal )

```bash
$ cd catkin_(yourID)
$ source devel/setup.bash
```

### 3.7 How to make your script executable

```bash
$ cd catkin_(yourID)/src/lab4pkg_fk/scripts 
$ chmod +x lab4_exec.py
```
