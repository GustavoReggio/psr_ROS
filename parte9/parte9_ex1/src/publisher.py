#!/usr/bin/env python3

import argparse
import rospy
from std_msgs.msg import String
from colorama import Style, Fore

def main():

    # -------------------------------------------
    # Initialization
    # -------------------------------------------

    
    

    # Setup ROS
    pub = rospy.Publisher('topic_name', String, queue_size=10)

    rospy.init_node('publisher', anonymous=True)

    #rosparamiter
    frquency = rospy.get_param('/publisher/frequency',1.0) # não é mais uma parâmetro relativo é global
    rate = rospy.Rate(frquency)

    #reade highlight_text_param (novo parâmetro criado pelo terminal:rosparam set highlight_text_color GREEN
    print_color = rospy.get_param('highlight_text_color',  'MAGENTA')
    #caso este parâmetro não seja solicitado será a magenta.



    while not rospy.is_shutdown():

        #conteúdo da mensagem
        message_to_send = 'content'

        #Rospy.loginfo tem mais funcionalidade quanto a display em comparação ao print()
        rospy.loginfo(getattr(Fore, print_color) +  message_to_send + Style.RESET_ALL)

        #outos exemplos:
        # Esses fazem prints diretamente para o rosout ! (tópico dos prints) (ver rqt_graph sem Debug.)
        rospy.logwarn('be carful')
        rospy.logerr('something is wrong!')

        pub.publish(message_to_send)                #Cria um publicador
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass