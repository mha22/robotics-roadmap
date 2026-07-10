import rclpy
from rclpy.node import Node
from custom_interfaces.msg import SensorData

import time

class SensorSubscriber(Node):
    def __init__(self):
        super().__init__('sensor_subscriber')
        self.create_subscription(SensorData, 'sensor_topic', self.listener_callback, 10)
    

    def listener_callback(self, msg):
        self.get_logger().info(
            f'recievied: {msg.sensor_name} | '
            f'T={msg.temperature}°C | H={msg.humidity}% | '
            f'Time={msg.timestamp}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = SensorSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()