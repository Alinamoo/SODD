from djitellopy import Tello
import time


tello = Tello()

tello.connect()
print(tello.get_current_state())

tello.takeoff()

tello.enable_mission_pads()



tello.go_xyz_speed_mid(25, 25, 120, 20, 1)

tello.go_xyz_speed_mid(-50, -50, 120, 20, 1)

#tello.go_xyz_speed_mid(25, 25, 120, 20, 1)

tello.go_xyz_speed_mid(0, 0, 50, 20, 1)


tello.land()