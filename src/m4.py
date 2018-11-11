"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    test_go_until_color_is(rb.RED)
    # test_polygon(4)
    # test_get_away_from_me()
    # test_the_floor_is_lava()

def test_go_until_color_is(n):
    lenin = rb.Snatch3rRobot()
    lenin.color_sensor.go_until_color_is(n)


def test_polygon(n):
    lenin = rb.Snatch3rRobot()
    lenin.drive_system.polygon(n)

def test_get_away_from_me():
    lenin = rb.Snatch3rRobot()
    lenin.proximity_sensor.get_away_from_me()

def test_the_floor_is_lava():
    lenin = rb.Snatch3rRobot()
    lenin.color_sensor.the_floor_is_lava(lenin)

main()
