#!/usr/bin/env python
import roslib; roslib.load_manifest('agv_teleop_twist_keyboard')
import rospy

from geometry_msgs.msg import Twist

import sys, select, termios, tty

msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   q    w    e
   a    k    d
   z    s    x

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   Q    W    E
   A    K    D
   Z    S    X

r : up (+z)
f : down (-z)

anything else : stop

y/u : increase/decrease max speeds by 10%
h/j : increase/decrease only linear speed by 10%
n/m : increase/decrease only angular speed by 10%

CTRL-C to quit
"""

moveBindings = {
		'w':(1,0,0,0),
		'e':(1,0,0,-1),
		'a':(0,0,0,1),
		'd':(0,0,0,-1),
		'q':(1,0,0,1),
		's':(-1,0,0,0),
		'x':(-1,0,0,1),
		'z':(-1,0,0,-1),
		'E':(1,-1,0,0),
		'W':(1,0,0,0),
		'A':(0,1,0,0),
		'D':(0,-1,0,0),
		'Q':(1,1,0,0),
		'S':(-1,0,0,0),
		'X':(-1,-1,0,0),
		'Z':(-1,1,0,0),
		'r':(0,0,1,0),
		'f':(0,0,-1,0),
	       }

speedBindings={
		'y':(1.1,1.1),
		'u':(.9,.9),
		'h':(1.1,1),
		'j':(.9,1),
		'n':(1,1.1),
		'm':(1,.9),
	      }

def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key


def vels(speed,turn):
	return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    	settings = termios.tcgetattr(sys.stdin)
	
	pub = rospy.Publisher('agv1/cmd_vel', Twist, queue_size = 1) #cmd_vel
	rospy.init_node('teleop_twist_keyboard_hakan')

	speed = rospy.get_param("~speed", 0.5)
	turn = rospy.get_param("~turn", 1.0)
	x = 0
	y = 0
	z = 0
	th = 0
	status = 0

	try:
		print msg
		print vels(speed,turn)
		while(1):
			key = getKey()
			if key in moveBindings.keys():
				x = moveBindings[key][0]
				y = moveBindings[key][1]
				z = moveBindings[key][2]
				th = moveBindings[key][3]
			elif key in speedBindings.keys():
				speed = speed * speedBindings[key][0]
				turn = turn * speedBindings[key][1]

				print vels(speed,turn)
				if (status == 14):
					print msg
				status = (status + 1) % 15
			else:
				x = 0
				y = 0
				z = 0
				th = 0
				if (key == '\x03'):
					break

			twist = Twist()
			twist.linear.x = x*speed; twist.linear.y = y*speed; twist.linear.z = z*speed;
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = th*turn
			pub.publish(twist)

	except:
		print e

	finally:
		twist = Twist()
		twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
		twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
		pub.publish(twist)

    		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)


