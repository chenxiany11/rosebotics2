"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    # sprint_1()
    sprint_2()


def sprint_1():
    # Refer to rosebotics_new --> class DriveSystem (line 145)
    # This is a test for the DriveSystem
    stalin = rb.Snatch3rRobot()  # Makes the robot

    print('Test: ')
    stalin.drive_system.go_straight_inches(10)  # (line 203)
    print('Test finished!')

    print('Test: ')
    stalin.drive_system.go_straight_inches(-10)  # (line 203)
    print('Test finished!')

    print('Test: ')
    stalin.drive_system.spin_in_place_degrees(360)  # (line 228)
    print('Test finished!')

    print('Test: ')
    stalin.drive_system.turn_degrees(-720)  # (line 254)
    print('Test finished!')


def sprint_2():
    print()

main()
