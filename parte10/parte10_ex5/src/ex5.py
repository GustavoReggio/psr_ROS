#!/usr/bin/env python3 
import argparse
from functools import partial

import cv2
import numpy as np
from colorama import Fore, Style

import rospy
from cv_bridge import CvBridge, CvBridgeError

def convert_image(image):

    bridge = CvBridge()
    try:
        # Converte a imagem do formato OpenCV para a mensagem sensor_msgs/Image
        ros_image = bridge.cv2_to_imgmsg(image, "bgr8")
        return ros_image
    except CvBridgeError as e:
        print(e)
        return None

def main():

    image_pub = rospy.Publisher("image_topic_2",image)
    rate = rospy.Rate(1)
    rospy.init_node('image_converter', anonymous=True)

    
    # -----------------------------------------------
    # Initialization 
    # -----------------------------------------------
    capture = cv2.VideoCapture(4)
    window_name = 'window'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

        

    # -----------------------------------------------
    # Execution 
    # -----------------------------------------------

    while True:
         
        _, image = capture.read()  # get an image from the camera

        ros_image = convert_image(image)

        image_pub.publish(ros_image)

        

        # -----------------------------------------------
        # Visualization 
        # -----------------------------------------------
        cv2.imshow(window_name, image)
        cv2.waitKey(25)
    # -----------------------------------------------
    # Termination 
    # -----------------------------------------------
    

if __name__ == '__main__':
    main()