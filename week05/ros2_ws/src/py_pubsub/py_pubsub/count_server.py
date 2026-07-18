import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from custom_interfaces.action import CountUntil

class CounterServer(Node):
    def __init__(self):
        super().__init__("count_server")
        self.action_server = ActionServer(
            self,
            CountUntil,
            "count_until",
            self.execute_callback
        )

        self.get_logger().info("Action server is ready.")
    
    def execute_callback(self, goal_handle):
        target = goal_handle.request.target
        self.get_logger().info(f"starting counting from 1---{target}")

        feedback = CountUntil.Feedback()
        current = 0

        for i in range(1, target + 1):
            current = i
            feedback.current = current
            goal_handle.publish_feedback(feedback)
            self.get_logger().info(f"current: {current}")
            time.sleep(0.5)

        goal_handle.succeed()
        result = CountUntil.Result()
        result.final_count = current

        return result
    

def main(args=None):
    rclpy.init(args=args)
    node = CounterServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

        
