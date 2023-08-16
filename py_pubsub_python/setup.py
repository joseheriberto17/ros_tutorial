from setuptools import find_packages, setup

package_name = 'py_pubsub_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='joseheri24',
    maintainer_email='jose.heriberto@hotmail.es',
    description='Examples of minimal publisher/subscriber using rclpy',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_pubsub_python.publisher_member_function:main',
            'listener = py_pubsub_python.subscriber_member_function:main',
        ],
    },
)
