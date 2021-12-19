from djitellopy import Tello
import time


tello = Tello()

tello.connect()
print(tello.get_current_state())

tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(1)

tello.takeoff()
 pad = tello.get_mission_pad_id()


#detect and react to pads until we see pad #1
#pad 1 is top left
#pad 2 is top right
#pad 3 is bottom left
#pad 4 is bottom right

while pad != 1:
    if pad == 3:
        tello.move_up(30)

    if pad == 4:
        tello.move_up(30)
        tello.move_left(30)

    if pad == 2:
        tello.move_left(30)

    pad = tello.get_mission_pad_id()


#termination
tello.disable_mission_pads()
tello.land()
tello.end()

#tello.go_xyz_speed_mid(25, 25, 120, 20, 1)

#tello.go_xyz_speed_mid(-50, -50, 120, 20, 1)

#tello.go_xyz_speed_mid(25, 25, 120, 20, 1)

#tello.go_xyz_speed_mid(0, 0, 50, 20, 1)
