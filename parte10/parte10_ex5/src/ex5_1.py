#!/usr/bin/env python3
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


def main():
    # initial setup
    capture = cv2.VideoCapture(0)
    window_name = 'window'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

    while True:

        bridge = CvBridge()

        pub = rospy.Publisher('Image', Image, queue_size=1)
        rospy.init_node('publisher', anonymous=True)

        while not rospy.is_shutdown():
            _, image = capture.read()  # get an image from the camera
        
            
            ros_image = bridge.cv2_to_imgmsg(image, encoding='bgr8')

            image_to_send = ros_image

            cv2.imshow(window_name, image)
            if cv2.waitKey(25) == ord(' '):
              break


            pub.publish(image_to_send)
            rospy.sleep(0.05)
        
        capture.release()
        cv2.destroyAllWindows()
        break
        


if __name__ == '__main__':
    main()