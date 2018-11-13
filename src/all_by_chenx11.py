"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    sprint_1()
    # sprint_2()


def sprint_1():
    # Refer to rosebotics_new --> class DriveSystem (line 145)
    # This is a test for the DriveSystem
    chen = rb.Snatch3rRobot()  # Makes the robot

    print('Test: Make robot go forth 10 inches')
    chen.drive_system.go_straight_inches(10)  # (line 203)
    print('Test finished!')

    print('Test: Make robot go backwards 10 inches')
    chen.drive_system.go_straight_inches(-10)  # (line 203)
    print('Test finished!')

    print('Test: Make robot spin a 360')
    chen.drive_system.spin_in_place_degrees(360)  # (line 228)
    print('Test finished!')

    print('Test: Make the robot turn a 720 in the opposite direction')
    chen.drive_system.turn_degrees(-720)   # (line 254)
    print('Test finished!')

    print('Test: Make a pentagon')
    chen.drive_system.polygon(5)  # (line 288)

def sprint_2():
    chen = rb.Snatch3rRobot()
    print('Test: Make robot beep if someone waves')
    chen.proximity_sensor.happy_to_see_you()
    print('Test finished!')

main()

