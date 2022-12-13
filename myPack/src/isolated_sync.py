from std_msgs.msg import String
import rec as rec
import stringify as str
import asyncio as asyncio
# import aioros
async def voice_cmd_pub():

    while True:
        print('start recording')
        voice = await rec.speech_recognizer()
        print(f'recieve voice value :{voice}')
        print('start resolving')
        commands = str.cmd_resolver(voice)
        print(f'resolve commands  :{commands}')
        for cmd in commands:
            pub.publish(cmd)
            rospy.loginfo('cmd %s published',cmd)
            rate.sleep()
if __name__ == '__main__':
    try:
        voice_cmd_pub()
    except Exception:
        pass