import sys
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from custom_interfaces.action import CountUntil

class CountClinet(Node):
    def __init__(self):
        super().__init__("count_client")

        self.action_client = ActionClient(
            self,
            CountUntil,
            "count_until"
        )

    def send_goal(self, target):
        goal = CountUntil.Goal()
        goal.target = target

        self.action_client.wait_for_server()
        self.get_logger().info(f"goal send to count until {target}")
        
        self.send_goal_future = self.action_client.send_goal_async(
            goal,
            feedback_callback=self.feedback_callback
        )

        self.send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Target rejected")
            return
        
        self.get_logger().info("goal accepted")
        self.result_future = goal_handle.get_result_async()
        self.result_future.add_done_callback(self.result_callback)

    def feedback_callback(self, feedback_msg):
        current = feedback_msg.feedback.current
        self.get_logger().info(f'feedback : {current}')

    def result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"final result: {result.final_count}")
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = CountClinet()
    target = int(sys.argv[1])
    node.send_goal(target)
    rclpy.spin(node)

if __name__ == "__main__":
    main()