#!/usr/bin/env python3


import roslib
roslib.load_manifest('learning_tf')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

def main():

    rospy.init_node('mercury_to_moon')

    listener = tf.TransformListener()
    br = tf.TransformBroadcaster()
    #rospy.wait_for_service('spawn')
    #spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    #spawner(4, 2, 0, 'turtle2')

    #turtle_vel = rospy.Publisher('turtle2/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)

    position = rospy.Publisher('moon', geometry_msgs.msg.Twist,queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('Mecurio', 'Lua', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

    rate = rospy.Rate(10)
    theta = 0
    radius = rospy.get_param("~radius", 2)
    angular_speed = rospy.get_param("~angular_speed", 0.1)
    while not rospy.is_shutdown():

        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        br.sendTransform((x, y, 0),
                         tf.transformations.quaternion_from_euler(0, 0, 2 * theta),
                         rospy.Time.now(),
                         rospy.remap_name("child"), rospy.remap_name("parent"))

        print('Moon to Mercury the transformations')
        rate.sleep()

        theta += angular_speed


        # angular = 4 * math.atan2(trans[1], trans[0])
        # linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        cmd = geometry_msgs.msg.Twist()
        cmd.linear.x = x
        cmd.angular.y = y
        position.publish(cmd)
        # turtle_vel.publish(cmd)
        # rate.sleep()

if __name__ == '__main__':
    main()