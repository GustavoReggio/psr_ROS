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
    
    ## Sphere ##
    marker_sphere = Marker()

    marker_sphere.header.frame_id = "world"
    marker_sphere.header.stamp = rospy.Time.now()

    marker_sphere.ns = "sphere"
    marker_sphere.id = 0

    marker_sphere.type = Marker.SPHERE
    marker_sphere.action = Marker.ADD

    marker_sphere.pose.position.x = 0
    marker_sphere.pose.position.y = 0
    marker_sphere.pose.position.z = 0
    marker_sphere.pose.orientation.x = 0.0
    marker_sphere.pose.orientation.y = 0.0
    marker_sphere.pose.orientation.z = 0.0
    marker_sphere.pose.orientation.w = 1.0

    marker_sphere.scale.x = 0.3
    marker_sphere.scale.y = 0.3
    marker_sphere.scale.z = 0.3

    marker_sphere.color.a = 1.0
    marker_sphere.color.r = 1.0
    marker_sphere.color.g = 0.0
    marker_sphere.color.b = 0.0

    ## Cube ##

    marker_cube = Marker(ns = "Cube", id = 0 , type = Marker.CUBE, action = Marker.ADD )

    marker_cube.header.frame_id = "world"
    marker_cube.header.stamp = rospy.Time.now()

    marker_cube.pose.position.x = 0
    marker_cube.pose.position.y = 0
    marker_cube.pose.position.z = 0
    marker_cube.pose.orientation.x = 0.0
    marker_cube.pose.orientation.y = 0.0
    marker_cube.pose.orientation.z = 0.0
    marker_cube.pose.orientation.w = 1.0

    marker_cube.scale.x = 1
    marker_cube.scale.y = 1
    marker_cube.scale.z = 1

    marker_cube.color.a = 0.3
    marker_cube.color.r = 0.0
    marker_cube.color.g = 1.0
    marker_cube.color.b = 0.0
    
    rate = rospy.Rate(50)

    diameter = 0.1
    increment = 0.01

    while not rospy.is_shutdown():
        
        marker_sphere.header.stamp = rospy.Time.now()
        diameter += increment
        marker_sphere.scale.x = diameter
        marker_sphere.scale.y = diameter
        marker_sphere.scale.z = diameter

        if diameter > 1:
            increment = -0.01
            print("decreasing")
        elif diameter < 0.1:
            increment = 0.01
            print("increasing")


        publisher.publish(marker_cube)
        publisher.publish(marker_sphere) #Cria um publicador
        print('Publisher a new sphere')
        
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass