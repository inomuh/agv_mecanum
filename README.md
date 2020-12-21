# AGV Mecanum (AGV-MOTA) (ROS Noetic)
This repository includes the AGV Mecanum ROS Noetic packages.

![Image of AGV Mecanum](https://github.com/inomuh/agv_mecanum/blob/main/images/agv_mecanum_gazebo.png)

- agv_mecanum_description: It is the sub-package containing urdf and mesh files of the AGV.
- agv_mecanum_simulation: It is a sub-package containing the package and launch files required for the simulation of the AGV.
- agv_mecanum_teleop: It is a sub-package containing the agv_mecanum_teleop_keyboard script file (Python).

# For other AGV Mecanum ROS Packages:

https://github.com/inomuh/agvsim_mecanumwheel_ros

Launch Commands:
---------------
### Warning !!!
Before using launch commands, you must unzip ~/agv_mecanum/agv_mecanum_description/meshes/MOTA-v0.3.tar.xz file..

-------------------------------------------------------------------------------------------------------------
Gazebo Launching:

    $ roslaunch agv_mecanum_simulation agvmecanum_gazebo_emptyworld.launch

Gazebo (Depo Map) Launching:

    $ roslaunch agv_mecanum_simulation agvmecanum_gazebo_depo.launch

Solo-Rviz Launching:

    $ roslaunch agv_mecanum_simulation agvmecanum_rviz_standalone.launch
    
Rviz (with Gazebo) Launching:

    $ roslaunch agv_mecanum_simulation agvmecanum_rviz.launch
    
AGV Mecanum Teleop Launching:

    $ rosrun agv_mecanum_teleop agv_teleop_twist_keyboard.py


![Image of AGV Mecanum Cameras](https://github.com/inomuh/agv_mecanum/blob/main/images/agv_mecanum_withcameras.png)
    
-----------------------------------------------------------------------------------------------------------------------
Requirements:
-------------
- In order for the sensors to work properly, "gazebo_ros_pkgs" files must be downloaded to your computer.

        $ sudo apt-get install ros-noetic-gazebo-ros-pkgs
        
-------------------------------------------------------------------------------
Changelog:
----------
Update v1.0 - 07.12.20
----------------------
- First version
