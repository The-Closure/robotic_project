#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():
    rospy.init_node('num_sub', anonymous=True)

    rospy.Subscriber("num_out", Int16, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()