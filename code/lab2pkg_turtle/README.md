# lab2pkg_turtle

## Objective

1. comprehend the concept of ROS node, topic, message
2. learn how to use them in code by a simple `turtlesim` example
3. see how tf works

## Task 

1. leader turtle is controlled by keyboard inputs and the other turtle is programmed to follow it.
2. complete `turtle_chase.py` by group.

## How to run it

```bash
# init own workspace as manual-reference A
cd catkin_your_workspace/src
# copy package to directory src
catkin_make 
source workspace_path/devel/setup.bash
# make turtle_chase.py executable
chmod +x turtle_chase.py
chmod +x turtle_spawn.py
chmod +x turtle_tf2_broadcaster.py
# run 
roslaunch lab2pkg_turtle turtle_tf2_demo.launch
roslaunch lab2pkg_turtle turtle_chase.launch
```

## example

![](../../image/lab2_example.gif)