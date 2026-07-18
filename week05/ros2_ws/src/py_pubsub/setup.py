import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*launch.py'))), 
          
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mha',
    maintainer_email='wma22330@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = py_pubsub.publisher:main',
            'listener = py_pubsub.subscriber:main',
            'sensor_pub = py_pubsub.sensor_publisher:main',
            'sensor_sub = py_pubsub.sensor_subscriber:main',
            'add_server = py_pubsub.add_server:main',
            'add_client = py_pubsub.add_client:main',
            'count_server = py_pubsub.count_server:main',
            'count_client = py_pubsub.c.parount_client:main',
            'param_publisher = py_pubsub.param_publisher:main',
        ],
    },
)
