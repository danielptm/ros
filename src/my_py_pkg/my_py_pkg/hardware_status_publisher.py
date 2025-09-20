import rclpy
from rclpy.node import Node

class MyCustomNode(Node):

    def __init__(self):
        super().__init__("hardware_status_publisher",10)
        self.timer = self.create_timer(1.0, None)
    
    # def publish hw_status(self):
    #     msg = HardwareSt

    

def main(args=None):
    rclpy.init(args=args)
    node = MyCustomNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()