# ECE470_LAB

This repo provides code and manual for ECE470: Introduction to Robotics.





## 3. Ubuntu and ROS (Optional)

if some of you guys want to debug in your own laptop, it is recommended to install ubuntu and ROS. Here show you some basic procedures.

### 3.1 VMware Workstation

1. Download VMware Workstation [here](https://www.vmware.com/cn/products/workstation-pro/workstation-pro-evaluation.html). Other virtual machine software (like VirtualBox) is fine. Recommended version: 16 Pro or 15 Pro.
2. Install it and activate license by yourself.

### 3.2 Ubuntu 20.04

1. Download ubuntu **Desktop** image (.iso) in official website [here](http://www.releases.ubuntu.com/20.04/) or [Tsinghua Mirror](https://mirrors.tuna.tsinghua.edu.cn/ubuntu-releases/20.04.5/).
2. Open VMware and create a new virtual machine.
3. Follow the steps in [ubuntu_install.md](./reference/ubuntu_install.md) in `reference` folder.

### 3.3 ROS 

1. update source

```bash
sudo apt update 
sudo apt upgrade
```

2. install ROS

```bash
# add ROS source
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
# or Tsinghua source
sudo sh -c '. /etc/lsb-release && echo "deb http://mirrors.tuna.tsinghua.edu.cn/ros/ubuntu/ focal main" > /etc/apt/sources.list.d/ros-latest.list'
# add ROS key
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
# install ros
sudo apt update 
sudo apt install ros-noetic-desktop-full
# add path to bashrc
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
# test ros
roscore
# started core service
```

3. install Universal_Robot package

```bash
sudo apt install ros-noetic-ur-msgs
sudo apt install ros-noetic-ur-gazebo
sudo apt install ros-noetic-ur-description
sudo apt install ros-noetic-ur-client-library
```

> Problems may occur when you install all these things. Feel free to ask TAs for help if you can not solve them.
