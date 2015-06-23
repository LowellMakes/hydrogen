#!/usr/bin/env python

import rospy

from speech import talk
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Saying %s", data.data)
    talk(data.data)
    
def speak():
    rospy.init_node('speak', anonymous=True)
    rospy.Subscriber("speech", String, callback)
    rospy.spin()

if __name__ == '__main__':
    speak()
