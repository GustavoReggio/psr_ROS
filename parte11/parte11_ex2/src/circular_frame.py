#!/usr/bin/env python3

import math
import turtlesim.msg
import tf
import rospy
import roslib

# Para criar uma rede de transformações, usa-se os parâmetros para simplificar esta função.
# Logo é o início para fazer o exemplo do sistema solar
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
    radius = rospy.get_param("~radius", 2)      # Se não for imposto um raio, asume-se =2
    angular_speed = rospy.get_param("~angular_speed", 0.1)

    while not rospy.is_shutdown():

        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        
        # Transformações petriódicas | 2D, z=0
        br.sendTransform((x, y, 0),
                         tf.transformations.quaternion_from_euler(0, 0, 0),
                         rospy.Time.now(),
                         rospy.remap_name("child"), rospy.remap_name("parent"))

        print('Published the transformations')
        rate.sleep()

        theta += angular_speed


if __name__ == '__main__':
    main()