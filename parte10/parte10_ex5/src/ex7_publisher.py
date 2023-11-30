#!/usr/bin/env python3

import argparse
import rospy
from std_msgs.msg import String

from visualization_msgs.msg import Marker 
from std_msgs.msg import Header

def main():

    # -------------------------------------------
    # Initialization
    # -------------------------------------------

    # Setup ROS

    rospy.init_node('publisher', anonymous=True)
    publisher = rospy.Publisher('drwaings', Marker, queue_size=10)
    
    marker = Marker()

    marker.header.frame_id = "world"
    marker.header.stamp = rospy.Time.now()

    marker.ns = "my_namespace"
    marker.id = 0

    marker.type = Marker.SPHERE
    marker.action = Marker.ADD

    marker.pose.position.x = 0
    marker.pose.position.y = 0
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0

    marker.scale.x = 1
    marker.scale.y = 1
    marker.scale.z = 1

    marker.color.a = 0.3
    marker.color.r = 0.0
    marker.color.g = 1.0
    marker.color.b = 0.0

    
    
    rate = rospy.Rate(50)

    scale = 0.1
    increment = 0.01

    while not rospy.is_shutdown():
        
        marker.header.stamp = rospy.Time.now()
        scale =+ increment
        marker.scale.x = scale
        marker.scale.y = scale
        marker.scale.z = scale

        if scale > 1:
            increment = -0.01
            print("decreasing")
        elif scale < 0.1:
            increment = 0.01
            print("increasing")



        publisher.publish(marker) #Cria um publicador

        print('Publisher a new sphere')

        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass