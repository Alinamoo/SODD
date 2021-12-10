from djitellopy import Tello
import time


tello = Tello()

tello.connect()


tello.takeoff()

#tello.move_left(100)
tello.rotate_clockwise(90)
#tello.move_forward(100)
print(tello.get_current_state())

tello.rotate_counter_clockwise(90)

time.sleep(3)

tello.land()