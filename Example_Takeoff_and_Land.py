import tello
import time
drone = tello.Tello('192.168.10.2', 8888, imperial=False)

drone.takeoff()
time.sleep(3)
drone.land()




