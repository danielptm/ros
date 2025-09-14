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

## to build project (inside src/)
`colcon build`
`colcon build --packages-select my_py_pkg`

## To uninstall
See the above link at the bottom of the page

## To start pubsub
- `colcon build --packages-select my_py_pkg`
- `source ~/.bashrc`
- `ros2 run my_py_pkg robot_news_station`
###In another terminal
ros2 run my_py_pkg smartphone

