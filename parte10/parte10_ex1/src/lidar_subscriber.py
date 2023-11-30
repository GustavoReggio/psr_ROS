#!/usr/bin/env python3 

import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import LaserScan, PointCloud2
import math

def polar_to_cartesian(ranges, angle_min, angle_increment):
    cartesian_points =[]
    for i, r in enumerate(ranges):
        angle = angle_min + i * angle_increment
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        cartesian_points.append([x,y,0.0])
    return cartesian_points

def lidar_callback(msg):
    # Converter polar para carteziando
    cartesian_points = polar_to_cartesian(msg.ranges, msg.angle_min, msg.angle_increment)

    #Publisher PointCloud2 message
    header = msg.header
    fields = [pc2.PointField('x',0,pc2.PointField.FLOAT32,1),
              pc2.PointField('y',4,pc2.PointField.FLOAT32,1),
              pc2.PointField('z',8,pc2.PointField.FLOAT32,1),]
    pc_data = pc2.create_cloud_xyz32(header,cartesian_points)
    pc_pub.publisher(pc_data)

if __name__ == '__main__':
    rospy.init_node('lidar_subscriber')

    #subscriber
    lidar_topic = '/left_laser/laserscam'
    rospy.Subscriber(lidar_topic,LaserScan,lidar_callback)

    #publisher
    pc_pub = rospy.Publisher('/lidar_pointcloud',PointCloud2,queue_size=10)
    
    #Spin
    rospy.spin()