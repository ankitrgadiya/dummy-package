import rospy
from time import sleep, clock
from std_msgs.msg import String


class Publisher(object):
    def __init__(self):
        self.__pub = rospy.Publisher("/test/pub1", String, queue_size=10)
        rospy.init_node("pub1")

    def start(self):
        while not rospy.is_shutdown():
            self.__pub.publish("%s" % clock())
            sleep(1)
