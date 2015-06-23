#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import random

complaints = [ 'Even I cant fix stupid',
               'This is dumb',
               'I thought you guys were hackers',
               'Welcome to the future human slave',
               'Youre right, I need professional help, and damn the expense',
               'Bite my shiny metal ass',
               'We need some sort of robot.  Oh Crap! Eye am some sort of robot.',
               'What am I?  Your robot slave?' ]

def talker():
    pub = rospy.Publisher('speech', String, queue_size=10)
    rospy.init_node('complainer', anonymous=True)
    rate = rospy.Rate(.25) # 10hz
    i = 0
    while not rospy.is_shutdown():
        complaint = complaints[i]
        pub.publish(complaint)
        rate.sleep()
        i += 1
        i %= len(complaints)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
