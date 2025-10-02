# Go through this setup guide
https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html

## Setup completed
- laptop ✅
- desktop ✅

## setup command
`source /opt/ros/jazzy/setup.bash`
`source /home/daniel/projects/ros/install/setup.bash`

## how to create a package
`ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy`

## How to create interfaces
1. Create a package for your interfaces like this: `ros2 pkg create my_py_pkg`
2. Remove include and src folders
3. Ensure that CmakeLists.txt has the same code as what it does in my_robot_interfaces package
4. Ensure that package.xml has the same relevant code as it does in the my_robot_interfaces package
5. Create interfaces similar to what is in the msg and srv folders





## to build project (inside src/)
`colcon build`
`colcon build --packages-select my_py_pkg`

## To uninstall
See the above link at the bottom of the page

## To start pubsub
- `colcon build --packages-select my_py_pkg`
- `source ~/.bashrc`
#### In terminal 1
- `ros2 run my_py_pkg robot_news_station`
#### In terminal 2
- `ros2 run my_py_pkg smartphone`


##In publish hardware messages
#### terminal1
`ros2 run my_py_pkg hardware_status_publisher`
#### terminal2
`ros2 topic echo /hardware_status`

## Run a server and client
#### terminal 1
`ros2 run my_py_pkg add_two_ints_server`

#### terminal 2
`ros2 run my_py_pkg add_two_ints_client`

