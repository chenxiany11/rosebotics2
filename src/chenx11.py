"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    # Test for go_straight_inches():
    run_go_straight_inches()

    # Test for spin_in_place_degrees():
    run_spin_in_place_degrees()

def run_go_straight_inches():
    robot1 = rb.Snatch3rRobot()
    robot1.drive_system.go_straight_inches(40)

    # Test for spin_in_place_degrees():
def run_spin_in_place_degrees():
    robot1 = rb.Snatch3rRobot()
    robot1.drive_system.spin_in_place_degrees(50)

main()
