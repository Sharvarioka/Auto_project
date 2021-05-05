# Auto_project
This repository contains simulation of T* algorithm on turtlebot3(burger) and husky robots.  Implementing_t_star_on_Turtlebot3 contains the actual simulation whereas rest packages are the pre-requisite folders for turtlebot3 and husky simulation.

**Ros version**- noetic<br />
**Ubuntu version** -20.04

Follow the instructions: <br />
**To install ros noetic:** http://wiki.ros.org/noetic/Installation/Ubuntu <br />
**To install and configure ros environment:** http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment <br />
Now in the src folder of catkin workspace clone this git repo.<br />

 
I have made some minor changes in the cpp program taken from https://github.com/DhavalGujarathi/T-.git. This program gives the coordinates of path using T* algorithm. The modified cpp program is uploaded in this repo with name motion-planner-final.cpp. This program requires files such as:<br />
**query_papereg.dat**- LTL query must be specified here <br />
**cfile_rec.dat**- 2D workspace discription file.

Follow step 8 given in https://github.com/DhavalGujarathi/T-.git to use the tool ltl2tgba. <br />
**motion-planner-final.cpp** provides prefix and suffix cycles in **prefix_file_1.txt and suffix_file_1.txt** respectively. Put these two files in python_scripts folder where driver python codes are present.<br />
**Compile:** g++ -std=c++11 motion-planner-final.cpp -o motion-planner-final <br />
**Execute:** ./motion-planner-final cfile_rec.dat



Use following **commands** on terminal to open world: <br />
cd catkin_ws/ <br />
source devel/setup.bash <br />
catkin_make <br />
roslaunch t_star_turtlebot t_star_launch_turtlebot.launch x_pos:=0.5 y_pos:=0.5 <br />
This will open the world and spawn robot. <br />

In another terminal use following **commands to run the driver code**:  <br />
cd catkin_ws/<br />
source devel/setup.bash <br />
rosrun t_star_turtlebot ControllerUpdate.py <br />

You can also use online version of ros as well! <br />
Use https://www.theconstructsim.com/develop-the-robots-of-the-future/. Create the account and upload the files for ros project. <br />
To run the simulation of husky bot, I used this version where you need upload the git repo files and select empty world map with husky robot. Use the command rosrun t_star_turtlebot ControllerUpdateHusky.py. Here I have used the default world map on ros desktop and hence have provided the coordinates manually but we can use the prefix_file and suffix_file to read coordinates as well.
