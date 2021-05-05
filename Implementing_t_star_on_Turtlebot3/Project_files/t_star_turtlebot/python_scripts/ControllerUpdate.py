#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2, floor
coordinates_prefix=[]
coordinates_suffix=[]


with open('/home/sharvari_ubuntu/catkin_ws/src/Implementing_t_star_on_Turtlebot3/Project_files/t_star_turtlebot/python_scripts/prefix_file_1.txt', 'r') as file:
    for line in file:
        words=[]
        line_array=[]
        words=list(line.split(','))
        line_array.append(int(words[0]))
        line_array.append(int(words[1].rstrip()))
        coordinates_prefix.append(line_array)
 
# print(coordinates_prefix)


with open("/home/sharvari_ubuntu/catkin_ws/src/Implementing_t_star_on_Turtlebot3/Project_files/t_star_turtlebot/python_scripts/suffix_file_1.txt") as file : 
    for line in file:
        words=[]
        line_array=[]
        words=list(line.split(','))
        line_array.append(int(words[0]))
        line_array.append(int(words[1].rstrip()))
        coordinates_suffix.append(line_array)
 
# print(coordinates_suffix)

x = 0.5
y = 0.5 
theta = 0.0
goal = Point()
temp= Point()
isPrefix = True

i_prefix=1
j_suffix=0

def newOdom(msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

rospy.init_node("speed_controller")

sub = rospy.Subscriber("/odom", Odometry, newOdom)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 5)

goal.x = coordinates_prefix[0][0]+0.5
goal.y = coordinates_prefix[0][1]+0.5

speed = Twist()
r = rospy.Rate(20)
rotation_direction=1
def setGoal(index):
    global isPrefix
    if isPrefix == True:
        goal.x = coordinates_prefix[index][0]+0.5
        goal.y = coordinates_prefix[index][1]+0.5
    else:
        goal.x = coordinates_suffix[index][0]+0.5
        goal.y = coordinates_suffix[index][1]+0.5

def GoalReached():
    if abs(goal.x - x) <= 0.25 and abs(goal.y - y) <= 0.25:
        return True
    return False

def actualExec(): 
    global x
    global y
    global pub
    global speed
    global theta
    global goal
    global rotation_direction
    global r
    if not GoalReached():
        print(goal.x, goal.y, x, y, 'in if')
        inc_x = goal.x - x
        inc_y = goal.y - y

        angle_to_goal = atan2(inc_y, inc_x)

        # print(angle_to_goal)
        # print(theta)
        
        #going on negative left direction on x axis

        if temp.x>goal.x and abs(temp.y-goal.y)<=0.2: 
            print("angle_to_goal",angle_to_goal)
            print("theta ",theta)
            if (angle_to_goal - theta)<= -0.25:
                speed.linear.x = 0.0
                speed.angular.z = 0.25
            elif (angle_to_goal - theta)> 0.25:
                speed.linear.x = 0.0
                speed.angular.z = -0.25
            else:
                speed.linear.x = 0.45
                speed.angular.z = 0.0
   
        else:           
            if (angle_to_goal - theta)> 0.25:
                    speed.linear.x = 0.0
                    speed.angular.z = 0.25
                  
            elif (angle_to_goal - theta)<= -0.25:
                    speed.linear.x = 0.0
                    speed.angular.z = -0.25                         
                
            else:
                speed.linear.x = 0.45
                speed.angular.z = 0.0

        pub.publish(speed)
        r.sleep()

        return False

    else:
        print(goal.x, goal.y, x, y, 'in else')
        x = goal.x
        y = goal.y
        temp.x=goal.x
        temp.y=goal.y
        return True


while not rospy.is_shutdown():
    if i_prefix == len(coordinates_prefix) - 1:
        isPrefix = False

    if isPrefix == True:
        response = actualExec()
        if response == True:
            i_prefix+=1
            setGoal(i_prefix)
    else:
        response = actualExec()
        if response == True:
            j_suffix=(j_suffix+1) % len(coordinates_suffix)
            setGoal(j_suffix)
