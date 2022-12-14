# voice robot

this robot will listen to the connected mic and filter the commands then send them one by on to the hardware motors.

## Installation

move this git repo to catkin_ws/src

Use the package manager [pip](https://pip.pypa.io/en/stable/) and [ros](https://ros.org)

### new terminal
```bash
roscore
```
### new terminal

```bash
pip install pyaudio
cd ~/catkin_ws
catkin_make
sudo chmod a+rw /dev/ttyUSB0
rosrun rosserial_python serial_node.py /dev/ttyUSB0
```

### new terminal

```bash
rosrun rosserial_python pub.p
```
notice to replace /dev/ttyUSB0 with your connected serial port with arduino
## available commands



forward

***

backward

___

right
___

left
___

any number between 0 and 360

