import rclpy
from rclpy.node import Node
from custom_interfaces.srv import AddTwoInts
import sys

class AddClient(Node):
    def __init__(self):
        super().__init__("add_client")
        self.cli = self.create_client(AddTwoInts, "add_two_ints")

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not availble")

        self.req = AddTwoInts.Request()

    def handle_response(self, a, b):
        self.req.a = a
        self.req.b = b
        future = self.cli.call_async(self.req)

        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main(args=None):
    rclpy.init(args=args)
    node = AddClient()
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    result = node.handle_response(a, b)
    node.get_logger().info(f"result is {result.sum}")
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()