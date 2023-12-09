#!/usr/bin/env python3

import math
import turtlesim.msg
import tf
import rospy
import roslib

## Este é a primeira versão do circular_frame, onde pode-se ver no rviz e no rostopic echo tf os valores a mudar
def main():

    # -------------------------------
    # Initialization
    # -------------------------------
    rospy.init_node('circular_frame')

    # Publicador de transformações geométricas
    br = tf.TransformBroadcaster()

    # -------------------------------
    # Execution
    # -------------------------------

    rate = rospy.Rate(10)
    theta = 0
    radius = 2
    
    while not rospy.is_shutdown():

        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        
        # Transformações petriódicas | 2D, z=0
        br.sendTransform((x, y, 0),
                         tf.transformations.quaternion_from_euler(0, 0, 0),
                         rospy.Time.now(),
                         "child", "parent")

        print('Published the transformations')
        rate.sleep()

        theta += 0.1


if __name__ == '__main__':
    main()