import rclpy
from rclpy.node import Node
from custom_interfaces.msg import SensorData

import time

class SensorPublisher(Node):
    def __init__(self):
        super().__init__('sensor_publisher')
        self.publisher = self.create_publisher(SensorData, 'sensor_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_data)
        self.counter = 0

    def publish_data(self):
        msg = SensorData()
        msg.sensor_name = 'DHT22'
        msg.temperature = 22.5 + (self.counter % 5)
        msg.humidity = 60.0 + (self.counter % 5)
        msg.timestamp = int(time.time())

        self.publisher.publish(msg)
        self.get_logger().info(f"Published: {msg.sensor_name}, T={msg.temperature}°C, H={msg.humidity}%")
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = SensorPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()