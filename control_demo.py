from djitellopy import Tello
import time


tello = Tello()

tello.connect()

user_input = ' '

while user_input != 'x':
    user_input = input()
    
    if user_input == 't':
        print("takeoff")
        tello.takeoff()
    if user_input == 'l':
        print("land")
        tello.land()    

    if user_input == 'a':
        print("left")
        tello.move_left(30)
    if user_input == 'w':
        print("forward")
        tello.move_forward(30)
    if user_input == 'd':
        print("right")
        tello.move_right(30)
    if user_input == 's':
        print("back")
        tello.move_back(30)

    if user_input == 'e':
        print("up")
        tello.move_up(30)    
    if user_input == 'q':
        print("down")
        tello.move_down(30)
    
print("exit")    
