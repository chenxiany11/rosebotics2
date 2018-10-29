"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """


    # Test for spin_in_place_degrees():
    run_turn_degrees(-720)

def run_go_straight_inches(n):
    robot1 = rb.Snatch3rRobot()
    robot1.drive_system.go_straight_inches(n)

    # Test for spin_in_place_degrees():
def run_spin_in_place_degrees(n):
    robot1 = rb.Snatch3rRobot()
    robot1.drive_system.spin_in_place_degrees(n)

def run_turn_degrees(n):
    robot1 = rb.Snatch3rRobot()
    robot1.drive_system.turn_degrees(n)


main()

