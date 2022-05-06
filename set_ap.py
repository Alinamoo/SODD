from djitellopy import Tello
import time

tello = Tello()

tello.connect()

print(tello.get_current_state())

tello.connect_to_wifi('AndroidAP', '3c11d944f399') #SSID pwd