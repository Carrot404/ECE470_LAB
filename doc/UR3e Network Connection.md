# UR3e Installment Instruction For Network Connection

**Author: Carrot (songjiexiao@intl.zju.edu.cn)**

## Prepare the robot

1. For using the ur_robot_driver with a real robot you need to install the **externalcontrol-1.0.4.urcap** using a **USB stick** which can be found inside the resources folder of this driver.
(*Universal_Robots_ROS_Driver-master/ur-robot_driver/resources/externalcontrol-1.0.4.urcap*)

![](https://i.loli.net/2021/09/13/xHOWTSfvqQBsIRu.png)

2. On the welcome screen click on the *hamburger menu* in the top-right corner and select *Settings* to enter the robot's setup. There select *System* and then *URCaps* to enter the URCaps installation screen

3. There, click the little *plus sign* at the bottom to open the file selector. There you should see all urcap files stored inside the robot's programs folder or *a plugged USB drive*. Select and open the *externalcontrol-1.0.4.urcap* file and click *open*. Your URCaps view should now show the External Control in the list of active URCaps and a notification to *restart* the robot. Do that now!

![](https://i.loli.net/2021/09/13/MQWNP5zI4tqZsGK.png)

4. After the reboot you should find the External Control URCaps inside the Installation section. For this select Program Robot on the welcome screen, select the *Installation* tab and select *External Control* from the list.

5. Here you'll have to setup the *IP address* of the external PC which will be running the ROS driver. Note that the robot and the external PC have to be in the **same network**, ideally in a direct connection with each other to minimize network disturbances. The *custom port* should be left *untouched* for now.
(*Here I set host IP **192.168.1.130** which is the virtual machine's IP, custom port **50002**,host name **ur3**. But it doesn't matter as long as they are in the same network segment **1**.*)
![](https://i.loli.net/2021/09/13/lsrbVMEKYh1k2c5.png)

![](https://i.loli.net/2021/09/13/wCXb7cVsIvG2Tfg.png)

6. To use the new URCaps, *create a new program* and insert the *External Control program node* into the program tree。
![](https://i.loli.net/2021/09/13/CM5bLFflR1Jo489.png)

7. If you click on the command tab again, you'll see the settings entered inside the Installation. Check that they are correct, then save the program. Your robot is now ready to be used together with this driver.

## Setting Network

### Robot Network

![](https://i.loli.net/2021/09/13/GVvDH15AedQpmnc.jpg)

1. On the welcome screen click on the *hamburger menu* in the top-right corner and select *Settings* to enter the robot's setup. There select *System* and then *Network* to enter the Network installation screen.

2. Choose **Static Address**, and set *IP address:* **192.168.1.120**, which is served as the *Robot IP* in ROS Program. (You can freely choose the 4th segment as a robot IP, as long as the 3th segment are same, to ensure *robot-host-virtual machine* connected to each other.) Similarly, set *Subnet mask:* **255.255.255.0** and *Default gateway:* **192.168.1.2**

3. Then Apply till *Network is connected!*

### Host Network

![](https://i.loli.net/2021/09/13/q7iX5Mp4AToFBYK.png)

1. Find the Wired Network in control panel. Right click and set the Property.

2. Find *Internet Protocol Version 4 (TCP/IPv4)* and set *Property*.

3. *manually* set the IP address as: *IP Address:* **192.168.1.110** *Subnet mask:* **255.255.255.0** *Default gateway:* **192.168.1.2**. *Confirm!*

### Virtual Machine Network

1. Open *virtual web editor* and *modify setting*.

![](https://i.loli.net/2021/09/13/h57Fmvz8XDAxWT4.png)

2. Choose *VMnet0 bridge mode*, and change *automatic* to *Your wired network*. Then *Apply*!

![](https://i.loli.net/2021/09/13/t5S8ewYyDU2OZfB.png)

3. Open your *VMware*, and edit *virtual machine setting*. Then choose *Network Adapter* and set it as *Bridge Mode*.

![](https://i.loli.net/2021/09/13/LGvqPXIpixSJRwK.png)

4. Enter your *Virtual Machine* and set your wired network. 
**Options-IPv4 Settings-Manual-Add-Address-Save**
*Address:192.168.1.130* as virtual machine's IP *Netmask:* 24 *Gateway:* 192.168.1.2

![](https://i.loli.net/2021/09/13/lwpCrxocRPUqz4k.png)

## Note

**CLOSE THE FIREWALL IN BOTH WINDOWS AND UBUNTU!**

## That's all for setting the UR3e robot!

## Troubleshooting

### Variable 'speed_slider_mask' is currently controlled by another RTDE client

**Installation > Fieldbus > EtherNet/IP > Disable**

![](https://i.loli.net/2021/09/13/q7iX5Mp4AToFBYK.png)