#!/usr/bin/env python
#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt


class TurtleBot:

    def __init__(self):
        rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)

        self.rate = rospy.Rate(10)


    def cuadrado(self):
            vel_msg = Twist()
            
	    for i in range(10):
                vel_msg.linear.x = 5
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

		vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0
		# Publish
                self.velocity_publisher.publish(vel_msg)
    	        self.rate.sleep()
            for i in range(10):
		vel_msg.linear.x = 0
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

		vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0.001
		# Publish
                self.velocity_publisher.publish(vel_msg)
    	        self.rate.sleep()
	    for i in range(10):
                vel_msg.linear.x = 0
                vel_msg.linear.y = 5
                vel_msg.linear.z = 0

		vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0
		# Publish
                self.velocity_publisher.publish(vel_msg)
    	        self.rate.sleep()
            for i in range(10):
		vel_msg.linear.x = 0
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

		vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0.001
		# Publish
                self.velocity_publisher.publish(vel_msg)
    	        self.rate.sleep()
	    for i in range(10):
                vel_msg.linear.x = -5
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

		vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0
		# Publish
                self.velocity_publisher.publish(vel_msg)
    	        self.rate.sleep()
            for i in range(10):
                vel_msg.linear.x = 0
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

		vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0.001
		# Publish
                self.velocity_publisher.publish(vel_msg)
    	        self.rate.sleep()
	    for i in range(10):
                vel_msg.linear.x = 0
                vel_msg.linear.y = -5
                vel_msg.linear.z = 0

		vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0
		# Publish
                self.velocity_publisher.publish(vel_msg)
    	        self.rate.sleep()
            for i in range(10):
                vel_msg.linear.x = 0
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

		vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0.001
		# Publish
                self.velocity_publisher.publish(vel_msg)
    	        self.rate.sleep()
	    for i in range(5):
                vel_msg.linear.x = 5
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

		vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0
		# Publish
                self.velocity_publisher.publish(vel_msg)
    	        self.rate.sleep()
	    # Detener la tortuga
       	    vel_msg.linear.x = 0
            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)

            rospy.spin()


if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.cuadrado()
    except rospy.ROSInterruptException:
        pass
