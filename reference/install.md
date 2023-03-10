# Ubuntu & ROS

## 1. Install Ubuntu

1. create a new virtual machine and choose customized.

![ubuntu_step1](../image/ubuntu_step1.jpg)

2. choose the version depend on your own choice.

![ubuntu_step2](../image/ubuntu_step2.jpg)

3. choose your path of image and install system later.

![ubuntu_step3](../image/ubuntu_step3.jpg)

4. choose Linux and Ubuntu 64.

![ubuntu_step4](../image/ubuntu_step4.jpg)

5. name your machine and place it as you want.

![](../image/ubuntu_step5.jpg)

6. assign processor for your virtual machine.

![](../image/ubuntu_step6.jpg)

7. assign memory for your virtual machine.

![](../image/ubuntu_step7.jpg)

8. add NAT for your network.

![](../image/ubuntu_step8.jpg)

9. choose LSI Logic 

![](../image/ubuntu_step9.jpg)

10. default value is fine.

![](../image/ubuntu_step10.jpg)

11. default value is fine.

![](../image/ubuntu_step11.jpg)

12. assign 30-40 GB for your virtual machine.

![](../image/ubuntu_step12.jpg)

13. default value is fine.

![](../image/ubuntu_step13.jpg)

14. see your configuration and complete it.

![](../image/ubuntu_step14.jpg)

15. start your machine we configured and wait for a while. Then we will see this interface and choose install ubuntu.

![](../image/ubuntu_step15.jpg)

16. choose language (English is preferred.)

![](../image/ubuntu_step16.jpg)

17. the author prefers to Minimal installation. 

![](../image/ubuntu_step17.jpg)

18. Install now!

![](../image/ubuntu_step18.png)

19. shanghai!

![](../image/ubuntu_step19.png)

20. set your user name and password and wait for a while. 

![](../image/ubuntu_step20.jpg)



## 2. Install ROS

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
