# README

## How to snapshot using ckcamera

````python 
# define camera object
camera = CKCamera()
# init camera
camera.init()
# display image
camera.display()
```
1. Press 'Esc' to quit window
2. Press 's' to save image, default path: '../img/img_name.bmp'
Make sure to Focus on the image window, then 'Esc' or 's' will work.
After press 's' in image window, then input 'img_name' in the terminal, the snapshot will be store in 'img' folder.
```
# Another option to store image without display
camera.save_image(img_name) # default path:'../img/img_name.bmp'
# Uninit camera when finished snapshot
camera.uninit
````

## Step to test your code

```bash
$ roslaunch ur_robot_driver ur3e_bringup.launch robot_ip:=192.168.1.120
# (new terminal)
$ rosrun ur3e_driver_ece470 ur3e_driver_ece470
# (new terminal)
$ rosrun lab7pkg_pick_place lab7_exec.py
```

## How to connect and run your robot

```bash
$ roslaunch ur_robot_driver ur3e_bringup.launch robot_ip:=192.168.1.120

# create a program with External Control program in Teach Pendant and start program after launching the driver.
# when you see following responses in the terminal, that means Robot is ready!
$ [INFO] [1571124040.693851608]: Robot requested program
$ [INFO] [1571124040.693924407]: Sent program to robot
$ [INFO] [1571124040.772090597]: Robot ready to receive control commands.
```

## How to compile your workspace

```bash
$ cd catkin_(yourID)
$ catkin_make
```

## How to source your workspace (before open a new terminal )

```bash
$ cd catkin_(yourID)
$ source devel/setup.bash
```

## How to make your script executable

```bash
$ cd catkin_(yourID)/src/lab7pkg_pick_place/scripts 
$ chmod +x lab7_exec.py
```

## Steps of run your code

1. roslaunch ur_robot_driver ur3e_bringup.launch robot_ip:=192.168.1.120
2. rosrun ur3e_driver_ece470 ur3e_driver_ece470 (another terminal)
3. rosrun lab7pkg_pick_place lab7_exec.py
