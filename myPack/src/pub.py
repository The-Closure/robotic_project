#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import rec as rec
import stringify as strignify
import anyio
def voice_cmd_pub():
    pub = rospy.Publisher('voice_cmd', String, queue_size=10)
    rospy.init_node('voice_cmd_pub', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        print('start recording')
        # voice = rec.speech_recognizer()
        voice = []
        print(f'recieve voice value :{voice}')
        print('start resolving')
        commands = strignify.cmd_resolver(voice)
        pub.publish('cmd_voice')
        print(f'resolve commands  :{commands}')
        for cmd in commands:
            cmd = str(cmd).upper()
            # pub.publish(cmd)
            rospy.loginfo('cmd %s published',cmd)
            rate.sleep()
if __name__ == '__main__':
    try:
        voice_cmd_pub()
    except rospy.ROSInterruptException:
        pass
