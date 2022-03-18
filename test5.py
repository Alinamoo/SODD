from djitellopy import Tello
import time


tello = Tello()

tello.connect()

print(tello.get_current_state())
#tello.wait_for_connection(10.0)
tello.takeoff()

# x is forward / backward
# y is left / right
# z up / down
speed = 100
tello.go_xyz_speed(0, 0, 50, speed)

tello.flip('l')
tello.flip('r')
tello.flip('f')
tello.flip('b')
'''
tello.go_xyz_speed(50, 0, 0, speed)
tello.go_xyz_speed(0, -50, 0, speed)
tello.go_xyz_speed(-50, 0, 0, speed)
tello.go_xyz_speed(0, 50, 0, speed)
'''

tello.land()