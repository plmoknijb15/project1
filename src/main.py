#!/usr/bin/python

import rospy
import keyboard 
from geometry_msgs.msg import Twist

rospy.init_node('my_pub')
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)

msg = Twist()

print("Press Key(W, S, A, D).\n")

rate = rospy.Rate(10)

while not rospy.is_shutdown():
	msg.linear.x = 0
	msg.linear.y = 0
	msg.linear.z = 0
	msg.angular.x = 0
	msg.angular.y = 0
	msg.angular.z = 0

	if keyboard.is_pressed('w'):
		msg.linear.x = 5
	elif keyboard.is_pressed('s'):
		msg.linear.x = -5
	elif keyboard.is_pressed('a'):
		msg.angular.z = 5
	elif keyboard.is_pressed('d'):
		msg.angular.z = -5

	pub.publish(msg)
