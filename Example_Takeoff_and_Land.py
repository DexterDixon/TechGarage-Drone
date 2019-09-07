import tello
import time
drone = tello.Tello('192.168.10.2', 8888, imperial=False)

debug = drone.takeoff()
time.sleep(3)
debug = drone.land()



