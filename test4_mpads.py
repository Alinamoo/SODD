from djitellopy import Tello
import time

tello = Tello()

tello.connect()

tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(0)

print(tello.get_current_state())
#tello.wait_for_connection(10.0)
tello.takeoff()

# x is forward / backward
# y is left / right
# z up / down
speed = 20
tello.go_xyz_speed(0, 0, 50, speed)

# Mission pads arranged as:
# 1 meter apart
# code as given goes from 1-2-3-4-1
# 1   2

# 4   3

# change arrangement to start in different position
tello.go_xyz_speed_mid(0, 0, 25, speed, 1)
tello.go_xyz_speed(0, -100, 50, speed)
tello.go_xyz_speed_mid(0, 0, 25, speed, 2)
tello.go_xyz_speed(-100, 0, 50, speed)
tello.go_xyz_speed_mid(0, 0, 25, speed, 3)
tello.go_xyz_speed(0, 100, 50, speed)
tello.go_xyz_speed_mid(0, 0, 25, speed, 4)
tello.go_xyz_speed(100, 0, 50, speed)
tello.go_xyz_speed(0, 0, 100, 2*speed)

tello.land()