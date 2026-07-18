from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    param_publisher_node = Node(
        package="py_pubsub",
        executable='param_publisher',
        name="my_publisher",
        parameters=[{
            'publishe_rate': '1.0',
            'message_prefix': 'Hi'
        }]
    )

    subscriber_node = Node(
        package="py_pubsub",
        executable="listener",
        name="my_listener"
    )

    return LaunchDescription(
        [
            param_publisher_node,
            subscriber_node
        ]
    )
