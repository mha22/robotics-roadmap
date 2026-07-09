import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinmalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, "chatter", 10)
        self.timer = self.create_timer(1, self.timer_callback)
        self.counter = 0
    
    def timer_callback(self):
        msg = String()
        msg.data = f"Hello ROS2 {self.counter}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")
        self.counter += 1
    
def main(args=None):
    rclpy.init(args=args)
    node = MinmalPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()