import rospy
from flask import Flask
from std_msgs.msg import String


class Listener(object):
    def __init__(self):
        self.__app = Flask("lis1")
        self.__cache = ""
        rospy.init_node("lis1")
        self.__init_sub()

    def __init_sub(self):
        def callback(data):
            self.__cache = data.data

        self.__lis = rospy.Subscriber("/test/pub1", String, callback=callback)

    def start(self):
        @self.__app.route("/")
        def serve():
            print(self.__cache)
            return self.__cache

        self.__app.run(host="0.0.0.0")
