#!/usr/bin/env python3
import argparse
import rospy
from std_msgs.msg import String
from functools import partial 
from colorama import Style, Fore


def callback(message_received):
    
    print_color = rospy.get_param('highlight_text_color',  'MAGENTA')
    #print(getattr(Fore,print_color)+ message_received.data + Style.RESET_ALL)
    rospy.loginfo(getattr(Fore,print_color)+ message_received.data + Style.RESET_ALL)
    
def main():

    # -------------------------------------------
    # Initialization
    # -------------------------------------------

    
    # Setup ROS
    rospy.init_node('subscriber', anonymous=True)               # Inicializador do NODE
       
    rospy.Subscriber('topic_name', String, callback)           # Subscrição, necessita ter o mesmo tópco do publicdor

    
    
    # -------------------------------------------
    # Execution
    # -------------------------------------------
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

    # -------------------------------------------
    # Termination
    # -------------------------------------------

if __name__ == '__main__':
    main()