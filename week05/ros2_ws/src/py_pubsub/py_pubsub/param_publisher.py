import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ParamPublisher(Node):
    def __init__(self):
        super().__init__("param_publisher")

        self.declare_parameter("publish_rate", 1.0)
        self.declare_parameter("message_prefix", "Hi")

        rate = self.get_parameter("publish_rate").value
        self.prefix = self.get_parameter("message_prefix").value

        self.publisher = self.create_publisher(String, "chatter", 10)
        self.timer = self.create_timer(1.0 / rate, self.timer_callback)
        self.count = 0

        self.get_logger().info(f"publisher rate: {rate}, prefix: {self.prefix}")

    def timer_callback(self):
        msg = String()
        msg.data = f"{self.prefix} {self.count}"
        self.publisher.publish(msg)
        self.get_logger().info(f"published: {msg.data}")
        self.count += 1

def main(args=None):
        rclpy.init(args=args)
        node = ParamPublisher()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
        main()


