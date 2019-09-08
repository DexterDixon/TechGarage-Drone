"""
Example Joystick Control Template
Created for Tech Garage
Contributors: Dexter Dixon, Danny Dasilva
"""
#This imports all the necessary packages for the program
import tello
import time
import pygame

pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

while True:
#These are examples of using if statments to trigger
#actions based on your button presses.
#In the first example if you press button 1 or if button(1) equals 1
#Then run the line of code under the if statment
#Whenever you do aren't pressing a button you will get a value of 0 and when you are pressing the button you get a value of 0
    if joystick.get_button(1) == 1:
        print("Button 1 pressed!")

    if joystick.get_button(2) == 1:
        print("Button 2 pressed!")

    if joystick.get_button(3) == 1:
        print("Button 3 pressed")

    if joystick.get_button(4) == 1:
        print("Button 4 pressed")

    if joystick.get_button(5) == 1:
        print("Button 5 pressed")

    if joystick.get_button(6) == 1:
        print("Button 6 pressed")

    if joystick.get_button(7) == 1:
        print("Button 7 pressed")

    if abs(joystick.get_axis(0)) > 0.05 or abs(joystick.get_axis(1)) > 0.05:
        print("Left stick %f, %f" % (joystick.get_axis(0),
                                     joystick.get_axis(1)))

    if abs(joystick.get_axis(3)) > 0.05 or abs(joystick.get_axis(4)) > 0.05:
        print("Right stick %f, %f" % (joystick.get_axis(3),
                                      joystick.get_axis(4)))

    # Triggers initialize at 0 and then reset to -1
    if joystick.get_axis(2) != 0:
        left_trigger_initialized = True

    if joystick.get_axis(5) != 0:
        right_trigger_initialized = True

    if left_trigger_initialized and abs(joystick.get_axis(2) > -.95):
        print("Left trigger %f" % joystick.get_axis(2))

    if right_trigger_initialized and abs(joystick.get_axis(5) > -.95):
        print("Right trigger %f" % joystick.get_axis(5))

        (hat_x, hat_y) = joystick.get_hat(0)
        if (hat_x != 0 or hat_y !=0):
            print("Hat %d, %d" % (hat_x, hat_y))
