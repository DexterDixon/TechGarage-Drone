"""
Example Takeoff and Land Program
Created for Tech Garage
Contributors: Dexter Dixon, Danny Dasilva
"""
#This imports all the necessary packages for the program
import pygame
import tello
import time

#This variable allows us to use "drone" instead of the long line
drone = tello.Tello('192.168.10.2', 8888, imperial=False)

#Initializes Pygame and one joystick
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

#Takeoff functoin
drone.takeoff()
#Function that stops the program before running the next command for (x) amount of seconds
time.sleep(3)
#Landing function
drone.land()




