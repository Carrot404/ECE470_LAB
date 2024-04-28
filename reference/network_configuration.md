# Network Configuration

## URCap

>  Before configuring network for UR robots, Import URCaps for external control.
>
>  Please refer to [official driver repo](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver) for more specific info.

1. copy urcap file to your usb driver and import to robot

![](https://s2.loli.net/2023/10/05/7apRiQ4YzlkewB8.png)

## Robot’s Network

1. Set static address, which is robot’s IP.

![](https://s2.loli.net/2023/10/05/UQ2H6rKaRpCnAd8.jpg)

2. set remote host’s IP, it should be at same subnet with robots’s IP. (192.168.1.130 for example, default port 50002)

![](https://s2.loli.net/2023/10/05/SlY4HeREuM3Cw1q.png)

3. load program for remote control, again, same subnet with robot’s IP and host’s IP

![](https://s2.loli.net/2023/10/05/DuQTFG9NKvVhoaE.png)

4. (optional) [RTDE initialization error when EtherNet/IP is enabled](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/issues/204) 

![](https://s2.loli.net/2023/10/05/NhyvzO6VjmlEcP9.png)

## Host’s Network

1. configure wired network as manual. (same subnet with robot’s IP)

![](https://s2.loli.net/2023/10/05/t8vqXVyklp7aGUO.png)

2. try ping robot’s IP if it works

   ```bash
   ping 192.168.1.120
   ```

## Bridged Network

>  if you are using Virtual Machine, you may need a bridged network to bridge robot’s network and host’s network.

1. open windows network adaptor, find corresponding adaptor and change IPv4 config to manual. same subnet with robot and host, different IP address, like `192.168.1.110`.

   `Figure placeholder`

2. Open Virtual Network Editor in VMware, change settings

![](https://s2.loli.net/2023/10/05/xsV9pzfuXEg46hF.png)

3. select default bridged network VMnet0, choose corresponding network adaptor, and save it.

![](https://s2.loli.net/2023/10/05/QrODK7XmGak5ZVJ.png)

4. start your virtual machine with corresponding bridged network.

![network_connection_11](https://s2.loli.net/2023/10/05/dipwlnIYzNZmKPa.png)

## Links: 

1. [UniversalRobots/Universal_Robots_ROS_Driver: Universal Robots ROS driver supporting CB3 and e-Series (github.com)](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver)
