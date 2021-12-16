from djitellopy import Tello
import time


tello = Tello()

tello.connect()
tello.wait_for_connection(10.0)
tello.takeoff()


tello.move_left(100)
time.sleep(5)
#tello.rotate_clockwise(90)
tello.move_forward(100)
time.sleep(5)
tello.move_right(100)
time.sleep(5)
tello.move_back(100)
time.sleep(5)


tello.move_down(100)
#print(tello.get_current_state())

#tello.rotate_counter_clockwise(90)

tello.land()