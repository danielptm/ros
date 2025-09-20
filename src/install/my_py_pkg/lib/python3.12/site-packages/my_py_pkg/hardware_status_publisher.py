import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus

class HardwarePublisherNode(Node):

    def __init__(self):
        super().__init__("hardware_status_publisher",10)
        self.hw_status_pub = self.create_publisher(HardwareStatus, "hardware_status", 10)
        self.timer = self.create_timer(1.0, self.publish_hw_status)
        self.get_logger().info("hardware status publisher has started...")
    
    def publish_hw_status(self):
        msg = HardwareStatus()
        msg.temperature = 43.7
        msg.are_motors_ready = True
        msg.debug_message = "Nonthing special"
        self.hw_status_pub = self.hw_status_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = HardwarePublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()