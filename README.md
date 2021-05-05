# Auto_project
This repository contains simulation of T* algorithm on turtlebot3(burger) and husky robots.  Implementing_t_star_on_Turtlebot3 contains the actual simulation whereas rest packages are the pre-requisite folders to for turtlebot3 and husky simulation.

**Ros version**- noetic
**Ubuntu version** -20.04

Follow the instructions on http://wiki.ros.org/noetic/Installation/Ubuntu to install ros noetic.__
To install and configure ros environment, follow http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment__
Now in the src folder of catkin workspace clone this git repo.__

 
I have made some minor changes in the cpp program taken from https://github.com/DhavalGujarathi/T-.git. This program gives the coordinates of path using T* algorithm. The modified cpp program is uploaded in this repo with name motion-planner-final.cpp. This program requires files such as:
query_papereg.dat- LTL query must be specified here,
cfile_rec.dat- 2D workspace discription file.

Follow the procedure given in https://github.com/DhavalGujarathi/T-.git to get the outout of motion-planner-final.cpp. Output of this program will be two files : prefix_file_1.txt and suffix_file_1.txt. These are the prefix and suffix cycles.

Put these two files in python_scripts folder where driver python codes are present.

Use following commands on terminal to run the code:
cd catkin_ws/
source devel/setup.bash
catkin_make
roslaunch t_star_turtlebot t_star_launch_turtlebot.launch x_pos:=0.5 y_pos:=0.5
This will open the world and spawn robot

In another terminal use following commands to run the driver code:
cd catkin_ws/
source devel/setup.bash
rosrun t_star_turtlebot ControllerUpdate.py

You can also use online version of ros as well!
Use https://www.theconstructsim.com/develop-the-robots-of-the-future/. Create the account and upload the files for ros project.
To run the simulation of husky bot, I used this version where you need upload the git repo files and select empty world map with husky robot. Use the command rosrun t_star_turtlebot ControllerUpdateHusky.py.
