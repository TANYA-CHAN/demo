#!/usr/bin/env python


import rospy
from std_msgs.msg import String

def youtuber():
    video_uploader = rospy.Publisher('youtube_channel', String, queue_size=1)

    rospy.init_node('youtuber')

    rate = rospy.Rate(1) # 1hz

    video_number = 0

    while not rospy.is_shutdown():

	new_video = "hello world, this is my %i video" % video_number

	video_number = video_number+1

        rospy.loginfo(new_video)

        video_uploader.publish(new_video)

        rate.sleep()

if __name__ == '__main__':
    try:
        youtuber()
    except rospy.ROSInterruptException:
        pass
