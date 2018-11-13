"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    polygon(4)

def polygon(n):
    chen = rb.Snatch3rRobot()
    for k in range(n):
        chen.drive_system.go_straight_inches(10)
        chen.drive_system.spin_in_place_degrees(360/n)


main()
