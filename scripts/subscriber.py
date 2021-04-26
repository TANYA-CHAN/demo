#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def watch_the_video(data):
    rospy.loginfo("I watched Pranshu's video with titled - %s ", data.data)
    
def subscriber():

    rospy.init_node('subscriber', anonymous=True)

    rospy.Subscriber("youtube_channel", String, watch_the_video)

    rospy.spin()

if __name__ == '__main__':
    subscriber()
