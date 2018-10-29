"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    color()


def color():
    chen = rb.Snatch3rRobot()

    while True:
        if chen.color_sensor.get_color() != rb.Color.BLUE.value:
            chen.drive_system.start_moving()
        else:
            chen.drive_system.stop_moving()
            break

main()
